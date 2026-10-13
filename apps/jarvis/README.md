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

**Aktualizováno 13. října 2026.**

**Implementováno je 765 z 766 kanonických řezů, tedy 99,87 %.** Jde o stav **napsané implementace** podle počtu roadmapových řezů, nikoliv o procento bezchybně fungujícího produktu ani podíl řádků zdrojového kódu.

Výpočet je deterministický: každý vrcholový i vnořený řez se počítá právě jednou; stav `verified` a `implemented-unverified` znamená implementováno. Ostatní stavy se za hotové nezapočítávají.

| Kanonický stav | Řezů | Podíl |
| --- | ---: | ---: |
| Implementováno, z toho stavově ověřeno | 765 (502) | 99,87 % (65,54 %) |
| Rozpracováno | 1 | 0,13 % |
| Pouze architektura | 0 | 0 % |
| **Celková roadmapa** | **766** | **100 %** |

| Oblast | Implementováno |
| --- | ---: |
| Platformní základy | 54 / 54 |
| Jádro runtime | 64 / 64 |
| Personal | 126 / 127 |
| Volitelné schopnosti | 132 / 132 |
| Teams | 70 / 70 |
| Enterprise | 63 / 63 |
| Průřezové schopnosti | 256 / 256 |

Jediným souhrnným rozpracovaným řezem zůstává **P8.15: komponentové aktualizace a vratný rollback**. Jeho podčásti již mají rozsáhlou implementaci, ale rodičovský řez není uzavřen jako celek. Všem položkám se ponechává jejich přesný kanonický stav.

### Aktuální strojový report

[**Aktuální kompletní přehled počtů a stavů kapitol**](roadmap-implementation.v1.json) je odvozen z aktuálního master JSON v CPM, se SHA-256 otiskem zdroje. Neobsahuje soukromé pracovní logy.

Původní vážený **evidenční přehled 37,48 % byl odstraněn z hlavního zobrazení**: měřil jinou veličinu a nebyl procentem napsané implementace. Archivní soubor [`progress.json`](progress.json) a dříve vygenerované velké SVG grafy se teprve musí v plném publikačním běhu znovu přegenerovat; **nepoužívejte jejich stará procenta pro současný stav**.

### Důležité rozlišení

Stavy typu `verified` v roadmapě znamenají **ověření příslušného deklarovaného rozsahu**, často izolovaného kontraktu či provider-free testu. Neprokazují automaticky produkční propojení modelu, UI, Workeru, instalace, periferií, spolupráce více počítačů ani připravenost veřejného vydání. Tyto brány jsou samostatné.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_END -->

## Co se připravuje

Personal 1.0.0 má být local-first osobní agent pro Windows, který může používat lokální modely, modely v LAN i uživatelem zvoleného providera a nemá vyžadovat povinný Jeniksoft inference cloud ani Jeniksoft tokenové platby.

Vývoj se nyní soustředí především na spolehlivost, recovery, bezpečnost akcí, práci s evidencí a zdroji, memory, support/reprodukci chyb, supervised self-development, instalaci/rollback a ověření na různých skutečných počítačích.

## Dostupnost

Veřejné datum vydání zatím není stanoveno. Verze 1.0.0 bude zveřejněna až po splnění release gates; samotný počet implementovaných funkcí není důvodem označit build za hotový.
