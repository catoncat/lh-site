import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class DigitalVisualAlignmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, "build-pages.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_homepage_uses_compact_system_rail(self) -> None:
        for language in ("zh", "en"):
            home = read(f"{language}/index.html")
            self.assertIn('class="mes-system-rail mono"', home)
            self.assertEqual(home.count('class="mes-flow-item"'), 4)
            self.assertEqual(home.count("<main"), 1)
            self.assertEqual(home.count("<h1"), 1)

    def test_manufacturing_uses_flow_list_and_outcome_strip(self) -> None:
        for language in ("zh", "en"):
            manufacturing = read(f"{language}/manufacturing.html")
            self.assertIn('class="digital-outcome-strip"', manufacturing)
            self.assertNotIn('class="digital-outcomes"', manufacturing)
            self.assertEqual(manufacturing.count('class="digital-system"'), 3)
            self.assertEqual(manufacturing.count('class="digital-capability"'), 6)
            self.assertEqual(manufacturing.count("<main"), 1)
            self.assertEqual(manufacturing.count("<h1"), 1)

    def test_card_specific_visual_rules_are_removed(self) -> None:
        css = read("css/site.css")
        home_start = css.index(".home-mes {")
        home_end = css.index(".home-quality {", home_start)
        digital_start = css.index(".digital-manufacturing {")
        digital_end = css.index(".manufacturing-quality {", digital_start)
        homepage_mes_css = css[home_start:home_end]
        digital_css = css[digital_start:digital_end]

        self.assertNotIn("min-height: 250px", homepage_mes_css)
        self.assertNotIn("position: sticky", homepage_mes_css)
        self.assertNotIn("background: rgba(255,255,255,0.42)", digital_css)
        self.assertNotIn("min-height: 280px", digital_css)
        self.assertIn(".digital-outcome-strip", digital_css)


if __name__ == "__main__":
    unittest.main()
