# Python a PyTorch – registrace vývojářských nástrojů

`register-development-tools.ps1` idempotentně objeví běžná umístění vývojářských nástrojů ve Windows a přidá je do uživatelského `PATH` bez administrátorských práv.

Registruje zejména:

- Python Launcher, všechny nalezené instalace Pythonu, jejich `Scripts` a Python virtualenvy;
- PyTorch/DirectML virtualenv, pokud existuje;
- Gradle, JDK, Ollama a jeho pomocné binárky;
- WinGet Links, npm, Cargo, `.NET tools`, Scoop a Node.js;
- Android SDK (`platform-tools`, emulator, qemu, command-line tools a build-tools).

Stávající uživatelské položky `PATH` zachovává. Do systémového `PATH` ani do registru aplikací nezasahuje. Skript nic nestahuje ani neinstaluje; pouze registruje existující nástroje.

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
