#!/usr/bin/env python3
"""Render the Jarvis/Maunder capability constellation without CI.

The script consumes the versioned capability definition and, optionally, the
sanitised inventory emitted by ``scenario_pyramid_runtime.py`` in CPM.  It
produces a deterministic status snapshot, a dark sci-fi SVG and a generated
README section.  No model, network call or GitHub Action is used.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


STATUS_ORDER = ("TESTED", "TESTING", "NOT_TESTED", "NOT_IMPLEMENTED")
STATUS_LABELS = {
    "TESTED": "OVĚŘENO",
    "TESTING": "TESTUJE SE",
    "NOT_TESTED": "NEOTESTOVÁNO",
    "NOT_IMPLEMENTED": "NEIMPLEMENTOVÁNO",
}
STATUS_LABELS_EN = {
    "TESTED": "TESTED",
    "TESTING": "TESTING",
    "NOT_TESTED": "NOT TESTED",
    "NOT_IMPLEMENTED": "NOT IMPLEMENTED",
}
STATUS_TABLE_LABELS_CS = {
    "TESTED": "Ověřeno",
    "TESTING": "Testuje se",
    "NOT_TESTED": "Neotestováno",
    "NOT_IMPLEMENTED": "Neimplementováno",
}
STATUS_COLORS = {
    "TESTED": "#35f2b4",
    "TESTING": "#ffc857",
    "NOT_TESTED": "#6ca8ff",
    "NOT_IMPLEMENTED": "#ff5f8f",
}
NODE_WIDTH = 300
NODE_HEIGHT = 118
NODE_TEXT_X_OFFSET = 43
NODE_TEXT_MAX_WIDTH = NODE_WIDTH - NODE_TEXT_X_OFFSET - 22
SUBTITLE_LINE_HEIGHT = 14
STATUS_BADGE_HEIGHT = 22
STATUS_BADGE_GAP = 12
STATUS_BADGE_FONT_SIZE = 11
STATUS_BADGE_LETTER_SPACING = 1
RANGE_RE = re.compile(r"^F(\d+)[-\u2013]F(\d+)$")
ID_RE = re.compile(r"^F\d+$")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def expand_selector(selector: str) -> set[str]:
    selector = selector.upper().strip()
    match = RANGE_RE.fullmatch(selector)
    if match:
        start, end = (int(value) for value in match.groups())
        if end < start:
            raise ValueError(f"Neplatný rozsah: {selector}")
        return {f"F{number}" for number in range(start, end + 1)}
    if ID_RE.fullmatch(selector):
        return {selector}
    raise ValueError(f"Neplatný scénářový selektor: {selector}")


def selector_ids(selectors: list[str]) -> set[str]:
    result: set[str] = set()
    for selector in selectors:
        result.update(expand_selector(selector))
    return result


def load_inventory(path: Path | None) -> tuple[dict[str, dict[str, Any]], str, bool]:
    if path is None:
        return {}, "documented-baseline", False
    payload = read_json(path)
    scenarios = payload.get("scenarios")
    if not isinstance(scenarios, list):
        raise ValueError("Inventory nemá pole scenarios")
    result = {str(item["id"]).upper(): item for item in scenarios if item.get("id")}
    if not result:
        raise ValueError("Inventory je prázdný")
    return result, str(payload.get("source_revision", "unknown")), True


def summarise_node(node: dict[str, Any], inventory: dict[str, dict[str, Any]], live: bool) -> dict[str, Any]:
    blocks = [str(value) for value in node.get("scenario_blocks", [])]
    planned_ids = selector_ids(blocks)
    implementation = node.get("implementation", "implemented")
    baseline_ids = selector_ids([str(value) for value in node.get("baseline_scenarios", [])])
    if implementation == "architecture-only":
        status = "NOT_IMPLEMENTED"
        counts = Counter()
        selected = {}
    elif live:
        selected = {scenario_id: inventory[scenario_id] for scenario_id in planned_ids if scenario_id in inventory}
        counts = Counter(str(item.get("status", "UNKNOWN")).upper() for item in selected.values())
        if not selected:
            status = "NOT_TESTED"
        elif all(value == "PASS" for value in (str(item.get("status", "UNKNOWN")).upper() for item in selected.values())):
            status = "TESTED"
        elif any(value in {"PASS", "FAIL", "UNKNOWN", "DIRTY"} for value in counts):
            status = "TESTING"
        else:
            status = "NOT_TESTED"
    else:
        selected = {scenario_id: {"status": "PASS"} for scenario_id in baseline_ids}
        counts = Counter(item["status"] for item in selected.values())
        status = "TESTED" if planned_ids and planned_ids.issubset(baseline_ids) else ("TESTING" if baseline_ids else "NOT_TESTED")
    return {
        "id": node["id"],
        "layer": node["layer"],
        "order": int(node.get("order", 0)),
        "label_cs": node["label_cs"],
        "label_en": node.get("label_en", node["label_cs"]),
        "subtitle_cs": node.get("subtitle_cs", ""),
        "subtitle_en": node.get("subtitle_en", node.get("subtitle_cs", "")),
        "dependencies": list(node.get("dependencies", [])),
        "scenario_blocks": blocks,
        "implementation": implementation,
        "status": status,
        "status_label_cs": STATUS_LABELS[status],
        "status_color": STATUS_COLORS[status],
        "planned_scenarios": len(planned_ids),
        "observed_scenarios": len(selected),
        "passed_scenarios": counts.get("PASS", 0),
        "attention_scenarios": sum(counts.get(key, 0) for key in ("FAIL", "UNKNOWN", "DIRTY")),
        "baseline_note_cs": node.get("baseline_note_cs", ""),
    }


def build_snapshot(definition: dict[str, Any], inventory_path: Path | None) -> dict[str, Any]:
    inventory, source_revision, live = load_inventory(inventory_path)
    nodes = [summarise_node(node, inventory, live) for node in definition["nodes"]]
    counts = Counter(node["status"] for node in nodes)
    return {
        "schema": "maunder.jarvis.capability-status.v1",
        "source_definition": "apps/jarvis/capability-map.json",
        "source_revision": source_revision,
        "live_inventory_used": live,
        "status_counts": {status: counts.get(status, 0) for status in STATUS_ORDER},
        "node_count": len(nodes),
        "nodes": nodes,
        "note_cs": (
            "Stav TESTED je podložený důkazy a neznamená přijetí vydání."
            if live
            else "Výchozí mapa používá pouze očištěný výchozí stav z dokumentované evidence; pro živý stav předejte seznam stavů ze scénářového běhu."
        ),
    }


def xml_text(value: Any) -> str:
    return html.escape(str(value), quote=True)


def estimate_svg_text_width(text: str, font_size: float, letter_spacing: float = 0.0) -> float:
    """Estimate a conservative SVG text width for deterministic layout decisions.

    The map is rendered by the browser, whose exact font metrics are not
    available to this provider-free generator.  A deliberately conservative
    estimate prevents localized labels from colliding with the card border or
    the coverage counter while keeping the SVG portable.
    """

    narrow = set(" ilI.,:;|'·")
    wide = set("MW@#%&")
    width = 0.0
    for character in text:
        factor = 0.34 if character in narrow else 0.86 if character in wide else 0.64
        width += font_size * factor
    return width + max(0, len(text) - 1) * letter_spacing


def wrap_svg_text(text: str, max_width: float, font_size: float) -> list[str]:
    """Wrap a short UI label at word boundaries for an SVG text block."""

    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if current and estimate_svg_text_width(candidate, font_size) > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def fit_svg_font_size(text: str, max_width: float, preferred: float, minimum: float) -> float:
    """Shrink a single-line label only as much as needed to fit its card."""

    measured = estimate_svg_text_width(text, preferred)
    if measured <= max_width:
        return preferred
    fitted = max(minimum, preferred * max_width / measured)
    if estimate_svg_text_width(text, fitted) > max_width + 0.01:
        raise ValueError(f"SVG label se nevejde do karty: {text}")
    return fitted


def status_badge_layout(status: str, coverage: str) -> tuple[float, float, float]:
    """Return badge width, text font size and coverage estimate for one card."""

    coverage_width = estimate_svg_text_width(f"{coverage} QA", 13)
    available_width = NODE_WIDTH - NODE_TEXT_X_OFFSET - 22 - coverage_width - STATUS_BADGE_GAP
    status_width = estimate_svg_text_width(
        status,
        STATUS_BADGE_FONT_SIZE,
        STATUS_BADGE_LETTER_SPACING,
    )
    badge_width = min(max(120.0, status_width + 24.0), available_width)
    text_font_size = STATUS_BADGE_FONT_SIZE
    required_width = status_width + 24.0
    if required_width > available_width:
        text_font_size = max(8.0, STATUS_BADGE_FONT_SIZE * (available_width - 24.0) / max(status_width, 1.0))
        badge_width = available_width
    return badge_width, text_font_size, coverage_width


def subtitle_svg(text: str, x: int, y: int) -> str:
    """Render a subtitle as one or two bounded SVG text lines."""

    font_size = 12.0
    lines: list[str] = []
    while font_size >= 9.0:
        lines = wrap_svg_text(text, NODE_TEXT_MAX_WIDTH, font_size)
        if len(lines) <= 2:
            break
        font_size -= 0.5
    if len(lines) > 2:
        raise ValueError(f"SVG podnadpis se nevejde do dvou řádků: {text}")
    if len(lines) == 1:
        return (
            f'<text x="{x}" y="{y}" fill="#9fb5d8" font-family="Segoe UI,Arial,sans-serif" '
            f'font-size="{font_size:g}">{xml_text(lines[0])}</text>'
        )
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if index == 0 else SUBTITLE_LINE_HEIGHT}">{xml_text(line)}</tspan>'
        for index, line in enumerate(lines[:2])
    )
    return (
        f'<text x="{x}" y="{y}" fill="#9fb5d8" font-family="Segoe UI,Arial,sans-serif" '
        f'font-size="{font_size:g}">{spans}</text>'
    )


def render_svg(definition: dict[str, Any], snapshot: dict[str, Any], language: str = "cs") -> str:
    english = language.lower() == "en"
    layers = sorted(definition["layers"], key=lambda item: int(item.get("order", 0)))
    layer_lookup = {layer["id"]: layer for layer in layers}
    nodes = sorted(snapshot["nodes"], key=lambda item: (int(layer_lookup[item["layer"]].get("order", 0)), item["order"]))
    by_id = {node["id"]: node for node in nodes}
    positions: dict[str, tuple[int, int]] = {}
    column_x = {layer["id"]: 80 + index * 380 for index, layer in enumerate(layers)}
    per_layer: dict[str, list[dict[str, Any]]] = {layer["id"]: [] for layer in layers}
    for node in nodes:
        per_layer.setdefault(node["layer"], []).append(node)
    for layer in layers:
        for index, node in enumerate(per_layer.get(layer["id"], [])):
            positions[node["id"]] = (column_x[layer["id"]], 230 + index * 145)

    edges: list[str] = []
    for node in nodes:
        tx, ty = positions[node["id"]]
        for dependency in node["dependencies"]:
            if dependency not in positions:
                continue
            sx, sy = positions[dependency]
            start_x, end_x = sx + 300, tx
            mid = (start_x + end_x) // 2
            edges.append(
                f'<path class="edge" d="M {start_x} {sy + 50} C {mid} {sy + 50}, {mid} {ty + 50}, {end_x} {ty + 50}" marker-end="url(#arrow)" />'
            )

    summary = snapshot["status_counts"]
    total = snapshot["node_count"]
    live = ("LIVE INVENTORY" if snapshot["live_inventory_used"] else "DOCUMENTED BASELINE") if english else ("ŽIVÝ SEZNAM STAVŮ" if snapshot["live_inventory_used"] else "DOKUMENTOVANÝ VÝCHOZÍ STAV")
    title = "Maunder Jarvis capability constellation" if english else "Mapa schopností Maunder Jarvis"
    description = (
        "Sci-fi dependency map of Jarvis capabilities with tested, testing, not tested and not implemented states."
        if english
        else "Sci-fi mapa závislostí schopností Jarvise se stavy ověřeno, testuje se, neotestováno a neimplementováno."
    )
    heading = "CAPABILITY CONSTELLATION" if english else "MAPA SCHOPNOSTÍ"
    node_caption = "CAPABILITY NODES" if english else "UZLŮ SCHOPNOSTÍ"
    tested_caption = "TESTED" if english else "OVĚŘENO"
    testing_caption = "TESTING" if english else "TESTUJE SE"
    source_revision = snapshot["source_revision"][:16]
    if not english and snapshot["source_revision"] == "documented-baseline":
        source_revision = "dokumentovaný-výchozí-stav"
    svg: list[str] = [
        '<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 1580 1000" width="1580" height="1000">',
        f'<title id="title">{xml_text(title)}</title>',
        f'<desc id="desc">{xml_text(description)}</desc>',
        """<defs>
          <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050b1e"/><stop offset="0.5" stop-color="#101a38"/><stop offset="1" stop-color="#070b18"/></linearGradient>
          <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#172955" stop-opacity=".95"/><stop offset="1" stop-color="#0b1430" stop-opacity=".96"/></linearGradient>
          <filter id="glow"><feGaussianBlur stdDeviation="4" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#6ca8ff" opacity=".8"/></marker>
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#7da4e8" stroke-opacity=".08"/></pattern>
        </defs>""",
        '<rect width="1580" height="1000" fill="url(#bg)"/>',
        '<rect x="20" y="20" width="1540" height="960" rx="24" fill="url(#grid)" stroke="#31568f" stroke-opacity=".7"/>',
        '<circle cx="1470" cy="80" r="240" fill="#1d62a8" opacity=".08" filter="url(#glow)"/>',
        '<text x="70" y="78" fill="#8fbaff" font-family="Segoe UI,Arial,sans-serif" font-size="18" letter-spacing="4">MAUNDER / JARVIS</text>',
        f'<text x="70" y="125" fill="#f4f8ff" font-family="Segoe UI,Arial,sans-serif" font-size="38" font-weight="700" letter-spacing="2">{heading}</text>',
        f'<text x="70" y="157" fill="#93a9ce" font-family="Segoe UI,Arial,sans-serif" font-size="16">{"DEPENDENCY GRAPH" if english else "GRAF ZÁVISLOSTÍ"} · {xml_text(live)} · {xml_text(source_revision)}</text>',
        f'<text x="1390" y="90" fill="#d9e7ff" font-family="Segoe UI,Arial,sans-serif" font-size="18" text-anchor="end">{total} {node_caption}</text>',
        f'<text x="1390" y="120" fill="#35f2b4" font-family="Segoe UI,Arial,sans-serif" font-size="17" text-anchor="end">{summary["TESTED"]} {tested_caption}</text>',
        f'<text x="1390" y="148" fill="#ffc857" font-family="Segoe UI,Arial,sans-serif" font-size="17" text-anchor="end">{summary["TESTING"]} {testing_caption}</text>',
        '<line x1="70" y1="180" x2="1510" y2="180" stroke="#4676bd" stroke-opacity=".5"/>',
    ]
    for layer in layers:
        x = column_x[layer["id"]]
        svg.extend([
            f'<text x="{x}" y="210" fill="#a9c8ff" font-family="Segoe UI,Arial,sans-serif" font-size="16" font-weight="700" letter-spacing="2">{xml_text(layer.get("label_en", layer["label"]) if english else layer["label"])}</text>',
            f'<text x="{x}" y="232" fill="#617aa5" font-family="Segoe UI,Arial,sans-serif" font-size="12">{xml_text(layer.get("subtitle_en", layer["subtitle"]) if english else layer["subtitle"])}</text>',
        ])
    svg.extend(edges)
    for node in nodes:
        x, y = positions[node["id"]]
        color = node["status_color"]
        label_text = node["label_en"] if english else node["label_cs"]
        label = xml_text(label_text)
        label_font_size = fit_svg_font_size(label_text, NODE_TEXT_MAX_WIDTH, 19, 15)
        subtitle = node["subtitle_en"] if english else node["subtitle_cs"]
        status_label = STATUS_LABELS_EN[node["status"]] if english else node["status_label_cs"]
        status = xml_text(status_label)
        coverage = f'{node["passed_scenarios"]}/{node["planned_scenarios"]}'
        badge_width, badge_font_size, _coverage_width = status_badge_layout(status_label, coverage)
        svg.extend([
            f'<g class="node" id="node-{xml_text(node["id"])}">',
            f'<rect x="{x}" y="{y}" width="{NODE_WIDTH}" height="{NODE_HEIGHT}" rx="14" fill="url(#panel)" stroke="{color}" stroke-width="2" stroke-opacity=".9"/>',
            f'<rect x="{x + 18}" y="{y + 17}" width="8" height="70" rx="4" fill="{color}" filter="url(#glow)"/>',
            f'<text x="{x + NODE_TEXT_X_OFFSET}" y="{y + 33}" fill="#f4f8ff" font-family="Segoe UI,Arial,sans-serif" font-size="{label_font_size:g}" font-weight="700">{label}</text>',
            subtitle_svg(subtitle, x + NODE_TEXT_X_OFFSET, y + 56),
            f'<rect x="{x + NODE_TEXT_X_OFFSET}" y="{y + 86}" width="{badge_width:g}" height="{STATUS_BADGE_HEIGHT}" rx="11" fill="{color}" fill-opacity=".14" stroke="{color}" stroke-opacity=".55"/>',
            f'<text x="{x + NODE_TEXT_X_OFFSET + badge_width / 2:g}" y="{y + 101}" fill="{color}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="{badge_font_size:g}" font-weight="700" letter-spacing="{STATUS_BADGE_LETTER_SPACING}">{status}</text>',
            f'<text x="{x + NODE_WIDTH - 22}" y="{y + 101}" fill="#d9e7ff" text-anchor="end" font-family="Consolas,monospace" font-size="13">{xml_text(coverage)} QA</text>',
            '</g>',
        ])
    legend_y = 930
    legend_x = 80
    svg.append(f'<text x="{legend_x}" y="{legend_y - 24}" fill="#728ebd" font-family="Segoe UI,Arial,sans-serif" font-size="12" letter-spacing="2">{"STATUS LEGEND" if english else "LEGENDA STAVŮ"}</text>')
    for index, status in enumerate(STATUS_ORDER):
        x = legend_x + index * 260
        color = STATUS_COLORS[status]
        svg.extend([
            f'<circle cx="{x + 7}" cy="{legend_y}" r="6" fill="{color}" filter="url(#glow)"/>',
            f'<text x="{x + 23}" y="{legend_y + 5}" fill="#cfe0ff" font-family="Segoe UI,Arial,sans-serif" font-size="13">{xml_text(STATUS_LABELS_EN[status] if english else STATUS_LABELS[status])}</text>',
        ])
    svg.append('</svg>')
    return "\n".join(svg) + "\n"


def render_readme_section(snapshot: dict[str, Any]) -> str:
    counts = snapshot["status_counts"]
    live = "živého seznamu stavů scénářů" if snapshot["live_inventory_used"] else "doloženého výchozího stavu"
    source_revision = snapshot["source_revision"][:16]
    if snapshot["source_revision"] == "documented-baseline":
        source_revision = "dokumentovaný-výchozí-stav"
    rows = "\n".join(
        f"| {STATUS_TABLE_LABELS_CS[status]} | {counts[status]} |"
        for status in STATUS_ORDER
    )
    return f"""<!-- JARVIS_CAPABILITY_MAP_BEGIN -->
