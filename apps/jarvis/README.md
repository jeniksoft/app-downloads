# Project codename: Jarvis

**Jarvis je interní codename projektu ve vývoji, nikoli finální produktový název.**

Cílem je bezplatná edice **Personal 1.0.0**. Až bude připravená k veřejnému vydání, bude zde zveřejněna pod jiným produktovým názvem.

Aktuálně zde není žádný veřejný instalační balíček ke stažení. Dřívější vývojové a beta buildy byly z aktuálního download kanálu odstraněny, protože neodpovídají cílové kvalitě a rozsahu verze 1.0.0.

## Personal 1.0.0 progress

<!-- JARVIS_PROGRESS_BEGIN -->
**Release readiness: 50 %**

Toto číslo neznamená „50 % řádků kódu“. Je to vážený ukazatel připravenosti k vydání podle aktuální Personal 1.0.0 roadmapy a ověřené evidence. Může se pohybovat oběma směry, pokud nové testy odhalí blocker nebo se zpřísní release kritéria.

| Oblast | Stav | Readiness |
| --- | --- | ---: |
| Recovery a durable execution | partial | 50 % |
| Model/provider spolehlivost | advanced | 75 % |
| Intake, research a source quality | partial | 50 % |
| Workspace a bezpečné akce | advanced | 75 % |
| Memory a continuity | advanced | 75 % |
| Secure Support Ticket | early | 25 % |
| Supervised self-development | early | 25 % |
| UX, installer, update a release QA | partial | 50 % |
| Reálný hardware/configuration matrix | early | 25 % |

Stupnice: `early = 25 %`, `partial = 50 %`, `advanced = 75 %`, `verified = 100 %`. Váhy jednotlivých oblastí nejsou stejné; recovery a release QA mají vyšší váhu.

Machine-readable veřejný snapshot: [progress.json](progress.json).
<!-- JARVIS_PROGRESS_END -->

## Co se připravuje

Personal 1.0.0 má být local-first osobní agent pro Windows, který může používat lokální modely, modely v LAN i uživatelem zvoleného providera a nemá vyžadovat povinný Jeniksoft inference cloud ani Jeniksoft tokenové platby.

Vývoj se nyní soustředí především na spolehlivost, recovery, bezpečnost akcí, práci s evidencí a zdroji, memory, support/reprodukci chyb, supervised self-development, instalaci/rollback a ověření na různých skutečných počítačích.

## Dostupnost

Veřejné datum vydání zatím není stanoveno. Verze 1.0.0 bude zveřejněna až po splnění release gates; samotný počet implementovaných funkcí není důvodem označit build za hotový.
