
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = PROJECT_ROOT / "scripts" / "validate_status.py"


class TestValidateStatus(unittest.TestCase):

    def run_validator(self, json_content):
        with tempfile.TemporaryDirectory() as temp:
            test_root = Path(temp)

            (test_root / "scripts").mkdir()
            (test_root / "src").mkdir()

            shutil.copy2(
                VALIDATOR,
                test_root / "scripts" / "validate_status.py"
            )

            (test_root / "src" / "status.json").write_text(
                json_content,
                encoding="utf-8"
            )

            return subprocess.run(
                [sys.executable, str(test_root / "scripts" / "validate_status.py")],
                capture_output=True,
                text=True,
                check=False
            )

    def test_valid_status(self):
        data = '{"services": [{"name": "Database Service", "status": "operational"}]}'
        result = self.run_validator(data)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_status(self):
        data = '{"services": [{"name": "Database Service", "status": "degraded"}]}'
        result = self.run_validator(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Invalid status", result.stderr)

    def test_malformed_json(self):
        data = '{"services": ['
        result = self.run_validator(data)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("JSONDecodeError", result.stderr)


if __name__ == "__main__":
    unittest.main()
