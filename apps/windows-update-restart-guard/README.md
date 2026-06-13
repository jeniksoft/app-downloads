# Windows Update Restart Guard

Windows Update Restart Guard je malá Windows utilita, která pomáhá zabránit běžným plánovaným restartům po Windows Update, když je aplikace spuštěná a ochrana je zapnutá.

## Stažení

* Verze: `1.0.27`
* Setup: [WindowsUpdateRestartGuardSetup.exe](WindowsUpdateRestartGuardSetup.exe)
* SHA-256: `06848C3B01F4627C89F8B7DA2C81FAED87FF9328C90599F40FB16B775521B866`
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

1. Stáhni [WindowsUpdateRestartGuardSetup.exe](WindowsUpdateRestartGuardSetup.exe).
2. Spusť setup.
3. Vyber instalační složku, pokud nechceš výchozí `C:\Program Files\WindowsUpdateRestartGuard`.
4. Dokonči instalaci.

Po instalaci se aplikace otevře do nastavení a zároveň se zaregistruje ve Windows jako běžná aplikace.

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

Setup je běžný Windows EXE soubor. Pokud ještě nemá dostatečnou reputaci nebo podpis, některé bezpečnostní nástroje ho můžou kontrolovat déle nebo zobrazit varování.
