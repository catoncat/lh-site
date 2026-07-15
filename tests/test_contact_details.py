import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ContactDetailsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, "build-pages.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_general_manager_name_and_phone_are_current(self) -> None:
        zh = (ROOT / "zh/contact.html").read_text(encoding="utf-8")
        en = (ROOT / "en/contact.html").read_text(encoding="utf-8")

        self.assertIn("Jared Lee / 李卓星", zh)
        self.assertIn("Jared Lee", en)
        self.assertIn('href="tel:+867505611189">+86 750 5611189</a>', zh)
        self.assertIn('href="tel:+867505611189">+86 750 5611189</a>', en)
        self.assertNotIn("Jare Lee", zh + en)
        self.assertNotIn("+86 135 5690 3684", zh + en)


if __name__ == "__main__":
    unittest.main()
