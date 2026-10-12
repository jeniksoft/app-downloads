# Python a PyTorch – registrace vývojářských nástrojů

`register-development-tools.ps1` idempotentně objeví běžná umístění vývojářských nástrojů ve Windows a přidá je do uživatelského `PATH` bez administrátorských práv.

Registruje zejména:

- Python Launcher, všechny nalezené instalace Pythonu, jejich `Scripts` a Python virtualenvy;
- PyTorch/DirectML virtualenv, pokud existuje;
- Gradle, JDK, Ollama a jeho pomocné binárky;
- WinGet Links, npm, Cargo, `.NET tools`, Scoop a Node.js;
- Windows App Execution Aliases, pokud je přítomen `winget.exe` (WinGet,
  WinDbg a všechny dostupné architektury `cdb`/`dbgsrv`/`kd`/`ntsd`; skutečné
  instalace Pythonu mají přednost před Store aliasem);
- Android SDK (`platform-tools`, emulator, qemu, command-line tools a build-tools).
- Hyper-V host/QA utilities (`VMCreate`, `VMImport` a `InspectVhdDialog`), pokud
  je hostitelská instalace Hyper-V přítomná;
- Visual Studio Build Tools (MSBuild, CMake, Ninja, MSVC/LLVM, `vswhere` a
  inicializační skripty), Roslyn (`csc`/`vbc`), VSTest, NuGet build task,
  Code Coverage CLI, coverage instrumentaci, VSDiagnostics, FxCopCmd, vcpkg,
  ARM64 LLVM/clang-format a testovací dump utility;
- Windows SDK (x64/x86/ARM64 build, resource, signing, shader, package,
  deployment, tracing, `cppwinrt` a accessibility/UI verification nástroje), včetně
  explicitních podadresářů `AccChecker` a `UIAVerify`; dále TAEF testovací
  runtime (`TE`, `TE.ProcessHost`, `Wex.Services` a broker) v nativní x64 a
  MinTe variantě. Volitelně se přidají také přesné kořeny Windows Debuggers a
  Windows Performance Toolkit, pokud jsou skutečně nainstalované;
- WiX 3.x i novější WiX CLI, včetně manuálně nainstalovaných verzí pod
  `C:\Tools\WiXToolset`;
- .NET Framework SDK nástroje (`ildasm`, `gacutil`, `resgen`, `sn` a další),
  AMD Ryzen Master CLI, 7-Zip z registrované instalace, VeraCrypt CLI,
  ZeroTier CLI a Git Bash (`bash`/`sh`);
- pomocné JDK příkazy (`jconsole`, `jpackage`, `jwebserver`, `keytool`) a
  Ollama runtime helper `llama-server`, pokud jsou součástí nalezené instalace;
- GitHub CLI z WinGetu nebo jako přesný fallback z instalace Codex Task Boardu;
- `dotnet` a Git CLI z jejich standardních instalačních umístění.
- Unreal Engine z nainstalovaných Epic Games kořenů na připojených discích
  (Editor/Cmd, UnrealPak, UnrealBuildTool, RunUAT, AutomationTool, Insights,
  Frontend, trace server a další build/test binárky); přidává se jen konkrétní
  engine/tool adresář, nikoli projekt, cache nebo celý disk;
- UnrealTraceServer z verzovaných per-user Epic/UnrealTrace umístění a
  volitelné Epic UnrealBuildAccelerator/Zen nástroje, pokud skutečně obsahují
  spustitelné soubory.

Součástí kontroly jsou také systémové vývojářské/QA nástroje, které už Windows
zpřístupňuje přes systémový PATH, například `appverif`, `wpr`, `appcert`,
`appcertui` a `nmake`; skript je pouze ověří a nepřidává podruhé systémové
adresáře.

Stávající uživatelské položky `PATH` zachovává. Do systémového `PATH` ani do registru aplikací nezasahuje. Skript nic nestahuje ani neinstaluje; pouze registruje existující nástroje.
U Visual Studio toolchainu registrace zpřístupní binárky přes `PATH`; pro
kompilaci, která vyžaduje `INCLUDE`/`LIB`, použij Developer PowerShell nebo
`VsDevCmd.bat`, protože samotný `PATH` tyto SDK proměnné nenastavuje.
Git `usr\bin` se globálně neregistruje schválně, protože obsahuje Unixové
kompatibilní příkazy, které by mohly zastínit stejnojmenné Windows nástroje;
Git Bash si tento interní adresář nastaví samo při spuštění.
Stejně se záměrně nepřidávají interní GUI aplikace, duplicitní 7-Zip z ovladačů
ani alternativní `adb` z BlueStacks, protože by mohly zastínit oficiální SDK
verze. Registrují se pouze přesné adresáře ověřených CLI/developer nástrojů.
Audit záměrně vynechává i interní `ffmpeg`/7-Zip z BlueStacks/AMD, Git
`usr\bin` a GUI/launcher binárky; jejich nalezení samo o sobě neznamená, že
patří do globálního vývojového PATH.
Stejným pravidlem se vynechávají CPU-Z GUI, DirectX instalátory, AMD OpenVR
registrátory a Codex/cache kopie nástrojů; registrují se jen přesně vymezené
vývojové nebo QA CLI kořeny.
U Unreal Engine se prohledávají pouze přesné `Epic Games` kořeny a standardní
engine tool adresáře; projektové `Binaries`, `Intermediate`, `Saved`,
`DerivedDataCache` ani launcher se globálně nepřidávají.
Kořen Hyper-V je výjimka pro tři konkrétní hostitelské VM/VHD QA nástroje;
registruje se pouze tehdy, když obsahuje skutečné spustitelné soubory.

## Použití

Nejdříve lze zobrazit nález bez změny:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\register-development-tools.ps1 -AndroidSdkRoot 'Z:\Android\Sdk'
```

Pro trvalou registraci a kontrolu PyTorch/DirectML:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\register-development-tools.ps1 -Apply -Verify -AndroidSdkRoot 'Z:\Android\Sdk'
```

Po dokončení otevři nový terminál nebo restartuj aplikaci, protože už běžící procesy mají starou kopii `PATH`. Volba `-AdditionalRoot` umožní přidat další konkrétní nástrojový adresář:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\register-development-tools.ps1 -Apply -AdditionalRoot 'D:\Tools\bin'
```
