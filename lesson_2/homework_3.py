# 2.1 функция для генерации текста с адресом суда

import re
import unicodedata
import lesson_2_data  # Файл lesson_2_data.py должен быть в той же папке

def normalize(s):
    """Приводит строку к стандартизированной форме: убирает пробелы, \xa0, делает верхний регистр"""
    return unicodedata.normalize("NFKC", s).strip().replace('\xa0', '').replace(' ', '').upper()

def extract_court_code(case_number):
    case_number = case_number.replace("А", "A")  # русская на латинскую
    match = re.match(r'A(\d+)-', case_number)
    if match:
        return f"A{match.group(1).zfill(2)}"
    return None

def generate_header(respondent, case_number, my_data, courts):
    court_code = extract_court_code(case_number)
    clean_courts = [c for c in courts if isinstance(c, dict) and 'court_code' in c]

    court = next(
        (c for c in clean_courts if normalize(c.get('court_code', '')) == normalize(court_code)),
        None
    )

    court_name = court['court_name'] if court else f"Арбитражный суд с кодом {court_code or '??'}"
    court_address = court['court_address'] if court else "адрес не указан"

    resp_ogrn_type = "ОГРНИП" if len(respondent['ogrn']) == 15 else "ОГРН"
    my_ogrn_type = "ОГРНИП" if len(my_data['ogrn']) == 15 else "ОГРН"

    header = f"В {court_name}\n"
    header += f"Адрес: {court_address}\n\n"
    header += f"Истец: {my_data['full_name']}\n"
    header += f"ИНН {my_data['inn']} {my_ogrn_type} {my_data['ogrn']}\n"
    header += f"Адрес: {my_data['address']}\n\n"
    header += f"Ответчик: {respondent['full_name']}\n"
    header += f"ИНН {respondent['inn']} {resp_ogrn_type} {respondent['ogrn']}\n"
    header += f"Адрес: {respondent['address']}\n\n"
    header += f"Номер дела {case_number}"
    return header

def get_user_data():
    print("="*50)
    print("ВВЕДИТЕ ВАШИ ДАННЫЕ КАК ИСТЦА")
    print("="*50)
    return {
        'full_name': input("Ваше полное ФИО: "),
        'inn': input("Ваш ИНН: "),
        'ogrn': input("Ваш ОГРН/ОГРНИП: "),
        'address': input("Ваш полный адрес: ")
    }

def select_respondent(respondents):
    print("\n" + "="*50)
    print("ДОСТУПНЫЕ ОТВЕТЧИКИ С НОМЕРАМИ ДЕЛ")
    print("="*50)
    valid = [r for r in respondents if 'case_number' in r]
    for i, r in enumerate(valid, 1):
        print(f"{i}. {r.get('short_name', r['full_name'])} ({r['case_number']})")
    while True:
        try:
            idx = int(input("\nВыберите номер ответчика: "))
            if 1 <= idx <= len(valid):
                return valid[idx - 1]
        except:
            pass
        print("Ошибка: введите номер из списка")

def main():
    respondents = lesson_2_data.respondents
    courts = lesson_2_data.courts

    my_data = get_user_data()
    respondent = select_respondent(respondents)
    header = generate_header(respondent, respondent['case_number'], my_data, courts)

    print("\n" + "="*50)
    print("СГЕНЕРИРОВАННАЯ ШАПКА ДОКУМЕНТА")
    print("="*50)
    print(header)

if __name__ == "__main__":
    main()
