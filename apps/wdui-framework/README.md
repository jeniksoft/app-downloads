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

<!-- WDUI_PF_PROGRESS_BEGIN -->
## WDUi Framework — Omezený closeout řezů PF-00 a PF-01

**Poslední snapshot: 2026-11-08**

Tento veřejný přehled zahrnuje pouze řezy PF-00 a PF-01, nikoli celou roadmapu WDUi. Implementace obou řezů je doložena jako 100 %, ověření zůstává 0 % a souhrnné hotovo proto zůstává 0 %.

### Identita zveřejněného closeoutu

Řez `PF-00-PF-01` je svázán se zdrojovým SHA `1fb68308311a66e1511c02f812ce33082cf60562` a closeout SHA `b11d3f2dc55cb3f262f4522d7d74fb81846c3059`. Stav: **verified**.

### Metriky řezu

| Metrika | Hodnota |
| --- | ---: |
| Implementace tohoto omezeného řezu | 100.00 % |
| Ověření | 0.00 % |
| Hotovo | 0.00 % |

### Grafický přehled

![Grafický stav WDUi Framework](visuals/implementation-overview.svg)

### Milníky

| ID | Milník | Stav | Implementace | Ověření | Evidence a otevřená mezera |
| --- | --- | --- | ---: | ---: | --- |
| `PF-00` | PF-00 — sjednocení reference 108 presetů a 216 záznamů | `implemented-unverified` | 100.00 % | 0.00 % | Důkaz: Inventář 108 presetů a 216 záznamů v 108 párech je zdokumentovaný. Odchylka proti referenci je 216 změněných hashů, 0 chybějících a 0 nových záznamů; reference nebyla přepsána. — Mezera: Všech 216 vizuálních rozdílů čeká na posouzení; AAA a výslovné owner schválení se netvrdí. |
| `PF-01` | PF-01 — typovaná ShapeSpec a geometrické invariants | `implemented-unverified` | 100.00 % | 0.00 % | Důkaz: Implementace ShapeSpec, path compiler fixture a fuzz validátor mají zdrojově připnuté testy s exit 0; fuzz ověřil 2 048 případů. — Mezera: Živá nezávislá vizuální kontrola, Direct2DNative presented read-back, UIA/screen-reader, downstream a Release acceptance zůstávají otevřené. |

Strojově čitelný snapshot: [progress.json](progress.json). Historie tohoto profilu záměrně obsahuje pouze aktuální closeoutový bod: [progress-history.json](progress-history.json).
<!-- WDUI_PF_PROGRESS_END -->
