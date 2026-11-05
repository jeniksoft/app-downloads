# Codex Task Board

Codex Task Board is a Windows desktop app for viewing tasks, reports, suggestions, and roadmap information for projects the user selects.

## Package

* Setup: [CodexTaskBoardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/codex-task-board/CodexTaskBoardSetup.exe)
* Verze: `1.1.202`
* SHA-256: `789C28C1E4922E5CCA1B06B094FC71A2D8E35CA2A2FF5872F701631C15D04B94`

## Project data

The Setup contains the application, not project task data or a copy of a project repository. Task Board reads project information from GitHub. Viewing a project requires the GitHub access allowed by that project's repository settings and the user's sign-in.

Downloading this installer does not make private project data public. Public access to the installer and access to project data are separate.

## Změny verze 1.1.202

Oprava Jarvis roadmapy: kanonické stavy MCH, bezpečný read-back UI geometrie a opravy zobrazení roadmapy.

## Změny verze 1.0.0

Opraveno zobrazování částečně implementovaných a dosud neověřených řezů roadmapy; Task Board nyní neoznačí otevřené ověření jako Ověřeno.

## Změny verze 1.1.142

Opraveno publikovani aktualizacniho manifestu Task Boardu: ADPR i ADPU nyni dostanou stejny overeny Setup, verzi, historii a SHA-256; tim se obnovuje kontrola aktualizaci v aplikaci.

## Změny verze 1.1.145

Nahrazeny všechny staré hexagonální update ikony novou ikonovou rodinou; kontrola i dostupná aktualizace používají nové stavové assety ve společném 50px cíli.

## Změny verze 1.1.146

Sjednoceny viditelne okraje vsech novych update ikon; static i hover stavy pouzivaji stejny alpha frame 128px canvas.

## Změny verze 1.1.149

Opal Silk: obdélníkové kotvy a široká vnitřní kapsle; přidána regresní geometrická brána.

## Změny verze 1.1.150

Normalizace strukturálních kotev WDUi napříč všemi skiny; vnitřní kapsle zůstávají skinové.

## Změny verze 1.1.151

Oprava blikajících tooltipů a připnutí bez zablokování akce; strukturální kotvy WDUi napříč skiny.

## Změny verze 1.1.152

Oprava skinů: zachování autorských kontur panelů při obdélníkové layoutové kotvě; líné náhledy skinů jen pro aktuální a viditelné položky.

## Změny verze 1.1.153

Adaptivní kontury: vysoké úzké vnitřní plochy zachovají kapsli a oříznou se podle rodičovského tvaru; široké panely zůstávají obdélníkovými layoutovými kotvami.

## Změny verze 1.1.154

Oprava konturového layoutu: levé panely zachovají obdélníkové rozměry a pravý inset, rodičovská kontura se projeví schodovitým ořezem po řádcích.

## Změny verze 1.1.155

Oprava konturových panelů: zachování levého i pravého obdélníkového odsazení s přesným schodovitým ořezem rodičovské kontury.

## Změny verze 1.1.156

Cilena oprava stability skinu Starlance Rift a orezani ovladacich prvku

## Změny verze 1.1.157

Oprava obnovy okna po minimalizaci a celoplošný repaint bez hoveru; Starlance Rift regresní kontrola.

## Změny verze 1.1.188

Přidán přehled běhů GitHub Actions a self-hosted runnerů.

## Změny verze 1.1.194

Tooltip jobů nyní začíná přehledem commitu: zobrazuje zprávu s kontextem, změněné soubory a počty řádků.

## Změny verze 1.1.199

Monitor běhů GitHub Actions nyní u každého jobu zobrazuje report jeho commitu: účel a důvod z připojeného pull requestu nebo commit message, změněné soubory a počty přidaných i odebraných řádků. Pokud důvod nelze ověřit, tooltip to řekne a nic si nevymýšlí.

## Změny verze 1.1.200

Pravým kliknutím na řádek jobu otevřete nabídku s kopírovatelným souhrnem do chatu. Souhrn obsahuje přímý odkaz na job, Run ID a Job ID, workflow, stav, větev a zprávu commitu.

