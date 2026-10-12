# Python a PyTorch – registrace vývojářských nástrojů

`register-development-tools.ps1` idempotentně objeví běžná umístění vývojářských nástrojů ve Windows a přidá je do uživatelského `PATH` bez administrátorských práv.

Registruje zejména:

- Python Launcher, všechny nalezené instalace Pythonu, jejich `Scripts` a Python virtualenvy;
- PyTorch/DirectML virtualenv, pokud existuje;
- Gradle, JDK, Ollama a jeho pomocné binárky;
- WinGet Links, npm, Cargo, `.NET tools`, Scoop a Node.js;
- Windows App Execution Aliases, pokud je přítomen `winget.exe` (WinGet a
  případné nainstalované WinDbg aliasy; skutečné instalace Pythonu mají
  přednost před Store aliasem);
- Android SDK (`platform-tools`, emulator, qemu, command-line tools a build-tools).
- Visual Studio Build Tools (MSBuild, CMake, Ninja, MSVC/LLVM, `vswhere` a
  inicializační skripty), Roslyn (`csc`/`vbc`), VSTest, NuGet build task a
  Code Coverage CLI;
- Windows SDK (x64/x86/ARM64 build, resource, signing a shader nástroje).
- WiX 3.x i novější WiX CLI, včetně manuálně nainstalovaných verzí pod
  `C:\Tools\WiXToolset`;
- .NET Framework SDK nástroje (`ildasm`, `gacutil`, `resgen`, `sn` a další),
  AMD Ryzen Master CLI, 7-Zip z registrované instalace a Git Bash (`bash`/`sh`);
- `dotnet` a Git CLI z jejich standardních instalačních umístění.

Stávající uživatelské položky `PATH` zachovává. Do systémového `PATH` ani do registru aplikací nezasahuje. Skript nic nestahuje ani neinstaluje; pouze registruje existující nástroje.
U Visual Studio toolchainu registrace zpřístupní binárky přes `PATH`; pro
kompilaci, která vyžaduje `INCLUDE`/`LIB`, použij Developer PowerShell nebo
`VsDevCmd.bat`, protože samotný `PATH` tyto SDK proměnné nenastavuje.
Git `usr\bin` se globálně neregistruje schválně, protože obsahuje Unixové
kompatibilní příkazy, které by mohly zastínit stejnojmenné Windows nástroje;
Git Bash si tento interní adresář nastaví samo při spuštění.

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
