# Windows Update Restart Guard

Windows Update Restart Guard je malá Windows utilita, která pomáhá zabránit běžným plánovaným restartům po Windows Update, když je aplikace spuštěná a ochrana je zapnutá.

## Stažení

* Verze: `1.0.77`
* Setup: [WindowsUpdateRestartGuardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/windows-update-restart-guard/WindowsUpdateRestartGuardSetup.exe)
* SHA-256: `F0788CBE512A2FD5C43A44209BFD79B53CDA3325C48B7544CBF84AB0A8ED7194`
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

Od verze `1.0.77` se historie změn z `O aplikaci` otevírá v rolovatelném WDUi dialogu se scrollbarem. Delší changelog tak zůstává celý čitelný a neuteče mimo okno.

Od verze `1.0.76` je veřejný setup znovu přegenerovaný a publikovaný z aktuální CPM/WDUi baseline. Release záměrně nemění viditelné chování appky; srovnává veřejný setup export, checksum a manifest s aktuálním referenčním buildem po další normalizační vlně durable skeletonu.

Od verze `1.0.75` má appka i společný durable WDUi headless probe `WindowsUpdateRestartGuard.exe --ensure-config` a reusable `smoke_test.ps1`. Neinteraktivní smoke vrstva tak ověřuje build výstup, export setupu a normalizovaný zápis configu bez otevření nastavení; vedle toho zůstává dostupný i starší lifecycle probe `--exit-after-ms`.

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

Od verze `1.0.53` je Restart Guard srovnaný s aktuální durable C++/WDUi šablonou pro paměť stavu UI. Nastavení si ukládá poslední normální nebo maximalizovanou polohu okna a stav seznamu restartovacích oken včetně scrollu. Uložený stav je záměrně očištěný: neobnovuje minimalizaci ani přechodné hidden/disabled stavy, aby se okno po startu nevrátilo do nepoužitelného stavu.

Od verze `1.0.54` WDUi okna zachytí samotnou klávesu PrintScreen jako fallback pro Windows screen snipping přes `ms-screenclip:`. To odpovídá toku `Win+Shift+S` a řeší stav, kdy screenshot klávesa nad custom WDUi oknem nepůsobila. Kombinace jako `Alt+PrintScreen` zůstávají ponechané Windows nebo appce.

Od verze `1.0.55` WDUi kreslí obrysy vector surfaces dovnitř bounds místo na exkluzivní pravý/spodní okraj GDI kreslení. Výplň zůstává přes celou plochu, ale pravá a spodní linka se už u custom nebo zkosených skinů neztratí oříznutím na hraně okna.

Od verze `1.0.56` WDUi ukládá normální pozici top-level okna podle skutečné screen pozice. Restart Guard zároveň ukládá placement po dokončení přesunu nebo změny velikosti okna, takže nastavení otevřené z tray se po zavření a znovuotevření vrací na místo, kam ho uživatel přesunul.

Od verze `1.0.58` používají WDUi tabulky, combo/dropdown popupy a menu popupy bezpečný vodorovný pás pro každý řádek. Texty, řádkové výplně, separátory a scrollbary tak zůstávají uvnitř zkosených nebo cut skinů. Tabulka restartovacích oken v Restart Guardu zároveň automaticky přizpůsobuje sloupce obsahu, dovoluje ruční resize hranic sloupců v hlavičce a změněné šířky ukládá do UI stavu.

Od verze `1.0.59` používají WDUi comboboxy a další dropdowny kompaktní vložený scroll rail místo plného výrazného scrollbaru. Výběr skinů a podobné seznamy tak zůstávají čitelné i u herních nebo zkosených skinů, ale scrollbar vizuálně nepřebíjí samotné položky.

Od verze `1.0.61` počítá WDUi progress bar track i procentní text z bezpečné oblasti aktivního tvaru. Update dialogy tak nedávají procenta do odříznuté části controlu u výrazně zkosených skinů. Stejný princip je doplněný i pro tab strip položky a popup action/close tlačítka.

Od verze `1.0.62` používají další stávající WDUi controly stejný shape-safe princip jako dropdowny a tabulky. Datumová pole, kalendáře, menu, taby, rich/selectable text bloky, popup texty a tooltip akční tlačítka počítají text a vnitřní obsah z bezpečné oblasti aktivního surface, takže ani výrazně zkosené skiny neposílají text do odříznutých rohů. Restart Guard je proti této WDUi vrstvě znovu přebuildovaný, včetně update dialogů.

Od verze `1.0.63` má WDUi obecné edge-safe layout lanes pro prvky ukotvené k okraji. Dropdown scrollbar v Restart Guardu se tak bere z pravého bezpečného pruhu aktivního dropdown surface a neleze přes šikmé nebo odříznuté okraje. Stejný princip je zapsaný jako pravidlo pro scrollbary, badge, update glyphy, toolbary, overlay tlačítka, splittery, resize gripy a budoucí edge controly.

