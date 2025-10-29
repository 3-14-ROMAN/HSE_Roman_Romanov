from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
from .parser_cbrf import ParserCBRF
from .storage import json_path

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="CBR Parser")
    p.add_argument("from_date", help="YYYY-MM-DD")
    p.add_argument("to_date", help="YYYY-MM-DD")
    p.add_argument("--out", default=str(json_path()), help="путь к JSON")
    return p.parse_args()

def main() -> None:
    ns = parse_args()
    f = date.fromisoformat(ns.from_date)
    t = date.fromisoformat(ns.to_date)
    out = Path(ns.out)
    path = ParserCBRF(from_date=f, to_date=t, save_to=out).start()
    print(f"Saved to: {path}")

if __name__ == "__main__":
    main()
