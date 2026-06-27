# WDUi Durable App Template

WDUi Durable App Template je referenční instalační kanál pro nativní C++/Win32 aplikace s WDUi, OOP strukturou, event tokem, callback hranicemi, update manifestem a běžným Windows setup lifecycle.

## Stažení

* Verze: `1.0.39`
* Setup: [WduiDurableAppTemplateSetup.exe](https://github.com/jeniksoft/app-downloads/raw/main/apps/wdui-durable-app-template/WduiDurableAppTemplateSetup.exe)
* SHA-256: `6558181B3E0529C2F46E1CFC2EB91B958F18D3DEE2F8E4912E6E57434E4C7DE6`
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
