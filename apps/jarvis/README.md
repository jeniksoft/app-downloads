# Projektové kódové označení: Jarvis

**Jazyk:** **Čeština (výchozí)** · [Anglická verze](README.en.md)

<p><a href="README.en.md">🇬🇧 <strong>Otevřít anglickou verzi</strong></a></p>

**Jarvis je interní kódové označení projektu ve vývoji, nikoli finální název produktu.**

Cílem je bezplatná edice **Personal 1.0.0**. Až bude připravená k veřejnému vydání, bude zde zveřejněna pod jiným produktovým názvem.

Aktuálně zde není žádný veřejný instalační balíček ke stažení. Dřívější vývojové a beta sestavení byla ze stahovacího kanálu odstraněna, protože neodpovídají cílové kvalitě a rozsahu verze 1.0.0.

## Zpětná vazba

Jarvis je veřejně sledovaný vývojový projekt. Pro zpětnou vazbu použij prosím jednu z těchto cest:

- [🐞 Nahlásit chybu](https://github.com/jeniksoft/app-downloads/issues/new?template=bug_report.yml)
- [💡 Navrhnout zlepšení](https://github.com/jeniksoft/app-downloads/issues/new?template=feature_request.yml)
- [💬 Otevřít diskuzi](https://github.com/jeniksoft/app-downloads/discussions)

Do veřejných příspěvků nevkládej hesla, tokeny, osobní údaje ani celé soukromé logy. Přikládej pouze očištěné a nezbytné informace.

## Věkové omezení (18+)

Jarvis je určen výhradně dospělým uživatelům od 18 let. Pokud ti ještě nebylo 18 let, Jarvis nepoužívej.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_BEGIN -->
## Jarvis Personal: stav implementace z roadmapy

**796 / 951 = 83.70 % s implementační evidencí**

Všechny vrcholové i vnořené řezy mají stejnou váhu. Implementační evidence počítá stavy ověřeno, implementováno bez ověření a připraveno k vydání; implementováno bez ověření není ověření ani přijetí vydání. Staré vážené evidenční přehledy se nezobrazují.

| Roadmapová skupina | S implementační evidencí / celkem |
| --- | ---: |
| Platformní základy | 55 / 55 |
| Běhové jádro | 64 / 64 |
| Personal 1.0.0 | 144 / 149 |
| Volitelné tratě | 138 / 166 |
| Tým | 70 / 70 |
| Podnik | 63 / 63 |
| Průřezové tratě schopností | 262 / 384 |

Stav: 499 ověřeno, 297 implementováno bez ověření, 0 připraveno k vydání, 4 rozpracováno, 149 pouze architektura, 2 odloženo.

Toto číslo NENÍ produkční připravenost, živé QA ani přijetí vydání. [Podrobný snímek](progress.json) může obsahovat historická QA pole s jinou metodikou.

<!-- JARVIS_IMPLEMENTATION_PROGRESS_END -->

<!-- JARVIS_CAPABILITY_MAP_BEGIN -->
## Sci-fi mapa schopností

![Mapa schopností Maunder Jarvis](visuals/capability-map.svg)

Mapa je graf schopností a závislostí, ne seznam intervalů scénářů. Každý uzel
ukazuje implementační stav, QA stav a počet přidružených scénářů; šipky vedou od
nutných předpokladů k navazující schopnosti.

**Snímek:** doloženého výchozího stavu · zdrojová revize `dokumentovaný-výchozí-stav` ·
12 uzlů schopností

| Stav | Uzly |
| --- | ---: |
| Ověřeno | 1 |
| Testuje se | 4 |
| Neotestováno | 6 |
| Neimplementováno | 1 |

`TESTED` znamená PASS podložený důkazy, nikoli přijetí vydání. `TESTING` je
částečně doložená nebo právě ověřovaná schopnost. `NOT_TESTED` nemá aktuální
důkaz QA a `NOT_IMPLEMENTED` zůstává pouze architekturou. Graf záměrně ukazuje
i závislosti na schopnostech, které ještě nejsou implementované.

### Aktualizace bez GitHub Actions

Mapa se aktualizuje místně ze scénářového běhu. Jedním příkazem se z kořene
tohoto repozitáře načte očištěný seznam stavů z CPM (bez zadání, tajemství a
surových výstupů) a znovu se vytvoří graf:

```powershell
python tools/update_jarvis_capability_map.py --cpm-root Z:\Codex\CPM --state Z:\Codex\CPM\qa\scenario-state.json
python tools/generate_jarvis_capability_map.py --check
```

Generátor je deterministický a mění pouze `capability-status.json`, českou a
anglickou SVG mapu a tuto označenou část dokumentace. Neexistuje automatizace,
placený spouštěč ani síťové volání; změna se publikuje běžným chráněným PR.
<!-- JARVIS_CAPABILITY_MAP_END -->

## Co se připravuje

Personal 1.0.0 má být osobní agent pro Windows s předností místního běhu. Může používat místní modely, modely v síti LAN i uživatelem zvoleného poskytovatele a nemá vyžadovat povinný Jeniksoftův cloud pro výpočty modelů ani Jeniksoftovy tokenové platby.

Vývoj se nyní soustředí především na spolehlivost, obnovu, bezpečnost akcí, práci s důkazy a zdroji, paměť, podporu a reprodukci chyb, řízený samovývoj, instalaci a návrat k předchozí verzi a ověření na různých skutečných počítačích.

## Dostupnost

Veřejné datum vydání zatím není stanoveno. Verze 1.0.0 bude zveřejněna až po splnění bran vydání; samotný počet implementovaných funkcí není důvodem označit sestavení za hotové.
