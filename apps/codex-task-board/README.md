# Codex Task Board

Codex Task Board is a Windows desktop app for viewing tasks, reports, suggestions, and roadmap information for projects the user selects.

## Package

* Setup: [CodexTaskBoardSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/codex-task-board/CodexTaskBoardSetup.exe)
* Verze: `1.1.142`
* SHA-256: `9009D5FFEACDB18355496739CC6AF00BCD999A6DE2094424675D358388BDE228`

## Project data

The Setup contains the application, not project task data or a copy of a project repository. Task Board reads project information from GitHub. Viewing a project requires the GitHub access allowed by that project's repository settings and the user's sign-in.

Downloading this installer does not make private project data public. Public access to the installer and access to project data are separate.

## Změny verze 1.1.142

Task Board zobrazuje stav startu ještě před inicializací hlavního okna. Při startu použije poslední úplný snapshot dříve načtený z GitHubu; vzdálená data načítá souběžně pouze pro vybraný projekt a z jednoho připnutého commitu. Cache je v aplikačních datech a nečte lokální repozitáře.

## Změny verze 1.0.0

Opraveno zobrazování částečně implementovaných a dosud neověřených řezů roadmapy; Task Board nyní neoznačí otevřené ověření jako Ověřeno.

## Změny verze 1.1.142

Opraveno publikovani aktualizacniho manifestu Task Boardu: ADPR i ADPU nyni dostanou stejny overeny Setup, verzi, historii a SHA-256; tim se obnovuje kontrola aktualizaci v aplikaci.

