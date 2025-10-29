from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, Any

import requests
from bs4 import BeautifulSoup

from .data_models import date_range, to_iso, to_decimal
from .storage import save_json, json_path

CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"

@dataclass
class ParserCBRF:
    from_date: date
    to_date: date
    save_to: Path = json_path()

    def _fetch_day(self, d: date) -> Dict[str, Dict[str, Any]]:
        params = {"date_req": d.strftime("%d/%m/%Y")}
        r = requests.get(CBR_URL, params=params, timeout=15)
        r.raise_for_status()
        soup = BeautifulSoup(r.content, "xml")
        result: Dict[str, Dict[str, Any]] = {}
        for node in soup.find_all("Valute"):
            code = node.find("CharCode").text.strip()
            nominal = int(node.find("Nominal").text.strip())
            val_raw = node.find("Value").text.strip()
            val_dec = to_decimal(val_raw)
            value_str = str(val_dec.quantize(to_decimal("0,0001")))
            result[code] = {"value": value_str, "nominal": nominal}
        return result

    def _fill_gaps(self, data: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        filled: Dict[str, Dict[str, Any]] = {}
        prev: Dict[str, Any] | None = None
        for day in sorted(data.keys()):
            today = data.get(day) or {}
            if today:
                filled[day] = today
                prev = today
            elif prev is not None:
                filled[day] = {k: v.copy() if isinstance(v, dict) else v for k, v in prev.items()}
            else:
                filled[day] = {}
        return filled


    def start(self) -> Path:
        collected: Dict[str, Dict[str, Any]] = {}
        for d in date_range(self.from_date, self.to_date):
            collected[to_iso(d)] = self._fetch_day(d)
        collected = self._fill_gaps(collected)
        return save_json(collected, self.save_to)

