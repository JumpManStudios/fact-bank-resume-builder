import importlib.util
import sys
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "template"
sys.path.insert(0, str(Path(__file__).resolve().parent))


def _load(module_name, filename):
    spec = importlib.util.spec_from_file_location(module_name, TEMPLATE_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_fix_bullet_spacing():
    return _load("fix_bullet_spacing", "fix-bullet-spacing.py")


def load_review_docx():
    return _load("review_docx", "review-docx.py")
