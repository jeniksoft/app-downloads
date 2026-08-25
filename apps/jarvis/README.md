# Project codename: Jarvis

**Jarvis je interní codename projektu ve vývoji, nikoli finální produktový název.**

Cílem je bezplatná edice **Personal 1.0.0**. Až bude připravená k veřejnému vydání, bude zde zveřejněna pod jiným produktovým názvem.

Aktuálně zde není žádný veřejný instalační balíček ke stažení. Dřívější vývojové a beta buildy byly z aktuálního download kanálu odstraněny, protože neodpovídají cílové kvalitě a rozsahu verze 1.0.0.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_BEGIN -->
## Sledování implementace Personal 1.0.0

**Synchronizovaný snapshot: 2026-08-25**

Hlavní číslo je konzervativní index z explicitních milestone evidence. Task Board dodává pouze strukturu kapitol a synchronizaci evidence.

**Jazyk reportu:** čeština pro `cs*`; jiné locale používá anglický fallback. GitHub README je statický a jazyk se určuje při generování.

### Jarvis report

![Grafický cover veřejného reportu Jarvis Personal 1.0.0 vázaného na důkazy](visuals/report-cover.svg)

Tato stránka je veřejný report o stavu vývoje Jarvis Personal 1.0.0 vázaný na důkazy: ukazuje ověřenou implementaci, stav milestone a otevřené důkazní mezery.
Nejde o instalační balíček ani o prohlášení, že je produkt hotový; připravenost vydání je samostatná roadmapová brána.

### Grafický dashboard

![Přehled vázaný na důkazy](visuals/implementation-overview.svg)
![Mapa závislostí architektury](visuals/architecture-map.svg)
![Graf architektonických kapitol](visuals/architecture-chapters.svg)
![Matice evidence milestone](visuals/milestone-evidence.svg)
![Časový graf sledovaného pokroku](visuals/progress-history.svg)

Čísla jsou záměrně kreslená přímo na sloupcích, bodech, uzlech a milestone tiles. Časový graf sledovaného pokroku má na vodorovné ose anonymizované relevantní revize a delta anotace ukazují přírůstky mezi body. Tabulky níže drží stav, kontext a důkazní mezeru.

### Zdrojový inventář Jarvise

Rozsah `tools/jarvis` je čtený z `git archive HEAD`; fyzické řádky zahrnují i prázdné a komentářové řádky. Velikost je uvedená v desítkových MB (1 MB = 1 000 000 bajtů).

| Jazyk / obsah | Soubory | Fyzické řádky | Velikost (MB) |
| --- | ---: | ---: | ---: |
| C/C++ | 940 | 320 268 | 21.24 |
| JSON | 235 | 145 668 | 11.26 |
| Markdown | 642 | 62 058 | 3.09 |
| Python | 125 | 30 377 | 1.25 |
| PowerShell | 50 | 24 517 | 1.28 |
| JSONL | 14 | 2 499 | 6.91 |
| Plain text | 106 | 1 652 | 0.18 |
| INI | 5 | 66 | 0.00 |
| CMake | 1 | 20 | 0.00 |
| Shell | 1 | 17 | 0.00 |
| YAML | 3 | 16 | 0.00 |
| Encoded text | 13 | 13 | 0.06 |
| Nanity pseudocode | 2 | 13 | 0.00 |
| Other text | 7 | 7 | 0.00 |
| **Text/source celkem** | **2 144** | **587 191** | **45.27** |
| Binární assety (mimo řádky) | 35 | — | 14.47 |
| **Trackovaný strom celkem** | **2 179** | **587 191** | **59.74** |

### Přírůstek od předchozí revize

Delta je vůči předchozímu commitnutému snapshotu (`HEAD^`); kladná hodnota znamená přírůstek a záporná úbytek. U prvního commitu je baseline nedostupná.

| Oblast | Δ soubory | Δ fyzické řádky | Δ velikost (MB) |
| --- | ---: | ---: | ---: |
| Text/source celkem | +0 | +0 | +0.00 |
| Binární assety | +0 | — | +0.00 |
| Trackovaný strom celkem | +0 | +0 | +0.00 |

Binární assety jsou uvedené zvlášť, aby nebyly zaměněné za programovací jazyk. Tento inventář je informativní a nemění žádné procento dokončení, ověření, hotova ani release readiness.

