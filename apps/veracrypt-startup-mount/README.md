# Codex VeraCrypt Startup Mount

Malá Windows utilita pro lokální mount VeraCrypt svazku po přihlášení uživatele.

## Stažení

* Verze: `1.0.1`
* Setup: [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe)
* SHA-256: `920161538946DB7501D3B29DCE43DDCDA44117CC7BB5028EDDF92D9CC92E8255`
* Update manifest: [update.json](update.json)

## Co Aplikace Dělá

* spouští nativní C++/Win32 + WDUi manager
* ukládá heslo jen lokálně přes Windows DPAPI pro aktuálního uživatele
* umí zapnout mount po přihlášení
* umí volitelný zástupce na ploše
* jde normálně odinstalovat přes Windows Nastavení > Aplikace > Nainstalované aplikace

## Co Aplikace Nedělá

Není to správce VeraCrypt kontejnerů obecně. Je to jednoduchá pomocná utilita pro jeden lokální startup mount workflow.

## Instalace

1. Stáhni [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe).
2. Spusť setup.
3. Vyber instalační složku, pokud nechceš výchozí Program Files cestu.
4. Dokonči instalaci a v manageru nastav svazek, písmeno disku, VeraCrypt cestu a heslo.

Po instalaci se vytvoří Start Menu záznam pod `Jeniksoft` a aplikace se zaregistruje jako běžná Windows aplikace.

## Poznámka K Heslu

Heslo není součástí setupu, gitu ani veřejného manifestu. Ukládá se až lokálně v manageru do DPAPI CurrentUser úložiště na konkrétním PC.

## Historie Změn

Od verze `1.0.1` má appka srovnaný veřejný ADPU manifestový základ: build používá jednu runtime verzi z `VERSION`, setup se publikuje do ADPU, Start Menu se uklízí pod `Jeniksoft` a v menu `O aplikaci` lze otevřít historii změn z veřejného `update.json`.
