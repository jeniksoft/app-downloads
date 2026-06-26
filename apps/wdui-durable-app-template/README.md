# WDUi Durable App Template

WDUi Durable App Template je referenční instalační kanál pro nativní C++/Win32 aplikace s WDUi, OOP strukturou, event tokem, callback hranicemi, update manifestem a běžným Windows setup lifecycle.

## Stažení

* Verze: `1.0.37`
* Setup: [WduiDurableAppTemplateSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/wdui-durable-app-template/WduiDurableAppTemplateSetup.exe)
* SHA-256: `183AA7F32DB2D0B5A24EA7803A2FF922C61C290984BC27531E66FCED4426FE66`
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
