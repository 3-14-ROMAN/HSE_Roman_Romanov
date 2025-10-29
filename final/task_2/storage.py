from __future__ import annotations
from pathlib import Path
import json
from typing import Any, Dict

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DIR = BASE_DIR / "parsed_data"
DEFAULT_DIR.mkdir(parents=True, exist_ok=True)

def json_path(filename: str = "cbr_rates.json") -> Path:
    p = DEFAULT_DIR / filename
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def save_json(data: Dict[str, Any], path: Path | None = None) -> Path:
    path = path or json_path()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path

def load_json(path: Path | None = None) -> Dict[str, Any]:
    path = path or json_path()
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))
