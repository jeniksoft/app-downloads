# WDUi Framework SDK

WDUi je proprietární C++/Win32 UI framework od Jeniksoft pro skinovatelné nativní Windows aplikace.

## Stažení

* Verze: 0.1.15
* Balík: [WduiFrameworkSdk-0.1.15.zip](WduiFrameworkSdk-0.1.15.zip)
* SHA-256: E3B5F8819C16FFBD4B60AA71106A38173C68208FA4F75A67153E2FEB760AE888
* Velikost: 27342123 bytes
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