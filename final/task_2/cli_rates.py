from __future__ import annotations
import argparse
from pathlib import Path
from .services_rates import CurrencyRatesCBRF
from .storage import json_path

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="CBR rates")
    p.add_argument("--data", default=str(json_path()), help="path to cbr_rates.json")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="list available currency codes")

    p_last = sub.add_parser("last", help="last rate by code")
    p_last.add_argument("code")

    p_by = sub.add_parser("bydate", help="rate by code and date")
    p_by.add_argument("code")
    p_by.add_argument("date")

    p_range = sub.add_parser("range", help="rates for period")
    p_range.add_argument("code")
    p_range.add_argument("from_date")
    p_range.add_argument("to_date")

    return p.parse_args()

def main() -> None:
    ns = parse_args()
    svc = CurrencyRatesCBRF(Path(ns.data))

    if ns.cmd == "list":
        print("\n".join(svc.available_currencies()))
    elif ns.cmd == "last":
        print(svc.rate_last(ns.code))
    elif ns.cmd == "bydate":
        print(svc.rate_by_date(ns.code, ns.date))
    elif ns.cmd == "range":
        for d, v in svc.rate_range_dates(ns.code, ns.from_date, ns.to_date):
            print(d, v)

if __name__ == "__main__":
    main()
