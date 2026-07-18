# Jarvis Beta

Jarvis Beta je veřejný, dobrovolný testovací kanál před vydáním Jarvise 1.0.0. Slouží pro ověření UI/UX, chování na různém hardwaru a srozumitelnosti pracovních toků dřív, než se změny dostanou do stabilního kanálu.

## Důležité bezpečnostní upozornění

Beta instalátor zatím není podepsán veřejným Authenticode certifikátem. Stahuj jej pouze z tohoto repozitáře, před spuštěním porovnej SHA-256 a testuj ho na vlastním počítači nebo v prostředí, kde máš oprávnění. Beta není automaticky nabízena uživatelům stabilního kanálu Jarvis.

## Stažení

* Verze: `0.9.0`
* Setup: [JarvisSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/jarvis-beta/JarvisSetup.exe)
* SHA-256: `75227EC641D9A11B018C94D49FC8D275CF36587E08CACB723AEAB4FF7EB10306`
* Beta update manifest: [update.json](update.json)

## Jak testovat

1. Nainstaluj beta setup a spusť Jarvis.
2. Vyzkoušej běžný chat, výběr projektu, Project Intake, TabView pro soubory/GitHub/náhled a změnu velikosti okenních panelů.
3. Při problému přilož verzi Jarvise, Windows verzi, GPU/CPU/RAM, stručný postup reprodukce a snímek obrazovky nebo relevantní lokální log.
4. Pošli feedback přes [nový GitHub issue](https://github.com/jeniksoft/app-downloads/issues/new?title=Jarvis%20Beta%20feedback) včetně toho, zda problém blokuje práci, nebo jde jen o UX detail.

## Změny beta 0.9.0

* UI/UX testovací vydání se souvislým TabView panelem pro soubory projektu, GitHub a náhled souboru.
* Oprava překreslení náhledu souboru po otevření z panelu souborů.
* Odolnější cache Project Intake a ověřený lokální vision scénář pro červený čtverec a modrý kruh.
