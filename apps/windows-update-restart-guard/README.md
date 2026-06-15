# Windows Update Restart Guard

Windows Update Restart Guard je malá Windows utilita, která pomáhá zabránit běžným plánovaným restartům po Windows Update, když je aplikace spuštěná a ochrana je zapnutá.

## Stažení

* Verze: `1.0.50`
* Setup: [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe)
* SHA-256: `8EF7F215C3066D16DAAB210838BB336435C4B87A73C04FB07DEE5DAC16A96BF3`
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

Od verze `1.0.41` WDUi drží text a interaktivní obsah uvnitř bezpečné vnitřní oblasti aktivního tvaru surface. Pomáhá to hlavně u skinů se zkosenými, hexagonálními, kapslovými a dalšími výraznými tvary, kde už obsah neleze do šikmých nebo odříznutých rohů.

Od verze `1.0.42` WDUi používá safe oblast i pro layout vnitřních controlů. Panely a karty tak vrací skutečný layout viewport, anchor výpočet respektuje přirozená minima controlů a nastavení Restart Guardu přepočítává formulářové prvky podle použitelných oblastí karet.

Od verze `1.0.43` WDUi přidává shape-safe layout bands: neobdélníkové surfaces vrací stabilní vodorovné bezpečné pásy přes `contentLayoutRects()`. Restart Guard je používá pro skupiny controlů v nastavení, takže výrazné zkosené skiny lépe drží tabulky a formuláře uvnitř použitelného prostoru.

Od verze `1.0.44` používá WDUi stejný shape-safe princip i pro custom chrome. Ikona aplikace, text titulku a ovládací tlačítka titulku se počítají z bezpečného řádku aktivního titlebar tvaru, takže šikmé skiny jako Ultraviolet Rift nestrkají ikonu do zkoseného okraje.

Od verze `1.0.45` používají shape-safe řádek i vestavěné texty karet. Tím se opravuje explanatory text u panelu Restartovací okna ve skinu Ultraviolet Rift, který předtím mohl ležet v odříznuté části šikmé karty.

Od verze `1.0.47` jsou restartovací okna v nastavení skutečné děti panelu `Restartovací okna`, ne overlay položený přes kartu. WDUi přidává body layout API pro karty, takže tabulka, editor dne a časové vstupy respektují bezpečné tělo panelu i u výrazně zkosených skinů.

Od verze `1.0.48` používají WDUi popup akční tlačítka a popup close tlačítko bezpečné row spany aktivního surface. Tlačítka v malých dialozích, například `Zavřít` v dialogu kontroly aktualizací, se tak neposouvají do useknutých rohů u cut/slanted skinů.

Od verze `1.0.49` má WDUi obecnou surface geometry vrstvu oddělenou od kreslení. Skin může použít fallback tvar, alpha kanál bitmapy nebo samostatnou masku pro hit-test a layout pásy, a současně nastavit bezpečné insety zvlášť pro text, child layout, header, akční řádek, scrollbar a klikací oblast.

Od verze `1.0.50` WDUi opravuje resize/restore tok custom oken: minimalizace už nepřepočítává root layout na nulovou plochu, app-level relayout po `WM_SIZE` běží až nad aktuální velikostí klienta a ručně přepočítané ovládací prvky v Restart Guardu používají runtime bounds bez přepisování návrhové anchor reference. Tím se opravuje stav, kdy šlo okno zvětšovat, ale po zvětšení už nešlo zmenšit, a po minimalizaci/restore mizely spodní prvky nastavení.

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
