from __future__ import annotations

import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import generate_jarvis_capability_map as generator


class CapabilityMapGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(__file__).resolve().parents[1]
        self.definition = generator.read_json(self.root / "apps/jarvis/capability-map.json")

    def test_baseline_has_all_four_public_states(self) -> None:
        snapshot = generator.build_snapshot(self.definition, None)
        self.assertEqual(snapshot["node_count"], 12)
        self.assertEqual(snapshot["status_counts"], {
            "TESTED": 1,
            "TESTING": 4,
            "NOT_TESTED": 6,
            "NOT_IMPLEMENTED": 1,
        })

    def test_live_inventory_recomputes_node_status(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "inventory.json"
            path.write_text(
                json.dumps({
                    "source_revision": "live-revision",
                    "scenarios": [
                        {"id": f"F{number}", "block": "F00-F09", "status": "PASS"}
                        for number in range(10)
                    ] + [
                        {"id": f"F{number}", "block": "F10-F19", "status": "NOT_RUN"}
                        for number in range(10, 20)
                    ],
                }),
                encoding="utf-8",
            )
            snapshot = generator.build_snapshot(self.definition, path)
        core = next(node for node in snapshot["nodes"] if node["id"] == "core-runtime")
        self.assertEqual(core["status"], "TESTING")
        self.assertEqual(core["passed_scenarios"], 10)
        self.assertTrue(snapshot["live_inventory_used"])
        self.assertEqual(snapshot["source_revision"], "live-revision")

    def test_svg_is_well_formed_and_deterministic(self) -> None:
        snapshot = generator.build_snapshot(self.definition, None)
        first = generator.render_svg(self.definition, snapshot, "cs")
        second = generator.render_svg(self.definition, snapshot, "cs")
        english = generator.render_svg(self.definition, snapshot, "en")
        self.assertEqual(first, second)
        ET.fromstring(first)
        ET.fromstring(english)
        self.assertIn("MAPA SCHOPNOSTÍ", first)
        self.assertIn("Běhové jádro", first)
        self.assertIn("Vytváření 3D a CAD", first)
        self.assertIn("seznam schválených poskytovatelů", first)
        self.assertNotIn("Core runtime", first)
        self.assertNotIn("documented-basel", first)
        self.assertIn("CAPABILITY CONSTELLATION", english)
        self.assertIn("core and authority", english)
        self.assertNotIn("jádro a autorita", english)
        self.assertIn("TESTED", english)

    def test_czech_labels_are_localized_and_english_labels_remain_separate(self) -> None:
        expected_czech = {
            "Běhové jádro",
            "Zásady a bezpečnost",
            "Vývojový agent",
            "Běh modelu",
            "Obnova a provoz",
            "Pracovní prostor a Git",
            "Ovládání UI a plochy",
            "Pověření a poskytovatelé",
            "Instalace a migrace",
            "Důkazy a uzavření",
            "Doplňky a rozšíření",
            "Vytváření 3D a CAD",
        }
        self.assertEqual({node["label_cs"] for node in self.definition["nodes"]}, expected_czech)
        self.assertTrue(all(node["label_en"] for node in self.definition["nodes"]))
        for node in self.definition["nodes"]:
            label = node["label_cs"]
            size = generator.fit_svg_font_size(label, generator.NODE_TEXT_MAX_WIDTH, 19, 15)
            self.assertLessEqual(generator.estimate_svg_text_width(label, size), generator.NODE_TEXT_MAX_WIDTH + 0.01)
            subtitle_lines = generator.wrap_svg_text(node["subtitle_cs"], generator.NODE_TEXT_MAX_WIDTH, 12)
            self.assertLessEqual(len(subtitle_lines), 2, node["id"])
        for status in generator.STATUS_LABELS.values():
            width, font_size, _ = generator.status_badge_layout(status, "0/160")
            self.assertLessEqual(
                generator.estimate_svg_text_width(status, font_size, generator.STATUS_BADGE_LETTER_SPACING),
                width - 24 + 0.01,
                status,
            )

        nodes_per_layer = {}
        for node in self.definition["nodes"]:
            nodes_per_layer[node["layer"]] = nodes_per_layer.get(node["layer"], 0) + 1
        max_card_bottom = generator.NODE_START_Y + (max(nodes_per_layer.values()) - 1) * generator.NODE_STEP_Y + generator.NODE_HEIGHT
        self.assertLess(max_card_bottom + 6, generator.LEGEND_Y)


if __name__ == "__main__":
    unittest.main()
