import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DeployWorkflowTests(unittest.TestCase):
    def test_upload_retries_transient_ssh_resets(self) -> None:
        workflow = (ROOT / ".github/workflows/deploy.yml").read_text(encoding="utf-8")

        self.assertIn("ConnectTimeout=15", workflow)
        self.assertIn("ConnectionAttempts=3", workflow)
        self.assertIn("retry rsync", workflow)
        self.assertIn("retry ssh", workflow)


if __name__ == "__main__":
    unittest.main()