## Sci-fi mapa schopností

![Mapa schopností Maunder Jarvis](visuals/capability-map.svg)

Mapa je graf schopností a závislostí, ne seznam intervalů scénářů. Každý uzel
ukazuje implementační stav, QA stav a počet přidružených scénářů; šipky vedou od
nutných předpokladů k navazující schopnosti.

**Snímek:** {live} · zdrojová revize `{source_revision}` ·
{snapshot["node_count"]} uzlů schopností

| Stav | Uzly |
| --- | ---: |
{rows}

`TESTED` znamená PASS podložený důkazy, nikoli přijetí vydání. `TESTING` je
částečně doložená nebo právě ověřovaná schopnost. `NOT_TESTED` nemá aktuální
důkaz QA a `NOT_IMPLEMENTED` zůstává pouze architekturou. Graf záměrně ukazuje
i závislosti na schopnostech, které ještě nejsou implementované.

### Aktualizace bez GitHub Actions

Mapa se aktualizuje místně ze scénářového běhu. Jedním příkazem se z kořene
tohoto repozitáře načte očištěný seznam stavů z CPM (bez zadání, tajemství a
surových výstupů) a znovu se vytvoří graf:

```powershell
python tools/update_jarvis_capability_map.py --cpm-root Z:\\Codex\\CPM --state Z:\\Codex\\CPM\\qa\\scenario-state.json
python tools/generate_jarvis_capability_map.py --check
```

