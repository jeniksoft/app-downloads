# Planetopia – vývojový report nové verze

**Planetopia je interní označení nové verze pluginu ve vývoji, nikoli potvrzení
hotového vydání.** Tento report je veřejný stavový snapshot pro zákazníky,
partnery a systémy, které nemají k dispozici češtinu. Česká část je hlavní;
níže je stejný závěr v anglickém fallbacku.

Aktuálně zde není žádný veřejný instalační balíček ani distribuční demo obsah.

<!-- PLANETOPIA_IMPLEMENTATION_PROGRESS_BEGIN -->
## Sledování vývoje nové verze

**Synchronizovaný snapshot: 2026-09-02**

**Cílový engine: Unreal Engine 5.8**

**Stav: 🟠 Rozpracováno – není připraveno k vydání**

### Co tento report potvrzuje

Report odděluje implementaci, runtime důkaz, vizuální kontrolu a release
hranice. Build nebo existující asset sám o sobě neznamená, že je funkční demo
hotové. Čísla a verdikty níže jsou konzervativní a nepovyšují interní stav na
produktový slib.

### Důležitá kompatibilita

Stará verze **Planetopia v3.1.4 pro Unreal Engine 5.4** je zmrazená,
nepodporovaná a není součástí tohoto vývoje. Její sample ani její opravy nejsou
release cílem. Zákazník má čekat na novou samostatnou UE 5.8 verzi.

### Aktuální verdikt

Nová větev už obsahuje základní plugin-only mapu, Fab-safe vlastní makety,
jednobarevné fake povrchové swatche a replacement sloty. UE 5.8 RHI běh
prošel bootstrapem, texturovací frontou, dynamickým meshovým taskem a dvěma
pozdějšími generacemi. Ochrana dynamického meshe odstranila konkrétní pád při
neplatném triangle indexu a stale collision cook nyní spouští opakovaný cook.

To však stále není důkaz vydatelné nové verze. Nejnovější omezený běh sice
skončil bez `Critical error`, `Assertion failed`, `Fatal error` nebo GPU
chyb, ale runtime manager hlásil `WorldCurrent=0` a
`worldMeshPlayableCurrent=0`. PCG nevytvořil žádný manager ani instanci a
čerstvý screenshot ukázal téměř plochý oranžový povrch proti černému nebi bez
ověřitelných foliage instancí. Proto je release gate stále otevřený.

## Legenda stavu

| Značka | Význam |
| --- | --- |
| ✅ Ověřeno | Reprodukovatelný důkaz splnil danou bránu. |
| 🟦 Implementováno, neověřeno | Kód nebo asset existuje, ale chybí cílový runtime či vizuální důkaz. |
| 🟠 Rozpracováno | Probíhá implementace, oprava nebo integrace. |
| ⚪ Pouze roadmapa | Požadavek je naplánovaný, ale není vydávanou funkcí. |
| ⛔ Blokováno | Brána čeká na závislý důkaz nebo rozhodnutí. |

## Roadmapa a stav bran

| ID | Oblast | Stav | Co už je doloženo | Co ještě chybí |
| --- | --- | --- | --- | --- |
| R0 | První generování a opakovaný Play | 🟠 Rozpracováno | Bootstrap pivotu, texturovací fronta, dva dynamické cykly a fail-closed async shutdown | Skutečný PIE Play/Stop/Play, reset, pohyb, collision-ready a PCG handoff |
| R1 | Jednoduchý editovatelný sample | 🟠 Rozpracováno | Replacement sloty, fake surface inputs a builder | Jeden centrální drag-and-drop workflow a krátký návod |
| R2 | Formáty, projekce, tiling a noise | ⚪ Pouze roadmapa | Požadavek je specifikovaný | Ověřená importní matice PNG/JPEG/EXR/TIFF, projekce, opakování, švy a close-up QA |
| R3 | Soulad sphere map ↔ ground height | ⚪ Pouze roadmapa | Kontrakt pro shodné hory, krátery a hřebeny | Landmark test od orbity k povrchu |
| R4 | LOD, streaming, více planet a lighting override | 🟠 Důkaz otevřený | Guard proti neplatnému triangle read, fail-closed task a retry stale collision cooku | `WorldCurrent=1`, playable collision, smooth orbit-to-ground přechod a stress evidence |
| R5 | Atmosféra, mraky a plynné planety | 🟦 Částečné stavební kameny | Water/wave/cloud komponenty a weather směr | Integrovaný vizuální a cooked průlet, včetně vrstev a pohybu mraků |
| R6 | Voda, vztlak a wake/brázda | ⚪ Pouze roadmapa | Wave source, výška vlny a normála | Sampler, buoyancy, lokální ripple/wake/foam a gameplay test |
| R7 | Sníh, písek, štěrk, láva a stopy | ⚪ Pouze roadmapa | Navržený lokální interaction směr | Budgetované buffery/RVT/Niagara a ověřené stopy či pohyblivá láva |
| R8 | Foliage a bohatý biome katalog | 🟦 Scaffold, runtime neověřen | Fab-safe balíčky, 8 surface planet a role profily | Skutečné PCG instance, doplněné biomy, screenshoty a realistický visual review |
| R9 | Packaging a vydání | ⛔ Čeká na R0/R4/R8 | Základní dependency a licence hranice | Cooked demo, finální QA, dokumentace a release evidence |

