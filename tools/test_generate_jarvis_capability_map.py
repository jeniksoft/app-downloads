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
        self.assertIn("CAPABILITY CONSTELLATION", english)
        self.assertIn("core and authority", english)
        self.assertNotIn("jádro a autorita", english)
        self.assertIn("TESTED", english)


if __name__ == "__main__":
    unittest.main()