Generátor je deterministický a mění pouze `capability-status.json`, českou a
anglickou SVG mapu a tuto označenou část dokumentace. Neexistuje automatizace,
placený spouštěč ani síťové volání; změna se publikuje běžným chráněným PR.
<!-- JARVIS_CAPABILITY_MAP_END -->"""


def render_readme_section_en(snapshot: dict[str, Any]) -> str:
    counts = snapshot["status_counts"]
    live = "live scenario inventory" if snapshot["live_inventory_used"] else "documented baseline"
    rows = "\n".join(
        f"| {status.replace('_', ' ').title()} | {counts[status]} |"
        for status in STATUS_ORDER
    )
    return f"""<!-- JARVIS_CAPABILITY_MAP_BEGIN -->
## Capability constellation

![Maunder Jarvis capability constellation](visuals/capability-map.en.svg)

This is a dependency graph of capabilities, not a list of scenario ranges.
Each node shows implementation state, QA state and associated scenario
coverage; arrows point from prerequisites to dependent capabilities.

**Snapshot:** {live} · source revision `{snapshot["source_revision"][:16]}` ·
{snapshot["node_count"]} capability nodes

| State | Nodes |
| --- | ---: |
{rows}

`TESTED` means evidence-bound PASS, not release acceptance. `TESTING` means
that part of the capability is evidenced or currently being verified.
`NOT_TESTED` has no current QA evidence. `NOT_IMPLEMENTED` remains
architecture-only. The graph intentionally includes future dependencies.

