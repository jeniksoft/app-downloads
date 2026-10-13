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
## Jarvis Personal 1.0.0: implementace podle kanonické roadmapy

**Aktuální zdrojový přepočet: 13. 10. 2026 | 766 řezů.**

### 99,87 % zdrojově deklarované implementace

**765 z 766** implementačních řezů master roadmapy má stav `verified` (502) nebo `implemented-unverified` (263). Jeden řez je `in-progress`. Počítají se také vnořené podřezy; všechny mají stejnou váhu. Žádná částečná procenta ani zastaralý vážený evidenční odhad.

Toto číslo **neznamená, že je Jarvis produkčně funkční z 99,87 %**, ani že prošel koncovými testy, uživatelskou akceptací nebo schváleným releasem.

| Rodina roadmapy | Implementováno / celkem |
| --- | ---: |
| Platformní základy | 54 / 54 |
| Jádro runtime | 64 / 64 |
| Personal 1.0.0 | 126 / 127 |
| Volitelné schopnosti | 132 / 132 |
| Teams | 70 / 70 |
| Enterprise | 63 / 63 |
| Průřezové schopnosti | 256 / 256 |
| **Celkem** | **765 / 766 = 99,87 %** |

**Zdrojová aktuální agregace:** [implementation-slices.json](implementation-slices.json).

**Stav zveřejnění:** veřejný instalační balíček Personal 1.0.0 zatím není dostupný. Personal, Teams a Enterprise mají vlastní neuzavřené release a runtime brány. Záznam `progress.json` je rozsáhlá historická/detailní projekce, která může do dokončení další synchronizované regenerace obsahovat starší stav či původní vážené evidence; pro aktuální počet napsaných řezů použijte výše uvedený nový strojový souhrn. Staré důkazní grafy nejsou aktuálním ukazatelem implementace.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_END -->

## Co se připravuje

Personal 1.0.0 má být local-first osobní agent pro Windows, který může používat lokální modely, modely v LAN i uživatelem zvoleného providera a nemá vyžadovat povinný Jeniksoft inference cloud ani Jeniksoft tokenové platby.

Vývoj se nyní soustředí především na spolehlivost, recovery, bezpečnost akcí, práci s evidencí a zdroji, memory, support/reprodukci chyb, supervised self-development, instalaci/rollback a ověření na různých skutečných počítačích.

## Dostupnost

Veřejné datum vydání zatím není stanoveno. Verze 1.0.0 bude zveřejněna až po splnění release gates; samotný počet implementovaných funkcí není důvodem označit build za hotový.
