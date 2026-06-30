# WDUi Framework SDK

WDUi je proprietární C++/Win32 UI framework od Jeniksoft pro skinovatelné nativní Windows aplikace.

## Stažení

* Verze: 0.1.9
* Balík: [WduiFrameworkSdk-0.1.9.zip](WduiFrameworkSdk-0.1.9.zip)
* SHA-256: 2781AA94C6B37135A617F0B81003FCC53D930D7129B238E112579BFA316703A6
* Velikost: 23828527 bytes
* Manifest: [update.json](update.json)

## Co balík obsahuje

* veřejné hlavičky include\wdui\*.h
* hotovou MSVC x64 statickou knihovnu lib\x64\wdui.lib
* binární demo bin\wdui_demo.exe
* výchozí JSON skiny a app-local fonty včetně licencí
* otevřený ukázkový zdroj examples\minimal_app.cpp
* návod k build/link/runtime assets

Balík záměrně neobsahuje zdrojové .cpp soubory WDUi knihovny.

## Změny ve verzi 0.1.9

* `SelectableTextBlock` zrychluje layout dlouhých word-wrap textů: prefix widths se měří jednou na odstavec, ne znovu pro každý vizuální řádek.
* Přidaná diagnostika `textPrefixMeasureCount` hlídá, že se optimalizace nerozbije při dalších úpravách textových controlů.

## Licence

WDUi knihovna není open source. Ukázky v examples\ jsou otevřené pod MIT-0; fonty mají vlastní SIL OFL licence.
