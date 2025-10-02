import requests
import re
import json
from datetime import datetime
import os

class ParserCBRF:
    def __init__(self, url):
        self.url = url
        self.data = {}
        self.save_path = os.path.dirname(os.path.realpath(__file__))

    def start(self):
        self._fetch_data()
        self._save_data()

    def _fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            page_content = response.text
            self._parse_html(page_content)

    def _parse_html(self, page_content):
        categories_match = re.search(r'"categories":\s*\[([^\]]+)\]', page_content)
        data_match = re.search(r'"data":\s*\[([^\]]+)\]', page_content)

        if categories_match and data_match:
            categories = categories_match.group(1).replace('"', '').split(',')
            data = list(map(float, data_match.group(1).split(',')))

            for i in range(len(categories)):
                date = datetime.strptime(categories[i].strip(), "%d.%m.%Y").date()
                self.data[date] = data[i]

    def _save_data(self):
        data_to_save = {str(date): rate for date, rate in self.data.items()}
        file_path = os.path.join(self.save_path, 'key_rate_data.json')
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_to_save, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    url = 'https://www.cbr.ru/hd_base/KeyRate/'
    parser = ParserCBRF(url)
    parser.start()
