"""PPG-Pulsmonitor: Aufnahme, Signalverarbeitung und Bericht."""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_config(path: Path | None = None) -> dict:
    """Lädt die gemeinsamen Parameter aus config.json."""
    path = path or PROJECT_ROOT / "config.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)
