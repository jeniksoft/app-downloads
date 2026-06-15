# Windows Update Restart Guard

Windows Update Restart Guard je malá Windows utilita, která pomáhá zabránit běžným plánovaným restartům po Windows Update, když je aplikace spuštěná a ochrana je zapnutá.

## Stažení

* Verze: `1.0.40`
* Setup: [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe)
* SHA-256: `D1FB2FEB24846CA329905D80D72AD825CE20A054089D3CE08A5F7338D6CCD584`
* Update manifest pro aplikaci: [update.json](update.json)

## Co Aplikace Dělá

* běží v oznamovací oblasti Windows
* blokuje běžné plánované restarty mimo povolená časová okna
* umožňuje nastavit profily restartovacích oken
* umí spouštění po přihlášení
* má volitelný zástupce na ploše
* jde odinstalovat přes Windows Nastavení > Aplikace > Nainstalované aplikace

## Co Aplikace Nedělá

Nezakazuje Windows Update. Neblokuje kritické vypnutí systému, výpadek napájení, pád systému, restart vyvolaný firmwarem nebo administrátorem vynucené vypnutí.

## Instalace

1. Stáhni [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe).
2. Spusť setup.
3. Vyber instalační složku, pokud nechceš výchozí `C:\Program Files\WindowsUpdateRestartGuard`.
4. Dokonči instalaci.

Po instalaci se aplikace otevře do nastavení a zároveň se zaregistruje ve Windows jako běžná aplikace.

Od verze `1.0.32` si setup nechává instalační práci dělat standardním Windows Installer backendem. WDUi okno zůstává stejné, ale za scénou se rozbalí vestavěný MSI balíček, spustí se `msiexec`, zapisují se verbose MSI logy a případná chyba ukáže konkrétní fázi, MSI kód a cestu k logu. MSI také používá standardní WiX zavírání běžící aplikace, takže odinstalace přes Windows Nastavení nezůstane jen na zamčeném EXE. Start Menu, Startup a Desktop zástupci jsou přímé neadvertised odkazy na nainstalovaný EXE. Od verze `1.0.35` používá MSI pro Start Menu standardní `ProgramMenuFolder` a vytváří záznam `Jeniksoft\Windows Update Restart Guard`, takže běžná jedna appka sedí pod vydavatelem a nevytváří zbytečnou vlastní app podsložku.

Od verze `1.0.38` je přibalený novější WDUi katalog skinů. Skin `Starlance` používá obdélníkové scrollbary místo kapslových a ostatní výchozí skiny mají výrazněji odlišené tvarové profily podle svého účelu.

Od verze `1.0.39` WDUi automaticky zobrazuje tooltip s plným textem u textových prvků, kde se viditelný obsah nevejde do dostupného místa. Platí to pro tlačítka, popisky, stavové prvky, checkboxy, comboboxy včetně dropdown položek, datumová pole, taby, menu root položky a tabulkové hlavičky/buňky.

Od verze `1.0.40` updater před samotným stažením setupu znovu načítá čerstvý update manifest. Když během čekání vyjde novější verze, nainstaluje novější setup a SHA-256; když manifest mezitím update zruší, dialog skončí jako aktuální místo selhání na starém manifestu.

## Ovládání

Po spuštění najdeš aplikaci v oznamovací oblasti Windows. Tray popup nabízí:

* zapnout nebo vypnout blokování plánovaných restartů
* otevřít Windows Update
* zapnout nebo vypnout spouštění s Windows
* vytvořit nebo odebrat zástupce na ploše
* otevřít nastavení, logy, nápovědu a informace o aplikaci

V nastavení můžeš upravit profily chování a restartovací okna. Například pátek `13:00-17:00` znamená, že v pátek mezi 13:00 a 17:00 je restart povolený a ochrana se dočasně neuplatní.

## Aktualizace

Aplikace umí zkontrolovat veřejný [update.json](update.json) manifest. Kontroluje tiše po startu a potom zhruba každou hodinu. V nastavení je stavová bitmapová akce: běžně spustí ruční kontrolu aktualizací, a když je dostupná novější verze, změní se na instalační update ikonu; po kliknutí stáhne setup, ověří SHA-256, spustí tichou instalaci a znovu otevře aplikaci. Manifest zároveň obsahuje historii změn, takže aplikace v update tooltipu a dialogu ukáže i změny z verzí, které uživatel přeskočil.

## Odinstalace

Použij Windows Nastavení > Aplikace > Nainstalované aplikace > Windows Update Restart Guard > Odinstalovat.

## Poznámka K Antiviru

Setup je běžný Windows EXE soubor. Verze `1.0.29` až `1.0.35` vznikly jako reakce na false-positive behavior-shield test a následné dotažení MSI instalace: aplikace byla čistá, ale starší instalační tok mohl bezpečnostním nástrojům připomínat dropper/persistence vzor. Setup proto nepoužívá skrytý shell cleanup ani shell handoff pro update setup a od verze `1.0.32` používá pro instalaci standardní WiX/MSI backend. Pokud EXE ještě nemá dostatečnou reputaci nebo podpis, některé bezpečnostní nástroje ho můžou kontrolovat déle.
