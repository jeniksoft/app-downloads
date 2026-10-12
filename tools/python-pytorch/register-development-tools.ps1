[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [switch]$Apply,
    [switch]$Verify,
    [string]$AndroidSdkRoot,
    [string[]]$AdditionalRoot = @()
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Add-ToolDirectory {
    param([AllowNull()][string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) {
        return
    }

    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        return
    }

    $resolved = (Resolve-Path -LiteralPath $Path).Path.TrimEnd('\')
    $toolFiles = @(Get-ChildItem -LiteralPath $resolved -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.exe', '.com', '.cmd', '.bat' })
    if ($toolFiles.Count -eq 0) {
        return
    }

    $key = $resolved.ToLowerInvariant()
    if (-not $script:seenCandidates.ContainsKey($key)) {
        $script:seenCandidates[$key] = $true
        [void]$script:candidates.Add($resolved)
    }
}

function Add-AndroidToolDirectories {
    param([string]$SdkRoot)

    if ([string]::IsNullOrWhiteSpace($SdkRoot) -or
        -not (Test-Path -LiteralPath $SdkRoot -PathType Container)) {
        return
    }

    Add-ToolDirectory (Join-Path $SdkRoot 'platform-tools')
    Add-ToolDirectory (Join-Path $SdkRoot 'emulator')
    Add-ToolDirectory (Join-Path $SdkRoot 'emulator\qemu\windows-x86_64')

    $cmdlineRoot = Join-Path $SdkRoot 'cmdline-tools'
    if (Test-Path -LiteralPath $cmdlineRoot -PathType Container) {
        $cmdlineVersions = @(Get-ChildItem -LiteralPath $cmdlineRoot -Directory -ErrorAction SilentlyContinue |
            Sort-Object Name -Descending)
        foreach ($version in $cmdlineVersions) {
            Add-ToolDirectory (Join-Path $version.FullName 'bin')
        }
    }

    $buildToolsRoot = Join-Path $SdkRoot 'build-tools'
    if (Test-Path -LiteralPath $buildToolsRoot -PathType Container) {
        $buildTools = @(Get-ChildItem -LiteralPath $buildToolsRoot -Directory -ErrorAction SilentlyContinue |
            Sort-Object Name -Descending)
        foreach ($version in $buildTools) {
            Add-ToolDirectory $version.FullName
        }
    }
}

function Add-VisualStudioToolDirectories {
    param([string]$VisualStudioRoot)

    if ([string]::IsNullOrWhiteSpace($VisualStudioRoot) -or
        -not (Test-Path -LiteralPath $VisualStudioRoot -PathType Container)) {
        return
    }

    # Keep discovery scoped to installed VS instances. Do not expose the whole
    # Program Files tree or arbitrary application directories through PATH.
    $instances = @()
    foreach ($year in @(Get-ChildItem -LiteralPath $VisualStudioRoot -Directory -ErrorAction SilentlyContinue)) {
        $instances += @(Get-ChildItem -LiteralPath $year.FullName -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -notin @('Installer', 'Shared') })
    }

    foreach ($instance in @($instances | Sort-Object FullName -Descending)) {
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\Tools')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE\CommonExtensions\Microsoft\CMake\Ninja')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE\CommonExtensions\Microsoft\NuGet')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE\CommonExtensions\Microsoft\TestWindow')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE\Extensions\Microsoft\CodeCoverage.Console')
        Add-ToolDirectory (Join-Path $instance.FullName 'Common7\IDE\Extensions\TestPlatform')
        Add-ToolDirectory (Join-Path $instance.FullName 'MSBuild\Current\Bin\amd64')
        Add-ToolDirectory (Join-Path $instance.FullName 'MSBuild\Current\Bin')
        Add-ToolDirectory (Join-Path $instance.FullName 'MSBuild\Current\Bin\Roslyn')
        Add-ToolDirectory (Join-Path $instance.FullName 'VC\Auxiliary\Build')
        Add-ToolDirectory (Join-Path $instance.FullName 'VC\Tools\Llvm\bin')
        Add-ToolDirectory (Join-Path $instance.FullName 'VC\Tools\Llvm\x64\bin')

        $msvcRoot = Join-Path $instance.FullName 'VC\Tools\MSVC'
        if (Test-Path -LiteralPath $msvcRoot -PathType Container) {
            foreach ($version in @(Get-ChildItem -LiteralPath $msvcRoot -Directory -ErrorAction SilentlyContinue |
                Sort-Object Name -Descending)) {
                # x64 is first so ordinary lookup selects the native compiler;
                # other supported host/target pairs remain discoverable later.
                foreach ($toolPath in @(
                    (Join-Path $version.FullName 'bin\Hostx64\x64'),
                    (Join-Path $version.FullName 'bin\Hostx64\x86'),
                    (Join-Path $version.FullName 'bin\Hostx64\arm64'),
                    (Join-Path $version.FullName 'bin\Hostx86\x86'),
                    (Join-Path $version.FullName 'bin\Hostx86\x64')
                )) {
                    Add-ToolDirectory $toolPath
                }
            }
        }
    }

    Add-ToolDirectory (Join-Path $VisualStudioRoot 'Installer')
}