### Architektonické kapitoly

| Architektonická kapitola | Stav | Scope |
| --- | --- | --- |
| Aplikační shell, instalátor, update a veřejný kanál | `in-progress` | WDUi application shell; WiX/setup and update contract; ADPU/public-channel integrity |
| Worker core, konverzace, fronta a recovery | `in-progress` | worker queue and journal; durable execution and resume; model-continuity lifecycle |
| Model providery, profily, routing a fallback | `in-progress` | provider readiness and model catalog; role/task routing and fallback; benchmark and liveness evidence |
| Workspace, memory, source, patch, build, Git a web | `in-progress` | workspace/source grounding; memory and provenance; policy-bound file, build, Git and web actions |
| Extension discovery, manager a permissions | `in-progress` | registry and discovery; capability center and permission profiles; read-only connector preview |
| Policy-bound MCP, plugin a app executor runtime | `in-progress` | typed executor scopes; MCP/plugin/app result lifecycle; audit, resume and fail-closed policy |
| Owner-facing UX, diagnostika, support a lokalizace | `in-progress` | chat/project-first UX; diagnostics and support evidence; language and accessibility quality |
| End-to-end QA, dogfooding a bezpečnostní audity | `in-progress` | contract and self-test gates; long dogfood and live acceptance; hardware/configuration and safety evidence |

```mermaid
flowchart LR
    C1[App shell]
    C2[Worker/recovery]
    C1 --> C2
    C3[Models/routing]
    C2 --> C3
    C4[Workspace/actions]
    C3 --> C4
    C5[Extensions]
    C4 --> C5
    C6[Executor]
    C5 --> C6
    C7[UX/support]
    C6 --> C7
    C8[QA/dogfood]
    C7 --> C8
```

### Milestone evidence

