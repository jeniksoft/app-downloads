# Project codename: Jarvis

**Jarvis je interní codename projektu ve vývoji, nikoli finální produktový název.**

Cílem je bezplatná edice **Personal 1.0.0**. Až bude připravená k veřejnému vydání, bude zde zveřejněna pod jiným produktovým názvem.

Aktuálně zde není žádný veřejný instalační balíček ke stažení. Dřívější vývojové a beta buildy byly z aktuálního download kanálu odstraněny, protože neodpovídají cílové kvalitě a rozsahu verze 1.0.0.

## Zpětná vazba / Feedback

Jarvis je veřejně sledovaný vývojový projekt. Pro zpětnou vazbu použij prosím jednu z těchto cest:

- [🐞 Nahlásit chybu / Report a bug](https://github.com/jeniksoft/app-downloads/issues/new?template=bug_report.yml)
- [💡 Navrhnout zlepšení / Suggest an improvement](https://github.com/jeniksoft/app-downloads/issues/new?template=feature_request.yml)
- [💬 Otevřít diskuzi / Start a discussion](https://github.com/jeniksoft/app-downloads/discussions)

Do veřejných příspěvků nevkládej hesla, tokeny, osobní údaje ani celé soukromé logy. Přikládej pouze očištěné a nezbytné informace.

## Věkové omezení / Age restriction (18+)

**CZ:** Jarvis je určen výhradně dospělým uživatelům od 18 let. Pokud ti ještě nebylo 18 let, Jarvis nepoužívej.

**EN:** Jarvis is intended exclusively for adults aged 18 and over. If you are under 18, do not use Jarvis.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_BEGIN -->
## Jarvis Personal 1.0.0 — skutečný stav roadmapy

**Aktualizováno: 2026-10-13 · 766 řezů**

Implementační pokrytí podle master roadmapy je **98.99 %**. Zobrazené stavy kapitol se odvozují ze stavů jejich řezů, takže zastaralý stav rodiče nezastíní skutečný postup.

### Souhrn kanonických stavů

| Metrika | Hodnota | Význam |
| --- | ---: | --- |
| `implementation_complete_percent` | 98.99 % | Průměrný postup podle kanonických řezů roadmapy. |
| `roadmap_implemented_percent` | 98.96 % | Implementované řezy včetně všech ověřených. |
| `roadmap_verified_percent` | 65.54 % | Řezy, které jsou v master roadmapě ověřené. |
| `roadmap_in_progress_percent` | 0.13 % | Řezy, na kterých se podle master roadmapy pracuje. |
| `roadmap_architecture_percent` | 0.91 % | Řezy, které jsou zatím jen navržené. |

### Jarvis report

![Kanonický roadmap report Jarvis Personal 1.0.0](visuals/report-cover.svg)

### Grafický dashboard

![Souhrn kanonických stavů roadmapy](visuals/implementation-overview.svg)
![Roadmapa a postup řezů Jarvis](visuals/roadmap-editions.svg)

Grafy a tabulky vycházejí ze stejné kanonické roadmapy. Implementováno zahrnuje Ověřeno; Rozpracováno a Architektura jsou samostatné stavy. Staré důkazní a historické grafy zůstávají odpojené.

### Kanonický stav roadmapových skupin

Implementováno je kumulativní a vždy zahrnuje ověřené řezy. Ostatní stavové podíly jsou oddělené.

| Roadmapová skupina | Řezů | Pokrytí | Implementováno včetně ověřených | Ověřeno | Rozpracováno | Architektura |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Platformní základy | 54 | 100.00 % | 100.00 % | 100.00 % | 0.00 % | 0.00 % |
| Jádro runtime | 64 | 89.06 % | 89.06 % | 51.56 % | 0.00 % | 10.94 % |
| Personal 1.0.0 | 127 | 99.41 % | 99.21 % | 98.43 % | 0.79 % | 0.00 % |
| Volitelné tratě | 132 | 100.00 % | 100.00 % | 77.27 % | 0.00 % | 0.00 % |
| Teams | 70 | 100.00 % | 100.00 % | 20.00 % | 0.00 % | 0.00 % |
| Enterprise | 63 | 100.00 % | 100.00 % | 14.29 % | 0.00 % | 0.00 % |
| Průřezové capability tratě | 256 | 100.00 % | 100.00 % | 64.45 % | 0.00 % | 0.00 % |

### Roadmapa produktu

**Legenda ikon:** · <span role="img" title="Ověřeno: Ověřený stav; zelená fajfka znamená, že řez splnil ověřovací bránu." aria-label="Ověřeno: Ověřený stav; zelená fajfka znamená, že řez splnil ověřovací bránu.">✅</span> Ověřeno · <span role="img" title="Implementováno: Kanonický stav řezu je Implementováno; stav Ověřeno ještě není uzavřený." aria-label="Implementováno: Kanonický stav řezu je Implementováno; stav Ověřeno ještě není uzavřený.">🟦</span> Implementováno · <span role="img" title="Rozpracováno: Práce pokračuje; oranžová značka označuje rozpracovaný stav." aria-label="Rozpracováno: Práce pokračuje; oranžová značka označuje rozpracovaný stav.">🟠</span> Rozpracováno · <span role="img" title="Architektura: Kanonický stav řezu je Architektura; implementace ještě není deklarovaná." aria-label="Architektura: Kanonický stav řezu je Architektura; implementace ještě není deklarovaná.">⚪</span> Architektura · <span role="img" title="Blokováno: Stav je odmítnutý nebo blokovaný; červená značka není úspěch." aria-label="Blokováno: Stav je odmítnutý nebo blokovaný; červená značka není úspěch.">⛔</span> Blokováno
V grafu jsou všechny roadmapové kapitoly, uzly a řezy; textové kopie jsou v češtině a popisují, co Jarvis díky dané části umí.

**Synchronizace s kanonickou roadmapou: opraveno stavů 0 · popisů 7 · přidáno 0 · odebráno 0**

![Kanonická roadmapa Jarvis](visuals/roadmap-editions.svg)

Duplicitní tabulky řezů se nezobrazují. Úplné aktuální stavy a popisy jsou v [progress.json](progress.json). Historický záznam zůstává oddělený v [progress-history.json](progress-history.json).

### Release gates

| Stav | Edice | Popis | Ověření | Závislosti |
| --- | --- | --- | --- | ---: |
| <span role="img" title="Rozpracováno: Práce pokračuje; oranžová značka označuje rozpracovaný stav." aria-label="Rozpracováno: Práce pokračuje; oranžová značka označuje rozpracovaný stav.">🟠</span> Rozpracováno | `personal-1.0.0` | Bezplatný local-first Jarvis pro jednoho člověka. | `V6` | 9 |
| <span role="img" title="Otevřeno: Kanonický stav řezu je Implementováno; stav Ověřeno ještě není uzavřený." aria-label="Otevřeno: Kanonický stav řezu je Implementováno; stav Ověřeno ještě není uzavřený.">🟦</span> Otevřeno | `teams` | Spolupráce v jednom zákaznicky vlastněném TeamRealmu. | `V6` | 12 |
| <span role="img" title="Otevřeno: Kanonický stav řezu je Implementováno; stav Ověřeno ještě není uzavřený." aria-label="Otevřeno: Kanonický stav řezu je Implementováno; stav Ověřeno ještě není uzavřený.">🟦</span> Otevřeno | `enterprise` | Rekurzivní zákaznicky vlastněná organizace a Konstelace. | `V6` | 10 |

Roadmapový postup není prohlášením, že je produkt hotový nebo připravený k vydání; rozhoduje stav samostatné release brány.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_END -->

## Co se připravuje

Personal 1.0.0 má být local-first osobní agent pro Windows, který může používat lokální modely, modely v LAN i uživatelem zvoleného providera a nemá vyžadovat povinný Jeniksoft inference cloud ani Jeniksoft tokenové platby.

Vývoj se nyní soustředí především na spolehlivost, recovery, bezpečnost akcí, práci s evidencí a zdroji, memory, support/reprodukci chyb, supervised self-development, instalaci/rollback a ověření na různých skutečných počítačích.

## Dostupnost

Veřejné datum vydání zatím není stanoveno. Verze 1.0.0 bude zveřejněna až po splnění release gates; samotný počet implementovaných funkcí není důvodem označit build za hotový.
