# Jarvis

Jarvis je lokální fallback host pro práci s uživatelem nastavenými LLM providery, soubory ve workspace a bezpečně potvrzovanými nástroji. Program vzniká jako nouzová náhrada za cloudový Codex/Jarvis styl práce, když není dostupný internet, dojdou limity, nebo je vhodnější lokální model.

## Stažení

* Verze: `0.1.135`
* Setup: [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/personal-codex-fallback-host/JarvisSetup.exe)
* SHA-256: `DEDCBB28ECCB4BD2450084C63F78A55D89DB0325357747EACACD351777BBE6D1`
* Update manifest pro aplikaci: [update.json](update.json)

## Co Aplikace Dělá

* běží jako WDUi Windows aplikace
* drží UI ve vlastním hlavním vlákně, aby šlo psát a ovládat appku i při práci modelu
* posílá LLM, workspace, internetové a nástrojové úlohy do worker fronty
* umí lokální historii konverzací
* umí read-only scan, tree, search a čtení souborů ve zvoleném workspace
* umí explicitně připojovat project memory a webové nebo lokální textové zdroje
* umí potvrzené webové hledání, URL fetch, download se SHA-256, veřejné GitHub čtení a package metadata
* umí potvrzené čtení jednoho soukromého GitHub textového souboru přes uživatelovo `gh.exe` přihlášení
* umí read-only hardware probe a model-fit katalog: RAM, CPU vlákna, GPU/VRAM a odhad, které lokálně instalované modelové třídy dávají na daném PC smysl
* má první model manager: přes lokální Ollama provider umí po potvrzení stáhnout/smazat model a nastavovat aktivní profily `default`, `small`, `coder`, `reasoning`
* má update badge v titulku okna a veřejný ADPU update kanál

## Co Aplikace Nedělá

Jarvis není oficiální OpenAI ani Codex produkt. Neobsahuje cloudovou analytiku, nesmí bez potvrzení posílat soukromé workspace soubory na internet a nemá obecný neomezený shell. Síťové akce jsou vypnuté, dokud je uživatel výslovně nezapne přes internet režim, a konkrétní síťové příkazy i potom vyžadují `--confirm`.

Jarvis nedistribuuje, nebalí, nestahuje ani neinstaluje LLM/model weights. Modely si uživatel instaluje, licencuje, aktualizuje a maže samostatně v Ollama, LM Studio nebo jiném OpenAI-compatible provideru. Jarvis pouze ukládá názvy providerů/profilů a posílá požadavky na uživatelem nastavený endpoint.

Model-fit katalog je poradní vrstva, ne obchod s modely. Nároky se liší podle kvantizace, délky kontextu, backendu a GPU offloadu.

Automatické stahování/mazání modelů je provider-backed: Jarvis sám modely nehostuje ani nedistribuuje, jen po potvrzení požádá lokální Ollama endpoint o `pull` nebo `delete`. U LM Studio zatím modely vybírá a používá, ale instalace a mazání zůstává v LM Studio GUI, dokud nebude stabilní API.

## Instalace

1. Stáhni [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/personal-codex-fallback-host/JarvisSetup.exe).
2. Spusť setup.
3. Vyber instalační složku, pokud nechceš výchozí `C:\Program Files\Jarvis`.
4. Dokonči instalaci.

Po instalaci se aplikace zaregistruje ve Windows jako běžná aplikace, přidá Start Menu zástupce pod `Jeniksoft` a jde odinstalovat přes Windows Nastavení > Aplikace > Nainstalované aplikace.

## Aktualizace

Jarvis umí zkontrolovat veřejný [update.json](update.json) manifest. Po zapnutí internet režimu může příkaz `/update-check --confirm` porovnat lokální verzi s ADPU a `/update-install --confirm` stáhne setup z veřejného `setup_url`, ověří SHA-256 a spustí tichou instalaci.

## Poznámka K Antiviru

Setup je běžný Windows EXE soubor s vloženým MSI backendem. Pokud ještě nemá dostatečnou reputaci nebo podpis, Windows SmartScreen nebo antivirus můžou zobrazit varování nebo ho testovat déle. Pro kontrolu integrity porovnej SHA-256 se souborem [checksums/SHA256SUMS.txt](../../checksums/SHA256SUMS.txt).