| Kapitola | Milestone | Stav | Důkaz / mezera |
| --- | --- | --- | --- |
| App shell | WDUi aplikační shell a základní navigace | `verified-build` | Aktuální capability evidence uvádí warning-free build a contract/self-test gates pro WDUi/Jarvis vrstvy.; mezera: Čerstvé owner-facing vizuální a multi-monitor QA není uzavřené jako runtime acceptance.; typy: build, runtime |
| App shell | Instalátor, update a rollback kontrakt | `partial` | Instalační a update části jsou v architektuře a zdrojovém toku přítomné, ale veřejná P8 release QA je pouze partial.; mezera: Chybí uzavřený čistý install, upgrade a rollback acceptance pack pro Personal 1.0.0.; typy: contract, release-gate |
| App shell | ADPU a veřejný kanál | `partial` | Veřejný kanál a synchronizační kontrakt existují, ale samotná distribuce není důkazem funkčního release.; mezera: Je nutné dokončit a opakovaně ověřit end-to-end publikaci artefaktu, integritu a rollback hranice.; typy: contract, release-gate |
| App shell | Čistá instalace, upgrade, podpis a rollback acceptance | `open` | Release milestone je deklarovaný jako požadavek, nikoli jako uzavřený důkaz.; mezera: Chybí aktuální acceptance pack navázaný na konkrétní release candidate.; typy: roadmap |
| Worker/recovery | Queue, WorkerJournal a persistence | `verified-build` | Capability matrix uvádí queue, worker, typed recovery UI projection, durable evidence gates a skrytý parent/child process-restart self-test jako build/contract ověřené.; mezera: Skutečný crash/restart průchod reálného workflow, dlouhý providerový requeue a V5 owner-facing recovery workflow acceptance zůstávají samostatnými důkazy.; typy: runtime, self-test |
| Worker/recovery | Mid-step resume a přesný Fragment | `verified-contract` | Typed phase, target, digest a exact Fragment selection mají kontraktní self-test evidence.; mezera: Live provider replay a pokračování po skutečné mutaci nejsou tímto kontraktem prokázané.; typy: contract, runtime |
| Worker/recovery | Fail-closed review pro síťové a mutující replaye | `partial` | Fail-closed hranice a typed receipt continuity jsou deterministicky ověřené v existujícím policy/WorkerJournal toku, ale jejich úplná Personal acceptance není uzavřená.; mezera: Zbývá live a skutečný workflow důkaz přes všechny privilegované a mutující replay cesty.; typy: contract, runtime, self-test |
| Worker/recovery | Crash/restart dogfood skutečného workflow | `open` | Roadmap požadavek je známý, ale aktuální receipt není v registru.; mezera: Dodat opakovatelný crash/restart test s identity, journalem, resume a owner review.; typy: roadmap |
| Models/routing | Provider health, capability a identity | `verified-build` | Current evidence covers provider/model identity, readiness and bounded routing contracts.; mezera: Živá dostupnost každého podporovaného endpointu není permanentně prokázaná.; typy: runtime, self-test |
| Models/routing | Typed routing, fallback a blocked stav | `verified-build` | Evidence-driven first-attempt routing a fallback gates jsou v current build evidence.; mezera: Runtime kvalita provideru a 75% first-tier KPI zůstávají measurement target, nikoli hotový výsledek.; typy: build, runtime, self-test |
| Models/routing | Benchmark, idle gate a Work Report evidence | `verified-build` | Registry, scenario validation, idle resource gate, executor a Work Report summary mají build/self-test důkaz.; mezera: Skutečný idle model run a nahromaděné live owner Work Reports nejsou nahrazeny self-testem.; typy: runtime, self-test |
| Models/routing | Živá provider reliability a hardware-aware recommendation | `partial` | Jeden čerstvý localhost Ollama receipt prokazuje průchod konkrétního benchmarkového scénáře; širší provider a hardware matrix zůstává otevřená.; mezera: Dodat opakované live replaye s exact-route, více endpointy/modely, truthful downgrade/blocked receipts a skutečnou hardware matrix.; typy: roadmap, runtime, self-test |
| Workspace/actions | Workspace, source grounding a freshness | `verified-build` | Workspace helpers, source grounding a deterministic project workflow mají current build evidence.; mezera: Úplná kombinatorická action matrix pro každý podporovaný projekt není uzavřená.; typy: runtime, self-test |
| Workspace/actions | Memory, provenance a continuity | `verified-build` | Global memory capture, retrieval, scope nodes, citations and owner review mají executable evidence.; mezera: Semantic inference, online sync a všechny current-state correction scénáře nejsou tímto důkazem uzavřené.; typy: contract, self-test |
| Workspace/actions | Policy-bound file/build/test/Git/web akce | `verified-build` | Policy-bound helper and workspace command paths mají fail-closed selection, output capture a journal evidence.; mezera: Live owner acceptance všech mutujících a browser/app cest není doložená jedním kompletním packem.; typy: runtime, self-test |
| Workspace/actions | Recovery po selhání nástroje a no-overwrite hranice | `partial` | Bezpečnostní guardy a recovery kontrakty existují, ale nejsou kompletně potvrzené napříč runtime cestami.; mezera: Dodat end-to-end receipts pro containment, no-overwrite, destructive guard a recovery po pádu procesu.; typy: contract, runtime |
| Extensions | Registry a discovery rozšíření | `partial` | Kontrakt discovery a capability boundary existují, ale P7 je owner-approved pouze early.; mezera: Chybí uzavřená registrace/discovery lifecycle evidence pro obecné extension typy.; typy: contract, release-gate |
| Extensions | Capability center a permission profily | `contract-only` | Permission model je architektonicky popsaný; kompletní current runtime evidence chybí.; mezera: Dodat implementovaný UI/runtime flow, persistence a negative-path self-tests.; typy: documentation |
| Extensions | Read-only connector preview | `contract-only` | Read-only preview je součástí roadmapového směru, ne uzavřený universal connector proof.; mezera: Dodat konkrétní connector fixture, source identity, permission review a ověřený render.; typy: roadmap |
| Extensions | Install/update/disable lifecycle rozšíření | `open` | Obecný lifecycle není v Personal evidence uzavřen.; mezera: Dodat safe install, update, disable, rollback, ownership a audit receipts.; typy: release-gate |
| Executor | Typed executor scopes a stream lifecycle | `verified-contract` | Typed executor scope contract a bounded result lifecycle mají current contract evidence.; mezera: Univerzální runtime acceptance pro každý MCP/plugin/app typ není uzavřená.; typy: contract, runtime |
| Executor | Policy, audit, resume a fail-closed executor | `partial` | Auditní a fail-closed principy i deterministický policy-denied receipt jsou ověřené napříč přímými executor adaptery, ale cross-runtime proof je stále částečný.; mezera: Zbývá live a skutečný workflow důkaz pro generické, privilegované a mutující adaptery.; typy: contract, runtime, self-test |
| Executor | MCP/plugin/app result lifecycle | `partial` | Existující read-only app connector nyní po skutečném PolicyExecutor runtime předá typed receipt do WorkerJournal před dispatch-done. P4.12 klasifikuje MCP/plugin/app entrypoint přes typovaný no-side-effect obal a P4.14 přidává jednu manifestem vázanou vratnou mutační extension třídu s explicitním rollbackem a Unknown gate; deterministické self-testy, source guardy a navazující lifecycle/receipt guardy prošly.; mezera: Dodat generic typed fixtures pro success, partial, failure, timeout, retry a owner review; skutečný MCP/plugin stdio/process runtime, další mutační extension třídy a owner-approved live acceptance nejsou uzavřené.; typy: documentation, self-test |
| Executor | Live external integration a resume acceptance | `open` | Live MCP/plugin/app acceptance není doložena jako společný current receipt.; mezera: Dodat owner-approved, identity-bearing, reproducible live acceptance pack.; typy: release-gate |
| UX/support | First-run, setup a diagnostics | `partial` | Provider-status vrstva má provider-free typed first-run readiness a chat/project composer má nyní společnou baseline pro trvalý chat, projekt a přílohy zprávy; P8 owner-facing QA je stále partial.; mezera: Dodat čerstvý owner walkthrough v podporovaných DPI/multi-monitor konfiguracích, V5 live setup acceptance a skutečné tray recovery pro chat/project/attachments.; typy: build, runtime, self-test |
| UX/support | Failure/recovery a ticket UI | `partial` | Failure/recovery a Secure Ticket kontrakty existují; P6.1 typovaný stavový automat, P6.2 read-only evidence candidate refs, P6.3 shared sensitive-data boundary, P6.4 protected local draft store, P6.5 owner evidence selection review, P6.6 immutable prepared manifest digest, P6.7 bounded local export package, P6.8 read-only untrusted reproduction intake a P6.9 confirmed-bug regression lineage mají build/self-test důkaz, ale P6 runtime a P8 QA zůstávají partial.; mezera: P6.7 local export, P6.8 untrusted import/reproduction a P6.9 regression lineage jsou ověřené bez sítě; otevřené zůstávají kompletní ticket UI path, P6 runtime a owner-facing V5 acceptance.; typy: contract, release-gate, self-test |
| UX/support | Jazyk, lokalizace a accessibility quality | `partial` | Localization accounting a P8.8 read-only release gate existují; fallback backlog je explicitně otevřený a gate jej správně odmítá jako release blocker.; mezera: Uzavřít překladový backlog independently reviewed memory a projít accessibility/DPI acceptance na reálném UI.; typy: runtime, self-test |
| UX/support | Owner-facing live QA | `open` | Žádný aktuální univerzální live owner acceptance receipt není v manifestu.; mezera: Dodat vizuální a interakční QA pack včetně accessibility, DPI a recovery scénářů.; typy: roadmap |
| QA/dogfood | Contract/self-test gates | `verified-build` | Current capability matrix uvádí warning-free build a více self-test gates.; mezera: Self-test nenahrazuje dlouhý dogfood ani reálnou konfiguraci ownera.; typy: build, runtime, self-test |
| QA/dogfood | Deterministic dogfood a regression fixtures | `partial` | Contract a dogfood řídicí rovina včetně P7.1-P7.9 mají deterministické důkazy, ale potvrzené ticket-driven regression closure, skutečná production Nanity, mentor finding/live repair execution a plný sémantický ASM graf nejsou uzavřené.; mezera: Doplnit skutečnou Jarvis-authored Nanity, end-to-end P7.6/live důkaz, reálný mentor finding pro živé P7.8 provedení a úplnou bug-to-regression closure; P7.9 je pouze bounded source-backed refresh a plná semantic discovery zůstává otevřená.; typy: contract, release-gate, self-test |
| QA/dogfood | Reálný hardware/configuration matrix | `open` | Owner-approved release source označuje hardware/configuration matrix jako early.; mezera: Dodat opakovatelná měření na skutečných konfiguracích s identity a environment receipts.; typy: release-gate, self-test |
| QA/dogfood | Release acceptance pack a bezpečnostní audit | `open` | P8.9 nyní obsahuje deterministický evaluator immutable clean-install receiptu, P8.10 evaluator přesné pre-1.0 upgrade matice a P8.11 evaluator LKG rollback receiptu nad existujícím build/setup tokem, ale samotný V6 live acceptance pack stále není dodaný.; mezera: Dodat current release candidate, signed artifacts, skutečný clean install/upgrade/rollback a safety audit receipts.; typy: release-gate, self-test |

