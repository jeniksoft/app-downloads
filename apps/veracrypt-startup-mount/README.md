# Codex VeraCrypt Startup Mount

Malá Windows tray utilita pro lokální mount jednoho nebo více VeraCrypt svazků po přihlášení uživatele.

## Stažení

* Verze: `1.0.14`
* Setup: [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe)
* SHA-256: `CB19C498076C681B80A0CF3E8D61DDB37F3B476B346B63A8998841FC97FADE0D`
* Update manifest: [update.json](update.json)

## Co Aplikace Dělá

* spouští nativní C++/Win32 + WDUi manager
* běží jako tray appka: zavření okna schová manager do oznamovací oblasti
* levý klik na tray ikonu otevře manager, pravý klik ukáže WDUi akce
* umí více mapování VeraCrypt svazků na písmena disků
* v manageru ukazuje, co je na co namapované a zda je písmeno disku aktuálně mountnuté
* ukládá heslo jen lokálně přes Windows DPAPI pro aktuálního uživatele
* umí zapnout mount po přihlášení
* umí volitelný zástupce na ploše
* jde normálně odinstalovat přes Windows Nastavení > Aplikace > Nainstalované aplikace

## Co Aplikace Nedělá

Není to plný správce VeraCrypt kontejnerů obecně. Je to pomocná utilita pro lokální startup mount workflow s více předem nastavenými mapováními.

## Instalace

1. Stáhni [VeraCryptStartupMountSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/veracrypt-startup-mount/VeraCryptStartupMountSetup.exe).
2. Spusť setup.
3. Vyber instalační složku, pokud nechceš výchozí Program Files cestu.
4. Dokonči instalaci a v manageru nastav mapování svazků, písmena disků, VeraCrypt cestu a heslo.

Po instalaci se vytvoří Start Menu záznam pod `Jeniksoft` a aplikace se zaregistruje jako běžná Windows aplikace.

## Poznámka K Heslu

Heslo není součástí setupu, gitu ani veřejného manifestu. Ukládá se až lokálně v manageru do DPAPI CurrentUser úložiště na konkrétním PC.

## Historie Změn

Od verze `1.0.12` je manager normalizovaný jako tray appka. Zavření okna ho schová do oznamovací oblasti, levý klik ho vrátí, pravý klik otevře WDUi akce a manager nově podporuje více VeraCrypt mapování s živým přehledem mountnuto / není mountnuto.

Od verze `1.0.7` se historie změn z `O aplikaci` otevírá v rolovatelném dialogu s vlastním scrollbarem. Delší changelog tak zůstává celý čitelný a nepřetéká mimo okno.

Od verze `1.0.6` VeraCrypt Startup Mount přebírá current durable baseline: jazyk se přepíná živě bez nového otevření okna, poloha a velikost manageru se ukládají a vracejí při dalším otevření a build si generuje lokalizační header podle CPM Windows language rules. Build pipeline také nově bumpuje `VERSION` až po úspěšném exportu setupu místo hned na začátku běhu.

Od verze `1.0.4` má manager přímo v UI kontrolu aktualizací: bitmapovou stavovou ikonu, tooltip akce pro ruční kontrolu a instalaci a tichý update tok se znovu-načtením manifestu, ověřením `SHA-256` a automatickým znovuotevřením appky po setupu. Setup zároveň nově instaluje i update assety a před přeinstalací bezpečně ukončí běžící manager.

Od verze `1.0.2` má appka i společný durable WDUi headless probe `VeraCryptStartupMount.exe --ensure-config` a reusable `smoke_test.ps1`. Neinteraktivní smoke kontrola tak ověřuje export setupu, zapsání normalizovaného configu i stávající self-test appky a setupu bez instalace.

Od verze `1.0.1` má appka srovnaný veřejný ADPU manifestový základ: build používá jednu runtime verzi z `VERSION`, setup se publikuje do ADPU, Start Menu se uklízí pod `Jeniksoft` a v menu `O aplikaci` lze otevřít historii změn z veřejného `update.json`.
