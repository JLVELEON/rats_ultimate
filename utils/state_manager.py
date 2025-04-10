import json
from pathlib import Path
from typing import Dict

STATE_FILE = Path("rats_state.json")


def load_progress() -> Dict[str, int]:
    """Carga el progreso desde el archivo JSON."""
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}  # Si no existe el archivo, empezamos desde 0


def save_progress(data: Dict[str, int]) -> None:
    """Guarda el progreso en el archivo JSON."""
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