```mermaid
flowchart TD
    G1[App shell]
    G1M1[WDUi aplikační shell a základní navigace<br/>verified-build]
    G1 --> G1M1
    G1M2[Instalátor, update a rollback kontrakt<br/>partial]
    G1M1 --> G1M2
    G1M3[ADPU a veřejný kanál<br/>partial]
    G1M2 --> G1M3
    G1M4[Čistá instalace, upgrade, podpis a rollback acceptance<br/>open]
    G1M3 --> G1M4
    G10[Worker/recovery]
    G10M1[Queue, WorkerJournal a persistence<br/>verified-build]
    G10 --> G10M1
    G10M2[Mid-step resume a přesný Fragment<br/>verified-contract]
    G10M1 --> G10M2
    G10M3[Fail-closed review pro síťové a mutující replaye<br/>partial]
    G10M2 --> G10M3
    G10M4[Crash/restart dogfood skutečného workflow<br/>open]
    G10M3 --> G10M4
    G19[Models/routing]
    G19M1[Provider health, capability a identity<br/>verified-build]
    G19 --> G19M1
    G19M2[Typed routing, fallback a blocked stav<br/>verified-build]
    G19M1 --> G19M2
    G19M3[Benchmark, idle gate a Work Report evidence<br/>verified-build]
    G19M2 --> G19M3
    G19M4[Živá provider reliability a hardware-aware recommendation<br/>partial]
    G19M3 --> G19M4
    G28[Workspace/actions]
    G28M1[Workspace, source grounding a freshness<br/>verified-build]
    G28 --> G28M1
    G28M2[Memory, provenance a continuity<br/>verified-build]
    G28M1 --> G28M2
    G28M3[Policy-bound file/build/test/Git/web akce<br/>verified-build]
    G28M2 --> G28M3
    G28M4[Recovery po selhání nástroje a no-overwrite hranice<br/>partial]
    G28M3 --> G28M4
    G37[Extensions]
    G37M1[Registry a discovery rozšíření<br/>partial]
    G37 --> G37M1
    G37M2[Capability center a permission profily<br/>contract-only]
    G37M1 --> G37M2
    G37M3[Read-only connector preview<br/>contract-only]
    G37M2 --> G37M3
    G37M4[Install/update/disable lifecycle rozšíření<br/>open]
    G37M3 --> G37M4
    G46[Executor]
    G46M1[Typed executor scopes a stream lifecycle<br/>verified-contract]
    G46 --> G46M1
    G46M2[Policy, audit, resume a fail-closed executor<br/>partial]
    G46M1 --> G46M2
    G46M3[MCP/plugin/app result lifecycle<br/>partial]
    G46M2 --> G46M3
    G46M4[Live external integration a resume acceptance<br/>open]
    G46M3 --> G46M4
    G55[UX/support]
    G55M1[First-run, setup a diagnostics<br/>partial]
    G55 --> G55M1
    G55M2[Failure/recovery a ticket UI<br/>partial]
    G55M1 --> G55M2
    G55M3[Jazyk, lokalizace a accessibility quality<br/>partial]
    G55M2 --> G55M3
    G55M4[Owner-facing live QA<br/>open]
    G55M3 --> G55M4
    G64[QA/dogfood]
    G64M1[Contract/self-test gates<br/>verified-build]
    G64 --> G64M1
    G64M2[Deterministic dogfood a regression fixtures<br/>partial]
    G64M1 --> G64M2
    G64M3[Reálný hardware/configuration matrix<br/>open]
    G64M2 --> G64M3
    G64M4[Release acceptance pack a bezpečnostní audit<br/>open]
    G64M3 --> G64M4
```