function Add-WindowsSdkToolDirectories {
    param([string]$WindowsKitsRoot)

    if ([string]::IsNullOrWhiteSpace($WindowsKitsRoot) -or
        -not (Test-Path -LiteralPath $WindowsKitsRoot -PathType Container)) {
        return
    }

    foreach ($kit in @(Get-ChildItem -LiteralPath $WindowsKitsRoot -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^(10|8\.1)$' } | Sort-Object Name -Descending)) {
        Add-ToolDirectory (Join-Path $kit.FullName 'App Certification Kit')
        $binRoot = Join-Path $kit.FullName 'bin'
        if (-not (Test-Path -LiteralPath $binRoot -PathType Container)) {
            continue
        }

        $versionDirectories = @(Get-ChildItem -LiteralPath $binRoot -Directory -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -match '^\d+\.\d+\.\d+\.\d+$' } |
            Sort-Object Name -Descending)
        if ($versionDirectories.Count -gt 0) {
            foreach ($version in $versionDirectories) {
                foreach ($architecture in @('x64', 'x86', 'arm64')) {
                    Add-ToolDirectory (Join-Path $version.FullName $architecture)
                }
            }
        }
        else {
            foreach ($architecture in @('x64', 'x86', 'arm64')) {
                Add-ToolDirectory (Join-Path $binRoot $architecture)
            }
        }
    }
}

function Add-AdditionalDeveloperToolDirectories {
    # These are deliberately narrow, well-known developer/QA tool locations.
    # Do not add whole application trees or Git's usr\bin globally: the latter
    # contains Unix compatibility commands which can shadow Windows commands.
    Add-ToolDirectory (Join-Path ${env:ProgramFiles} 'dotnet')

    foreach ($gitRoot in @(
            (Join-Path ${env:ProgramFiles} 'Git'),
            (Join-Path ${env:ProgramFiles(x86)} 'Git')
        )) {
        if (Test-Path -LiteralPath $gitRoot -PathType Container) {
            Add-ToolDirectory (Join-Path $gitRoot 'cmd')
            Add-ToolDirectory (Join-Path $gitRoot 'bin')
        }
    }

    # WiX 3.x and 4+/7 installations use different command names and layouts.
    # Register the versioned roots that are actually present, including the
    # manually provisioned C:\Tools tree used by local packaging workflows.
    foreach ($wixParent in @(
            ${env:ProgramFiles},
            ${env:ProgramFiles(x86)},
            (Join-Path ${env:SystemDrive} 'Tools\WiXToolset')
        )) {
        if (-not (Test-Path -LiteralPath $wixParent -PathType Container)) {
            continue
        }

        $wixRoots = @()
        if ((Split-Path -Leaf $wixParent) -eq 'WiXToolset') {
            $wixRoots = @(Get-ChildItem -LiteralPath $wixParent -Directory -ErrorAction SilentlyContinue |
                Where-Object { $_.Name -match '^v\d' } |
                Sort-Object Name -Descending)
        }
        elseif ((Split-Path -Leaf $wixParent) -match '^WiX Toolset v') {
            $wixRoots = @(Get-Item -LiteralPath $wixParent -ErrorAction SilentlyContinue)
        }
        else {
            $wixRoots = @(Get-ChildItem -LiteralPath $wixParent -Directory -ErrorAction SilentlyContinue |
                Where-Object { $_.Name -match '^WiX Toolset v' } |
                Sort-Object Name -Descending)
        }

        foreach ($wixRoot in $wixRoots) {
            foreach ($toolPath in @(
                    (Join-Path $wixRoot.FullName 'bin'),
                    (Join-Path $wixRoot.FullName 'SDK'),
                    (Join-Path $wixRoot.FullName 'sdk'),
                    (Join-Path $wixRoot.FullName 'x86'),
                    (Join-Path $wixRoot.FullName 'x64')
                )) {
                Add-ToolDirectory $toolPath
            }
            # A manually extracted WiX 3.x tree keeps its CLI directly in the
            # version directory, while installed WiX keeps it under bin.
            Add-ToolDirectory $wixRoot.FullName
        }
    }

    # .NET Framework SDK utilities are separate from dotnet.exe and are not
    # included in the modern Windows SDK bin directories.
    $legacyWindowsSdkRoot = Join-Path ${env:ProgramFiles(x86)} 'Microsoft SDKs\Windows'
    if (Test-Path -LiteralPath $legacyWindowsSdkRoot -PathType Container) {
        foreach ($windowsSdk in @(Get-ChildItem -LiteralPath $legacyWindowsSdkRoot -Directory -ErrorAction SilentlyContinue |
                Where-Object { $_.Name -match '^v\d' })) {
            $sdkBin = Join-Path $windowsSdk.FullName 'bin'
            foreach ($toolDirectory in @(Get-ChildItem -LiteralPath $sdkBin -Directory -ErrorAction SilentlyContinue |
                    Where-Object { $_.Name -match '(?i)tools$' })) {
                Add-ToolDirectory $toolDirectory.FullName
                Add-ToolDirectory (Join-Path $toolDirectory.FullName 'x64')
            }
        }
    }

    # AMD ships a supported command-line diagnostic utility with Ryzen Master.
    Add-ToolDirectory (Join-Path ${env:ProgramFiles} 'AMD\RyzenMasterSDK\AMDRyzenMasterCLI\bin-prebuilt')

    # 7-Zip is often installed outside Program Files. Use only the registered
    # 7-Zip uninstall location rather than scanning arbitrary user directories.
    $uninstallRoots = @(
        'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
        'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
        'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*'
    )
    foreach ($installedTool in @(Get-ItemProperty -Path $uninstallRoots -ErrorAction SilentlyContinue |
            Where-Object {
                $displayName = $_.PSObject.Properties['DisplayName']
                $installLocation = $_.PSObject.Properties['InstallLocation']
                $null -ne $displayName -and
                    $null -ne $installLocation -and
                    $displayName.Value -match '(?i)^7-Zip\b' -and
                    -not [string]::IsNullOrWhiteSpace([string]$installLocation.Value)
            })) {
        Add-ToolDirectory ([string]$installedTool.InstallLocation)
    }
    Add-ToolDirectory (Join-Path ${env:ProgramFiles} '7-Zip')
    Add-ToolDirectory (Join-Path ${env:ProgramFiles(x86)} '7-Zip')
}