Od verze `1.0.64` používá WDUi pro edge-follow prvky vynucený 1px scanline layout. Dropdown scrollbar v Restart Guardu se kreslí, hit-testuje i táhne podle segmentů pravé hrany aktivního dropdown surface, takže se u výrazných šikmých nebo cut skinů drží stejného marginu od hrany místo jednoho hrubého obdélníku.

Od verze `1.0.65` je opravený kompaktní scrollbar v dropdownu: thumb zůstává úzký, ale track/rám je znovu širší a čitelně ho ohraničuje. WDUi navíc kreslí segmentované surfaces jako jeden souvislý materiál oříznutý contour regionem, takže se gradienty, bitmapy, obrysy a noise nerozbijí na izolované 1px proužky. Contour layout je nově společná vlastnost základního `Controlu`, kterou mohou používat i další současné a budoucí prvky.

Od verze `1.0.66` používá WDUi pro segmentované contour prvky nový bitmap-shift postup: control se nejdřív vykreslí rovně do offscreen bitmapy bez deformace a potom se 1px řádky nebo sloupce posunou do contour lanes. Dropdown scrollbary tak drží stejný margin od šikmé nebo cut hrany bez grafických zlomů, smrštěných rámů a rozbitých borderů.

Od verze `1.0.68` se stejný bitmap-shift postup používá pro celý složený control najednou. WDUi nejdřív vykreslí kompletní prvek včetně okrajů, výplně, thumbu/handle, glyphů a overlayů do rovné offscreen bitmapy a teprve hotový obraz posune po 1px řádcích nebo sloupcích do contour lanes. Edge prvky zároveň berou zdroj z odpovídající strany rovné bitmapy, ne ze středu, takže dropdown scrollbar už nedeformuje rail a thumb odděleně a rám zůstává širší než thumb i u šikmých a cut skinů.

Od verze `1.0.69` volí WDUi při bitmap-shift remapu zdrojovou stranu pro každý 1px pás podle menšího aktuálního marginu. Pokud je řádek blíž levé hraně, použije levou část rovné bitmapy; pokud je blíž pravé hraně, použije pravou část; při shodě zůstává střed. U šikmých a cut skinů tak dropdown scrollbar lépe drží stejný vizuální odstup od bližší hrany.

Od verze `1.0.70` se při zavření nastavení z custom chrome X nebo z menu pro zavření do tray nejdřív uloží aktuální UI state a až potom se okno zavře. Nastavení otevřené z tray se tak po přesunutí a zavření vrací na nové místo. Stejný request-close pattern je doplněný i do durable C++/WDUi šablony.

Od verze `1.0.71` se uložený UI state po úspěšném zápisu do `config.ini` propíše i do běžící runtime konfigurace tray procesu. To opravuje stav, kdy se pozice sice uložila na disk, ale další otevření nastavení ve stejném běžícím procesu použilo starou kopii `g_config`.

Od verze `1.0.74` jde z `O aplikaci` otevřít plná historie změn z veřejného `update.json` manifestu. Když manifest ještě není v paměti, appka si ho pro tuto akci zkusí čerstvě načíst sama a pak zobrazí kompletní changelog nebo srozumitelnou chybu.

## Ovládání

Po spuštění najdeš aplikaci v oznamovací oblasti Windows. Tray popup nabízí:

* zapnout nebo vypnout blokování plánovaných restartů
* otevřít Windows Update
* zapnout nebo vypnout spouštění s Windows
* vytvořit nebo odebrat zástupce na ploše
* otevřít nastavení, logy, nápovědu a informace o aplikaci

V nastavení můžeš upravit profily chování a restartovací okna. Například pátek `13:00-17:00` znamená, že v pátek mezi 13:00 a 17:00 je restart povolený a ochrana se dočasně neuplatní.

## Aktualizace

Aplikace umí zkontrolovat veřejný [update.json](update.json) manifest. Kontroluje tiše po startu a potom zhruba každou hodinu. V nastavení je stavová bitmapová akce: běžně spustí ruční kontrolu aktualizací, a když je dostupná novější verze, změní se na instalační update ikonu; po kliknutí stáhne setup, ověří SHA-256, spustí tichou instalaci a znovu otevře aplikaci. Manifest zároveň obsahuje historii změn, takže aplikace v update tooltipu a dialogu ukáže i změny z verzí, které uživatel přeskočil, a stejné release notes jsou dostupné i ručně přes `O aplikaci`.

## Odinstalace

Použij Windows Nastavení > Aplikace > Nainstalované aplikace > Windows Update Restart Guard > Odinstalovat.

## Poznámka K Antiviru

Setup je běžný Windows EXE soubor. Verze `1.0.29` až `1.0.35` vznikly jako reakce na false-positive behavior-shield test a následné dotažení MSI instalace: aplikace byla čistá, ale starší instalační tok mohl bezpečnostním nástrojům připomínat dropper/persistence vzor. Setup proto nepoužívá skrytý shell cleanup ani shell handoff pro update setup a od verze `1.0.32` používá pro instalaci standardní WiX/MSI backend. Pokud EXE ještě nemá dostatečnou reputaci nebo podpis, některé bezpečnostní nástroje ho můžou kontrolovat déle.