Detailní privátní zdrojové cesty, receipts a owner-specific data zůstávají v CPM evidence manifestu.

### Vývoj v relevantních revizích

Každý bod a změnová anotace jsou v časovém grafu historie; tabulka uvádí přírůstky všech hlavních metrik oproti předchozímu bodu a každý anonymizovaný záznam zůstává i ve strojově čitelném JSON. Raw private source commit, subject ani interní cesta se do veřejného repa nekopírují.

| Veřejná revize | Datum | Δ primary | Δ implementace | Δ ověření | Δ hotovo | Δ release readiness | Změněné kapitoly | Milestone evidence events |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| `b3ce2075fb03` | 2026-08-24 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | evidence-only | — |
| `1338c2e61c1c` | 2026-08-24 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | owner-ux | 1: owner-ux/first-run-diagnostics |
| `9d1e655a8643` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | owner-ux | 1: owner-ux/first-run-diagnostics |
| `5f1415036e96` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | owner-ux | 1: owner-ux/first-run-diagnostics |
| `9386e5930c44` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | owner-ux | 1: owner-ux/first-run-diagnostics |
| `b9a5b6eff3a7` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | owner-ux | 1: owner-ux/first-run-diagnostics |
| `54c1f3d34644` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | owner-ux | 1: owner-ux/language-accessibility-quality |
| `4f7e8600b92d` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/release-acceptance-pack |
| `da46d3948150` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/release-acceptance-pack |
| `815f0afb122d` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/release-acceptance-pack |
| `0b72861e1ed9` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/release-acceptance-pack |
| `c7a0f53679e5` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/release-acceptance-pack |
| `67ac3f8ef51f` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/release-acceptance-pack |
| `e30d365315ae` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/hardware-configuration-matrix |
| `762b687e684f` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/hardware-configuration-matrix |
| `fbb9d45ba85a` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/hardware-configuration-matrix |
| `c2bad3264703` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/hardware-configuration-matrix |
| `11579b637f98` | 2026-08-25 | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 | qa-dogfood | 1: qa-dogfood/hardware-configuration-matrix |

