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
$commandsToCheck = @('python', 'py', 'pip', 'torchrun', 'gradle', 'java', 'ollama', 'gh', 'adb', 'emulator', 'android')
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
