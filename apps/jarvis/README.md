# Jarvis

Jarvis je osobní lokální agent pro chat, práci se soubory ve workspace, lokální LLM providery a bezpečně potvrzované nástroje. Je určený pro běžné používání na vlastním počítači: psaní, programování, výzkum, plánování, dokumenty, troubleshooting i další projektovou práci bez nutnosti cloudové služby.

## Stažení

* Verze: `0.1.360`
* Setup: [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/jarvis/JarvisSetup.exe)
* SHA-256: `1EEC6FA9A8B5A9F612F47C4CAE59B90378B28288668D7CFA2AF6B603FAFEA843`
* Update manifest pro aplikaci: [update.json](update.json)

## Co Aplikace Dělá

* běží jako WDUi Windows aplikace
* drží UI ve vlastním hlavním vlákně, aby šlo psát a ovládat appku i při práci modelu
* posílá LLM, workspace, internetové a nástrojové úlohy do worker fronty
* umí lokální historii konverzací
* umí read-only scan, tree, search a čtení souborů ve zvoleném workspace
* umí explicitně připojovat project memory a webové nebo lokální textové zdroje
* umí potvrzené webové hledání, URL fetch, download se SHA-256, veřejné GitHub čtení a package metadata
* umí potvrzené čtení jednoho soukromého GitHub textového souboru přes uživatelovo gh.exe přihlášení
* v režimu Plný přístup umí po potvrzení spouštět PowerShell, Command Prompt, Git Bash a WSL v aktivním workspace a ukládat výstup jako zdroj pro další práci
* umí read-only hardware probe a model-fit katalog: RAM, CPU vlákna, GPU/VRAM a odhad, které lokálně instalované modelové třídy dávají na daném PC smysl
* má první model manager: přes lokální Ollama provider umí po potvrzení stáhnout/smazat model a nastavovat aktivní profily `default`, `small`, `coder`, `reasoning`
* má update badge v titulku okna a veřejný ADPU update kanál

## Co Aplikace Nedělá

Jarvis není oficiální OpenAI ani Codex produkt. Neobsahuje cloudovou analytiku, nesmí bez potvrzení posílat soukromé workspace soubory na internet a nemá shell zapnutý ve výchozím profilu; PowerShell, Command Prompt, Git Bash a WSL jsou dostupné až v režimu `Plný přístup` po potvrzení konkrétního spuštění. Veřejný internet je ve výchozím profilu Standard povolený, aby šlo hledat, číst veřejné URL a kontrolovat aktualizace bez skrytého nastavování. Uživatel ho může vypnout nebo přepnout do přísnějšího profilu v Nastavení; konkrétní síťové akce, které sahají na lokální/soukromý obsah, dál vyžadují potvrzení.

Jarvis nedistribuuje, nebalí, nestahuje ani neinstaluje LLM/model weights. Modely si uživatel instaluje, licencuje, aktualizuje a maže samostatně v Ollama, LM Studio nebo jiném OpenAI-compatible provideru. Jarvis pouze ukládá názvy providerů/profilů a posílá požadavky na uživatelem nastavený endpoint.

Model-fit katalog je poradní vrstva, ne obchod s modely. Nároky se liší podle kvantizace, délky kontextu, backendu a GPU offloadu.

Automatické stahování/mazání modelů je provider-backed: Jarvis sám modely nehostuje ani nedistribuuje, jen po potvrzení požádá lokální Ollama endpoint o `pull` nebo `delete`. U LM Studio zatím modely vybírá a používá, ale instalace a mazání zůstává v LM Studio GUI, dokud nebude stabilní API.

## Instalace

1. Stáhni [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/jarvis/JarvisSetup.exe).
2. Spusť setup.
3. Vyber instalační složku, pokud nechceš výchozí `C:\Program Files\Jarvis`.
4. Dokonči instalaci.

Po instalaci se aplikace zaregistruje ve Windows jako běžná aplikace, přidá Start Menu zástupce pod `Jeniksoft` a jde odinstalovat přes Windows Nastavení > Aplikace > Nainstalované aplikace.

## Aktualizace

Jarvis umí zkontrolovat veřejný [update.json](update.json) manifest. Kontrola a instalace aktualizace jsou dostupné v okně přes Nastavení nebo update badge v titulku; příkazy `/update-check --confirm` a `/update-install --confirm` zůstávají jen pokročilá kompatibilní cesta. Instalace stáhne setup z veřejného `setup_url`, ověří SHA-256 a spustí tichou instalaci.

## Poznámka K Antiviru

Setup je běžný Windows EXE soubor s vloženým MSI backendem. Pokud ještě nemá dostatečnou reputaci nebo podpis, Windows SmartScreen nebo antivirus můžou zobrazit varování nebo ho testovat déle. Pro kontrolu integrity porovnej SHA-256 se souborem [checksums/SHA256SUMS.txt](../../checksums/SHA256SUMS.txt).
