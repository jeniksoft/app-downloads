# WDUi Framework SDK

WDUi je proprietární C++/Win32 UI framework od Jeniksoft pro skinovatelné nativní Windows aplikace.

## Stažení

* Verze: 1.0.0
* Balík: [WduiFrameworkSdk-1.0.0.zip](WduiFrameworkSdk-1.0.0.zip)
* SHA-256: 25E88E95BF13C6AEC749508962DEFBA60535B04C9459F56E112A2AE376427CD1
* Velikost: 39038488 bytes
* Manifest: [update.json](update.json)

## Co balík obsahuje

* veřejné hlavičky include\wdui\*.h
* hotovou MSVC x64 statickou knihovnu lib\x64\wdui.lib
* binární demo bin\wdui_demo.exe
* výchozí JSON skiny a app-local fonty včetně licencí
* otevřený ukázkový zdroj examples\minimal_app.cpp
* návod k build/link/runtime assets

Balík záměrně neobsahuje zdrojové .cpp soubory WDUi knihovny. Demo ve složce
bin má vlastní skins a fonts vedle EXE, takže příkaz
bin\wdui_demo.exe --build-info-smoke --require-runtime-skins po rozbalení
ověří stejný runtime skin pack jako aplikace.

## Licence

WDUi knihovna není open source. Ukázky v examples\ jsou otevřené pod MIT-0; fonty mají vlastní SIL OFL licence.