Úplná strojově čitelná historie: [progress-history.json](progress-history.json). Snapshot: [progress.json](progress.json).

### Release readiness

| Release oblast | Stav |
| --- | --- |
| Recovery a durable execution | `partial` |
| Model/provider spolehlivost | `advanced` |
| Intake, research a source quality | `partial` |
| Workspace a bezpečné akce | `advanced` |
| Memory a continuity | `advanced` |
| Secure Support Ticket | `early` |
| Supervised self-development | `early` |
| UX, installer, update a release QA | `partial` |
| Reálný hardware/configuration matrix | `early` |

### Měřicí kontrakt

- `primary`: vážené minimum implementace a ověření po jednotlivých milnících; milník bez ověřeného důkazu nemůže vytvořit hotovo.
- `implementation`: explicitní milestone state s horními stropy; architektura, source-size ani plán číslo nezvyšují.
- `verification`: explicitní evidence; kontrakt nebo build není totéž co live runtime nebo owner acceptance.
- `done`: vážené minimum na každém milníku, potom vážený roll-up kapitol a jejich evidence cap.
- `Task Board`: slouží k mapování kapitol, vah a synchronizaci odvozené evidence; není samostatnou skórovanou osou.
- Relevantní revize vzniká při změně nakonfigurovaných vstupů měření; commit bez změny evidence zůstává jako `evidence-only`.
- Plánovaný stav, historická dokumentace, source-size, počet řádků ani samotný commit nemohou zvýšit primary bez evidence manifestu; source inventory je pouze informativní.
<!-- JARVIS_IMPLEMENTATION_PROGRESS_END -->

## Co se připravuje

Personal 1.0.0 má být local-first osobní agent pro Windows, který může používat lokální modely, modely v LAN i uživatelem zvoleného providera a nemá vyžadovat povinný Jeniksoft inference cloud ani Jeniksoft tokenové platby.

Vývoj se nyní soustředí především na spolehlivost, recovery, bezpečnost akcí, práci s evidencí a zdroji, memory, support/reprodukci chyb, supervised self-development, instalaci/rollback a ověření na různých skutečných počítačích.

## Dostupnost

Veřejné datum vydání zatím není stanoveno. Verze 1.0.0 bude zveřejněna až po splnění release gates; samotný počet implementovaných funkcí není důvodem označit build za hotový.