$script:candidates = New-Object 'System.Collections.Generic.List[string]'
$script:seenCandidates = @{}
$localPrograms = Join-Path $env:LOCALAPPDATA 'Programs'
$pythonRoot = Join-Path $localPrograms 'Python'

$pythonInstallations = @()
if (Test-Path -LiteralPath $pythonRoot -PathType Container) {
    $pythonInstallations = @(Get-ChildItem -LiteralPath $pythonRoot -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^Python\d+$' } |
        Sort-Object Name -Descending)
}

# Prefer a discovered PyTorch/DirectML environment for the default `python` command,
# then expose every Python installation and its Scripts directory.
$venvScripts = @()
if (Test-Path -LiteralPath $pythonRoot -PathType Container) {
    $venvScripts = @(Get-ChildItem -LiteralPath $pythonRoot -Directory -Recurse -ErrorAction SilentlyContinue |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'Scripts\python.exe') } |
        ForEach-Object { Join-Path $_.FullName 'Scripts' } |
        Sort-Object { if ($_ -match 'pytorch-directml') { '0' } else { '1' } }, { $_ })
}
foreach ($venvScript in $venvScripts) {
    Add-ToolDirectory $venvScript
}

Add-ToolDirectory (Join-Path $pythonRoot 'Launcher')

foreach ($pythonInstallation in $pythonInstallations) {
    Add-ToolDirectory $pythonInstallation.FullName
    Add-ToolDirectory (Join-Path $pythonInstallation.FullName 'Scripts')
}

