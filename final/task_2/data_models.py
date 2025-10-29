from __future__ import annotations
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Iterator

ISO = "%Y-%m-%d"

def to_date(s: str) -> date:
    return datetime.strptime(s, ISO).date()

def to_iso(d: date) -> str:
    return d.strftime(ISO)

def date_range(start: date, end: date) -> Iterator[date]:
    cur = start
    while cur <= end:
        yield cur
        cur += timedelta(days=1)

def to_decimal(s: str) -> Decimal:
    return Decimal(s.replace(",", "."))
