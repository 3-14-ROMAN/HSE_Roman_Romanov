import json
import csv
import re
from pathlib import Path

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(text):
    if not text:
        return []
    return re.findall(EMAIL_REGEX, text)


def extract_emails_by_inn(messages):
    result = {}
    for msg in messages:
        inn = msg.get("publisher_inn")
        if not inn:
            continue
        email_set = set()
        for key, value in msg.items():
            if isinstance(value, str):
                email_set.update(extract_emails(value))
        if email_set:
            result.setdefault(inn, set()).update(email_set)
    return {inn: list(emails) for inn, emails in result.items()}


def load_inn_list(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


def load_traders_data(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def filter_traders_by_inn(traders_data, inn_list):
    return [
        trader for trader in traders_data
        if trader.get("inn") in inn_list
    ]


def save_traders_to_csv(traders, output_csv_path):
    with open(output_csv_path, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["inn", "ogrn", "address"])
        writer.writeheader()
        for trader in traders:
            writer.writerow({
                "inn": trader.get("inn"),
                "ogrn": trader.get("ogrn"),
                "address": trader.get("address")
            })


def process_and_save_emails(input_json_path, output_json_path):
    with open(input_json_path, "r", encoding="utf-8") as f:
        messages = json.load(f)
    emails_by_inn = extract_emails_by_inn(messages)
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(emails_by_inn, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    txt_path = BASE_DIR / "traders.txt"
    json_path = BASE_DIR / "traders.json"
    messages_path = BASE_DIR / "1000_efrsb_messages.json"
    output_csv = BASE_DIR / "traders.csv"
    output_emails = BASE_DIR / "emails.json"

    # Создание traders.csv
    inn_list = load_inn_list(txt_path)
    traders_data = load_traders_data(json_path)
    filtered_traders = filter_traders_by_inn(traders_data, inn_list)
    save_traders_to_csv(filtered_traders, output_csv)
    print("Файл traders.csv создан.")

    # Создание emails.json
    process_and_save_emails(messages_path, output_emails)
    print("Файл emails.json создан.")
