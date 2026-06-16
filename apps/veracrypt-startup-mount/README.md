# Codex VeraCrypt Startup Mount

Malá Windows utilita pro lokální mount VeraCrypt svazku po přihlášení uživatele.

## Stažení

* Verze: `1.0.6`
* Setup: [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe)
* SHA-256: `D2DE05B15C6491000E43C6D03BB30C35984676E6CF1DFAB5BA03EBAECA006C5C`
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

Od verze `1.0.6` VeraCrypt Startup Mount přebírá current durable baseline: jazyk se přepíná živě bez nového otevření okna, poloha a velikost manageru se ukládají a vracejí při dalším otevření a build si generuje lokalizační header podle CPM Windows language rules. Build pipeline také nově bumpuje `VERSION` až po úspěšném exportu setupu místo hned na začátku běhu.

Od verze `1.0.4` má manager přímo v UI kontrolu aktualizací: bitmapovou stavovou ikonu, tooltip akce pro ruční kontrolu a instalaci a tichý update tok se znovu-načtením manifestu, ověřením `SHA-256` a automatickým znovuotevřením appky po setupu. Setup zároveň nově instaluje i update assety a před přeinstalací bezpečně ukončí běžící manager.

Od verze `1.0.2` má appka i společný durable WDUi headless probe `VeraCryptStartupMount.exe --ensure-config` a reusable `smoke_test.ps1`. Neinteraktivní smoke kontrola tak ověřuje export setupu, zapsání normalizovaného configu i stávající self-test appky a setupu bez instalace.

Od verze `1.0.1` má appka srovnaný veřejný ADPU manifestový základ: build používá jednu runtime verzi z `VERSION`, setup se publikuje do ADPU, Start Menu se uklízí pod `Jeniksoft` a v menu `O aplikaci` lze otevřít historii změn z veřejného `update.json`.
