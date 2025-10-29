from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Tuple

from .storage import load_json
from .data_models import to_date as _to_date

class CurrencyRatesCBRF:
    def __init__(self, path: Path):
        self._path = Path(path)
        self._data: Dict[str, Dict[str, dict]] = load_json(self._path)

    def _ensure_loaded(self) -> None:
        if not self._data:
            self._data = load_json(self._path)

    def available_currencies(self) -> List[str]:
        self._ensure_loaded()
        for day in sorted(self._data.keys()):
            return sorted(self._data[day].keys())
        return []

    def rate_by_date(self, code: str, date_iso: str) -> str:
        self._ensure_loaded()
        day = self._data.get(date_iso)
        if not day:
            raise KeyError(f"нет данных за {date_iso}")
        rec = day.get(code.upper())
        if not rec:
            raise KeyError(f"валюта {code} не найдена")
        return rec["value"]

    def rate_last(self, code: str) -> str:
        self._ensure_loaded()
        if not self._data:
            raise KeyError("пустой датасет")
        last_date = max(self._data.keys())
        rec = self._data[last_date].get(code.upper())
        if not rec:
            raise KeyError(f"валюта {code} не найдена")
        return rec["value"]

    def rate_range_dates(self, code: str, from_date: str, to_date: str) -> List[Tuple[str, str]]:
        self._ensure_loaded()
        f = _to_date(from_date)
        t = _to_date(to_date)
        out: List[Tuple[str, str]] = []
        for day in sorted(self._data.keys()):
            d = _to_date(day)
            if f <= d <= t:
                rec = self._data[day].get(code.upper())
                if rec:
                    out.append((day, rec["value"]))
        return out
