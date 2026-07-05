# WDUi Durable App Template

WDUi Durable App Template je referenční instalační kanál pro nativní C++/Win32 aplikace s WDUi, OOP strukturou, event tokem, callback hranicemi, update manifestem a běžným Windows setup lifecycle.

## Stažení

* Verze: `1.0.40`
* Setup: [WduiDurableAppTemplateSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/wdui-durable-app-template/WduiDurableAppTemplateSetup.exe)
* SHA-256: `A804E938AF703965F3C16D0E9D2B44B2A5A0E001BEB763DA72FD1779705B80DA`
* Update manifest pro aplikaci: [update.json](update.json)

## Co Aplikace Dělá

* ukazuje referenční owner-facing WDUi shell
* ověřuje trvalou konfiguraci, stav UI a update manifest
* používá setup tok s instalací, opravou, odinstalací a historií změn
* slouží jako runtime smoke kanál pro durable app šablonu

## Instalace

1. Stáhni [WduiDurableAppTemplateSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/wdui-durable-app-template/WduiDurableAppTemplateSetup.exe).
2. Spusť setup.
3. Dokonči instalaci podle dialogu.

## Aktualizace

Aplikace umí kontrolovat veřejný [update.json](update.json) manifest a zobrazit historii změn v dialogu `O aplikaci`.

## Odinstalace

Použij Windows Nastavení > Aplikace > Nainstalované aplikace > WDUi Durable App Template > Odinstalovat.