### Updating without GitHub Actions

Refresh the map locally from the scenario runtime. From this repository, run
one command with a local CPM checkout and its sanitised scenario ledger:

```powershell
python tools/update_jarvis_capability_map.py --cpm-root Z:\\Codex\\CPM --state Z:\\Codex\\CPM\\qa\\scenario-state.json
python tools/generate_jarvis_capability_map.py --check
```

The bridge transfers only machine-readable inventory: no prompts, secrets or
raw model output. The generator is deterministic and changes only
`capability-status.json`, both language SVG maps and the marked README
sections. There is no workflow, paid runner or network call; publish changes
through a normal protected PR.
<!-- JARVIS_CAPABILITY_MAP_END -->"""


def update_readme(path: Path, section: str) -> None:
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    pattern = re.compile(r"<!-- JARVIS_CAPABILITY_MAP_BEGIN -->.*?<!-- JARVIS_CAPABILITY_MAP_END -->", re.S)
    if pattern.search(original):
        updated = pattern.sub(lambda _match: section, original)
    else:
        marker = "## Co se připravuje"
        updated = original.replace(marker, section + "\n\n" + marker, 1) if marker in original else original.rstrip() + "\n\n" + section + "\n"
    path.write_text(updated.rstrip() + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--map-definition", default="apps/jarvis/capability-map.json")
    parser.add_argument("--inventory")
    parser.add_argument("--output-root", default=".")
    parser.add_argument("--check", action="store_true", help="fail if generated files differ")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.output_root).resolve()
    definition_path = Path(args.map_definition)
    if not definition_path.is_absolute():
        definition_path = root / definition_path
    inventory_path = Path(args.inventory).resolve() if args.inventory else None
    definition = read_json(definition_path)
    snapshot = build_snapshot(definition, inventory_path)
    status_path = root / "apps/jarvis/capability-status.json"
    svg_path = root / "apps/jarvis/visuals/capability-map.svg"
    svg_en_path = root / "apps/jarvis/visuals/capability-map.en.svg"
    readme_path = root / "apps/jarvis/README.md"
    readme_en_path = root / "apps/jarvis/README.en.md"
    status_text = json.dumps(snapshot, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    svg_text = render_svg(definition, snapshot, "cs")
    svg_en_text = render_svg(definition, snapshot, "en")
    current_status = status_path.read_text(encoding="utf-8") if status_path.exists() else None
    current_svg = svg_path.read_text(encoding="utf-8") if svg_path.exists() else None
    current_svg_en = svg_en_path.read_text(encoding="utf-8") if svg_en_path.exists() else None
    current_readme = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
    current_readme_en = readme_en_path.read_text(encoding="utf-8") if readme_en_path.exists() else ""
    section = render_readme_section(snapshot)
    section_en = render_readme_section_en(snapshot)
    pattern = re.compile(r"<!-- JARVIS_CAPABILITY_MAP_BEGIN -->.*?<!-- JARVIS_CAPABILITY_MAP_END -->", re.S)
    expected_readme = pattern.sub(lambda _match: section, current_readme) if pattern.search(current_readme) else current_readme
    expected_readme_en = pattern.sub(lambda _match: section_en, current_readme_en) if pattern.search(current_readme_en) else current_readme_en
    if args.check:
        if current_status != status_text or current_svg != svg_text or current_svg_en != svg_en_text or (pattern.search(current_readme) and expected_readme != current_readme) or (pattern.search(current_readme_en) and expected_readme_en != current_readme_en):
            return 1
        return 0
    write_json(status_path, snapshot)
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text(svg_text, encoding="utf-8")
    svg_en_path.write_text(svg_en_text, encoding="utf-8")
    update_readme(readme_path, section)
    update_readme(readme_en_path, section_en)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