if (Test-Path -LiteralPath $localPrograms -PathType Container) {
    foreach ($gradle in @(Get-ChildItem -LiteralPath $localPrograms -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^gradle-' } | Sort-Object Name -Descending)) {
        Add-ToolDirectory (Join-Path $gradle.FullName 'bin')
    }
}

$jdkRoot = Join-Path $localPrograms 'Microsoft'
if (Test-Path -LiteralPath $jdkRoot -PathType Container) {
    foreach ($jdk in @(Get-ChildItem -LiteralPath $jdkRoot -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^jdk-' } | Sort-Object Name -Descending)) {
        Add-ToolDirectory (Join-Path $jdk.FullName 'bin')
    }
}

Add-ToolDirectory (Join-Path $localPrograms 'Ollama')
Add-ToolDirectory (Join-Path $localPrograms 'Ollama\lib\ollama')
Add-ToolDirectory (Join-Path $env:LOCALAPPDATA 'Microsoft\WinGet\Links')
Add-ToolDirectory (Join-Path $env:APPDATA 'npm')
Add-ToolDirectory (Join-Path $env:USERPROFILE '.cargo\bin')
Add-ToolDirectory (Join-Path $env:USERPROFILE '.dotnet\tools')
Add-ToolDirectory (Join-Path $env:USERPROFILE 'scoop\shims')
Add-ToolDirectory (Join-Path $localPrograms 'nodejs')
Add-ToolDirectory (Join-Path ${env:ProgramFiles} 'nodejs')

foreach ($visualStudioRoot in @(
        (Join-Path ${env:ProgramFiles(x86)} 'Microsoft Visual Studio'),
        (Join-Path ${env:ProgramFiles} 'Microsoft Visual Studio')
    )) {
    Add-VisualStudioToolDirectories $visualStudioRoot
}

foreach ($windowsKitsRoot in @(
        (Join-Path ${env:ProgramFiles(x86)} 'Windows Kits'),
        (Join-Path ${env:ProgramFiles} 'Windows Kits')
    )) {
    Add-WindowsSdkToolDirectories $windowsKitsRoot
}

Add-AdditionalDeveloperToolDirectories

$androidRoots = New-Object 'System.Collections.Generic.List[string]'
foreach ($root in @(
        $AndroidSdkRoot,
        $env:ANDROID_SDK_ROOT,
        $env:ANDROID_HOME,
        (Join-Path $env:LOCALAPPDATA 'Android\Sdk')
    )) {
    if (-not [string]::IsNullOrWhiteSpace($root) -and
        -not $androidRoots.Contains($root)) {
        [void]$androidRoots.Add($root)
    }
}
foreach ($androidRoot in $androidRoots) {
    Add-AndroidToolDirectories $androidRoot
}

foreach ($extraRoot in $AdditionalRoot) {
    Add-ToolDirectory $extraRoot
}

$existingUserPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$existingEntries = @()
if (-not [string]::IsNullOrWhiteSpace($existingUserPath)) {
    $existingEntries = @($existingUserPath -split ';' | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
}

$orderedEntries = New-Object 'System.Collections.Generic.List[string]'
$seenEntries = @{}
foreach ($entry in @($script:candidates) + $existingEntries) {
    $clean = $entry.Trim().TrimEnd('\')
    if ([string]::IsNullOrWhiteSpace($clean)) {
        continue
    }
    $key = $clean.ToLowerInvariant()
    if (-not $seenEntries.ContainsKey($key)) {
        $seenEntries[$key] = $true
        [void]$orderedEntries.Add($clean)
    }
}

Write-Output ('DISCOVERED_TOOL_DIRECTORIES=' + $script:candidates.Count)
foreach ($candidate in $script:candidates) {
    Write-Output ('DISCOVERED=' + $candidate)
}

$newUserPath = $orderedEntries -join ';'
if ($Apply) {
    if ($PSCmdlet.ShouldProcess('Current user PATH', 'Register discovered development tool directories')) {
        [Environment]::SetEnvironmentVariable('Path', $newUserPath, 'User')
        Write-Output ('PATH_UPDATED=1;USER_ENTRIES=' + $orderedEntries.Count)
    }
}
else {
    Write-Output ('DRY_RUN=1;USE_-Apply_TO_PERSIST;USER_ENTRIES=' + $orderedEntries.Count)
}

# Refresh only this process so the optional verification does not require a new shell.
$env:Path = $newUserPath + ';' + [Environment]::GetEnvironmentVariable('Path', 'Machine')
$commandsToCheck = @(
    'python', 'py', 'pip', 'torchrun', 'gradle', 'java', 'javac', 'ollama', 'gh',
    'adb', 'emulator', 'sdkmanager', 'avdmanager', 'android', 'cmake', 'ninja',
    'msbuild', 'cl', 'clang-cl', 'rc', 'mt', 'signtool', 'vswhere', 'dotnet',
    'wix', 'candle', 'light', 'dark', 'heat', 'ildasm', 'gacutil', 'resgen',
    'sn', 'csc', 'vbc', 'vstest.console', 'NuGet.Build.Tasks.Console',
    'Microsoft.CodeCoverage.Console', '7z', 'git', 'bash', 'sh',
    'AMDRyzenMasterCLI'
)
foreach ($commandName in $commandsToCheck) {
    $command = Get-Command $commandName -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -ne $command) {
        Write-Output ('COMMAND=' + $commandName + '|' + $command.Source)
    }
}

if ($Verify) {
    $pythonCommand = Get-Command 'python' -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -eq $pythonCommand) {
        throw 'Python was not found after PATH registration.'
    }

    $probeOutput = @(& $pythonCommand.Source -c "import torch; print('TORCH_VERSION=' + torch.__version__); import torch_directml; print('TORCH_DIRECTML_IMPORT=ok')" 2>&1)
    foreach ($probeLine in $probeOutput) {
        Write-Output ('PYTORCH_PROBE=' + $probeLine)
    }
    if ($LASTEXITCODE -ne 0) {
        throw 'PyTorch/DirectML import verification failed.'
    }
}

Write-Output 'NOTE=Existing terminals keep their old PATH; open a new terminal or restart the application.'
