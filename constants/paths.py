from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"
ICONS_DIR = ASSETS_DIR / "icons"
IMAGES_DIR = ASSETS_DIR / "images"

ARCHIVES_DIR = BASE_DIR / "archives"

REPORTS_DIR = ARCHIVES_DIR / "reports"

REPORTS_IMAGES_DIR = REPORTS_DIR / "images"

DATABASE_DIR = BASE_DIR / "database"