## Ověřené důkazy tohoto snapshotu

### UE 5.8 runtime a stabilita

- Cílový editorový build `PlanetopiaEditor Win64 Development` pro UE 5.8
  prošel.
- Cílený RHI běh cílové plugin-only mapy skončil s exit code 0 a bez
  `Critical error`, `Assertion failed`, `Fatal error`, `GPU crashed`,
  `Device removed` nebo `Unhandled Exception`.
- Dva po sobě jdoucí RHI smoke běhy po dynamickém meshovém guardu prošly bez
  původního pádu na `Indices[-1]` v `GetLocalLocation`.
- Stale collision completion už neuvolní stav bez další práce: telemetry
  potvrdila `AsyncCookRetryAfterStale` a druhý cook dokončil snapshot pro
  generaci 2.

### Co je stále otevřené

- Retry collision cooku sice doběhl, ale runtime manager stále nepromítl
  výsledek jako `WorldCurrent=1`; současný důkaz proto nepokrývá gameplay
  collision.
- PCG snapshot uvedl `PCGCurrent=1`, ale aktivní/total manager i generation
  group zůstaly na nule. Log obsahoval `No Spatial data shape was provided
  for sampling`.
- Automatický běh neprokázal skutečné kliknutí Play → Stop → Play, reset,
  traversal po povrchu ani stabilní přechod všech LOD úrovní.
- Čerstvý screenshot cílové mapy je téměř plochý oranžový povrch proti černému
  nebi a neprokazuje viditelné foliage. Starší screenshot navíc nesl
  `LIGHTING NEEDS TO BE REBUILT`.

## Fab-safe obsah a licence

Veřejný sample bude používat pouze vlastní jednoduché Blender mockupy a
jednobarevné fake/replacement povrchové textury. Demo projekt může sloužit jako
interní vizuální reference, ale cizí photorealistic foliage, povrchy ani jiné
asset balíčky se do pluginu ani do tohoto veřejného repozitáře nekopírují.

Aktuální scaffold obsahuje 63 flat texture swatchů; každý prošel základní QA a
je 16×16 px. Nejde o finální AAA art a zákazník je má moci nahradit vlastními
texturami a assety.

## Co má zákazník očekávat po dokončení

Po uzavření příslušných bran má nová verze směřovat k tomu, aby uživatel mohl:

1. v jednom centrálním nastavení přetáhnout vlastní base-color, normal, height,
   roughness, cloud nebo atmosphere vstup;
2. nastavit projekci, rozsah, opakování, měřítko a řízený noise bez ručního
   přepisování mnoha generovaných assetů;
3. použít mapu celého glóbu tak, aby barvy i výškové landmarky navazovaly při
   přiblížení k povrchu;
4. vyměnit stromy, keře, trávy, skály a další role přes profilové sloty;
5. používat atmosféru, mraky, haze, více planet a vlastní lighting override;
6. později využít vztlak, wake/brázdu, pěnu, stopy ve sněhu/písku/štěrku a
   pohyblivou lávu v rozpočtovaných lokálních vrstvách.

Tento seznam je cílový produktový kontrakt, nikoli tvrzení, že všechny body už
fungují v aktuálním buildu.

## Nejbližší důkazní kroky

1. uzavřít collision-generation handoff tak, aby aktuální committed povrch
   dal `WorldCurrent=1` a `worldMeshPlayableCurrent=1`;
