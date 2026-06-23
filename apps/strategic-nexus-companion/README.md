# Strategic Nexus Companion

Strategic Nexus Companion je nativni Windows companion/tray aplikace pro Strategic Nexus. Zobrazuje stav projektu, lokalni workflow kontroly a owner-facing diagnostiku v jednom WDUi okne.

## Stazeni

* Verze: `0.16.0`
* Setup: [StrategicNexusCompanionSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/strategic-nexus-companion/StrategicNexusCompanionSetup.exe)
* SHA-256: `5AC5E5ABA8BB2242EDB8F6F279AE2EDE1F02F80CEE4F1BEA946FA4FD239C8EB0`
* Update manifest pro aplikaci: [update.json](update.json)

## Co Aplikace Dela

* bezi jako nativni C++/Win32 + WDUi companion
* poskytuje tray/status-center UI pro Strategic Nexus
* zobrazuje lokalni stav, next steps, reporty a diagnostiku
* umi instalaci pres standardni Windows Installer backend
* vytvari Start Menu zaznam pod `Strategic Nexus`
* jde odinstalovat pres Windows Nastaveni > Aplikace > Nainstalovane aplikace

## Instalace

1. Stahni [StrategicNexusCompanionSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/strategic-nexus-companion/StrategicNexusCompanionSetup.exe).
2. Spust setup.
3. Vyber instalacni slozku, pokud nechces vychozi `C:\Program Files\StrategicNexusCompanion`.
4. Dokonci instalaci.

Po instalaci se aplikace zaregistruje ve Windows jako bezna aplikace a je dostupna ze Start Menu.

## Aktualizace

Aplikace pouziva verejny [update.json](update.json) manifest. Setup je publikovany pres ADPU jako verejny binarni balik; zdrojovy kod a privatni projektove podklady nejsou soucasti tohoto repozitare.

## Odinstalace

Pouzij Windows Nastaveni > Aplikace > Nainstalovane aplikace > Strategic Nexus Companion > Odinstalovat.

## Poznamka K Antiviru

Setup je bezny Windows EXE soubor s vlozenym MSI backendem. Pokud EXE jeste nema dostatecnou reputaci nebo podpis, nektere bezpecnostni nastroje ho muzou kontrolovat dele.