2. zopakovat skutečný Editor PIE Play/Stop/Play, reset a pohyb;
3. opravit PCG spatial-shape/manager handoff a doložit skutečné instance;
4. opravit lighting/sky, pořídit orbit/approach/ground screenshoty a ověřit
   smooth LOD/streaming;
5. teprve potom uzavírat packaging a další funkce vody, stop a atmosféry.

## Release rozhodnutí

**Nevydávat jako hotovou novou verzi.** Veřejný report bude aktualizován podle
nových důkazů, ne podle samotného počtu změn. Stará v3.1.4 zůstává mimo podporu;
čeká se na samostatnou novou UE 5.8 verzi.

Strojově čitelná data: [progress.json](progress.json) a
[progress-history.json](progress-history.json).

## English fallback

### Development status

Planetopia is the internal name of the new plugin version under development.
There is no public installer or distributable demo content here. The old
**Planetopia v3.1.4 for Unreal Engine 5.4 is frozen and unsupported**; it is
not part of this release effort and is not being repaired. Customers should
wait for the separate Unreal Engine 5.8 version.

**Current verdict: 🟠 In progress – not release-ready.** The new branch has a
plugin-only map, Fab-safe self-authored mockups, flat replaceable surface
swatches and replacement slots. UE 5.8 RHI runs have passed bootstrap,
texturing queue, dynamic mesh work and repeated generation cycles. A dynamic
mesh guard removed the reproduced invalid-triangle crash, and a stale
collision cook now schedules a retry.

This is not yet a shippable release proof. The latest bounded RHI run ended
without critical/assert/fatal/GPU errors, but the runtime manager still
reported `WorldCurrent=0` and `worldMeshPlayableCurrent=0`. PCG created no
manager or instance and reported that no spatial data shape was available for
sampling. The fresh screenshot still showed an almost flat orange surface
against a black sky with no verifiable foliage. The release gates remain open.

### Roadmap

| ID | Area | Status | Remaining acceptance |
| --- | --- | --- | --- |
| R0 | First generation and repeat Play | 🟠 In progress | Real PIE Play/Stop/Play, reset, movement, collision-ready and PCG handoff |
| R1 | Editable sample | 🟠 In progress | One clear drag-and-drop workflow for textures, height, atmosphere and foliage slots |
| R2 | Formats, projection, tiling and noise | ⚪ Planned | Verified PNG/JPEG/EXR/TIFF import and close-up seam/noise QA |
| R3 | Sphere map to ground-height alignment | ⚪ Planned | Landmark regression from orbit to ground |
| R4 | LOD, streaming, multiple planets and lighting overrides | 🟠 Evidence open | `WorldCurrent=1`, playable collision, smooth transitions and stress evidence |
| R5 | Atmospheres, clouds and gas planets | 🟦 Partial building blocks | Integrated visual/cooked flight-through proof |
| R6 | Water buoyancy and wake | ⚪ Planned | Buoyancy sampler, ripples, wake/foam and gameplay proof |
| R7 | Snow, sand, gravel, lava and tracks | ⚪ Planned | Budgeted local layers and verified moving interactions |
| R8 | Foliage and biome catalog | 🟦 Scaffold, runtime unverified | Real PCG instances, remaining biomes and visual review |
| R9 | Packaging and release | ⛔ Waiting for R0/R4/R8 | Cooked demo, final QA, documentation and release evidence |

### Evidence boundary and licensing

The public sample will contain only self-authored simple Blender mockups and
flat fake/replacement textures. Demo-project photorealistic foliage and
surface assets may be used for internal visual reference, but assets with
unclear or restricted redistribution rights will not be shipped in the plugin
or copied into this public repository. The current 63 flat 16×16 swatches are
QA-checked placeholders, not final AAA art.

### Customer-facing expectation

The target is a single, understandable profile where users can replace
surface, height, atmosphere and foliage inputs; control projection, tiling and
noise; align a whole-sphere map with close ground detail; and later use
atmospheres, multiple planets, lighting overrides, buoyancy, wakes, tracks and
lava. These are release goals, not claims that every feature is already
working.

**Release decision: do not present the current build as finished.** The public
report will change only when new runtime, visual and packaging evidence closes
the relevant gates.

## Public report boundary

This page is a development report, not a download. It deliberately omits
private source paths, local logs, generated Unreal binary assets and restricted
demo content.
<!-- PLANETOPIA_IMPLEMENTATION_PROGRESS_END -->
