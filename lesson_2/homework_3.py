from lesson_2_data import respondents, courts
import lesson_2_data
import unicodedata
import re






# 1.1 функция вычисления факториала числа

def factorial(n):
    результат = 1
    for i in range(1, n + 1):
        результат = результат * i
    return результат


число = input("Введите положительное целое число: ")

if число.isdigit():
    число = int(число)
    факториал = factorial(число)
    print(f"Факториал числа {число} равен {факториал}")
else:
    print("Ошибка: введите только положительное целое число.")







# 1.2 поиск наибольшего числа из трёх

def это_число(значение):
    try:
        float(значение)
        return True
    except ValueError:
        return False


def найти_максимум(числа):
    return max(числа)


while True:
    число1 = input("Введите первое число: ")
    число2 = input("Введите второе число: ")
    число3 = input("Введите третье число: ")

    if это_число(число1) and это_число(число2) and это_число(число3):
        a = float(число1)
        b = float(число2)
        c = float(число3)

        результат = найти_максимум((a, b, c))
        print(f"\nНаибольшее число из {a}, {b}, {c} — это {результат}\n")
        break
    else:
        print("Ошибка: введите допустимые числа (можно с точкой).\n")







# 1.3 расчёт площади прямоугольного треугольника

def это_число(значение):
    try:
        float(значение)
        return True
    except ValueError:
        return False


def площадь_треугольника(катет1, катет2):
    return 0.5 * катет1 * катет2


while True:
    катет1 = input("Введите длину первого катета: ")
    катет2 = input("Введите длину второго катета: ")

    if это_число(катет1) and это_число(катет2):
        k1 = float(катет1)
        k2 = float(катет2)
        площадь = площадь_треугольника(k1, k2)
        print(f"\nПлощадь прямоугольного треугольника: {площадь}")
        break
    else:
        print("Ошибка: введите только числа (целые или дробные).\n")








# 2 функция для генерации шапки и дополнительно генерация шапок для всех ответчиков

def normalize(s):
    # """Нормализует строку: убирает пробелы, \xa0, заменяет русскую А на латинскую, приводит к верхнему регистру"""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace('\xa0', '').replace(' ', '').replace(
        'А', 'A')  # русская А в латинская A
    return s.strip().upper()


def extract_court_code(case_number):
    # """Извлекает код суда из номера дела (например, A56 из A56-12345/2021)"""
    case_number = normalize(case_number)
    match = re.match(r'A(\d+)-', case_number)
    if match:
        return f"A{match.group(1).zfill(2)}"
    return None


def format_court_line(court_name_raw):
    # """Формирует строку 'Арбитражный суд ...' из названия в родительном падеже"""
    pattern = r"Арбитражного суда\s+(.*)"
    match = re.search(pattern, court_name_raw, re.IGNORECASE)
    if match:
        region = match.group(1)
        return f"Арбитражный суд {region}"
    return court_name_raw


def generate_header(respondent, case_number, my_data, courts):
    court_code = extract_court_code(case_number)
    court = next(
        (c for c in courts if normalize(
            c.get('court_code', '')) == normalize(court_code)),
        None
    )

    court_name = court[
        'court_name'] if court else f"Арбитражный суд с кодом {court_code or '??'}"
    court_address = court['court_address'] if court else "адрес не указан"
    court_name_formatted = format_court_line(court_name)

    resp_ogrn_type = "ОГРНИП" if len(respondent['ogrn']) == 15 else "ОГРН"
    my_ogrn_type = "ОГРНИП" if len(my_data['ogrn']) == 15 else "ОГРН"

    header = f"В {court_name_formatted}\n"
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
        print(
            f"{i}. {r.get('short_name', r['full_name'])} ({r['case_number']})")
    while True:
        try:
            idx = int(input("\nВыберите номер ответчика: "))
            if 1 <= idx <= len(valid):
                return valid[idx - 1]
        except:
            pass
        print("Ошибка: введите номер из списка")


def generate_all_headers(respondents, my_data, courts):
    print("\n" + "="*50)
    print("ГЕНЕРАЦИЯ ШАПОК ДЛЯ ВСЕХ ОТВЕТЧИКОВ")
    print("="*50)
    valid = [r for r in respondents if 'case_number' in r]
    for r in valid:
        print("\n" + "-"*50)
        print(generate_header(r, r['case_number'], my_data, courts))


def main():
    my_data = get_user_data()
    respondent = select_respondent(respondents)

    print("\n" + "="*50)
    print("СГЕНЕРИРОВАННАЯ ШАПКА ДОКУМЕНТА")
    print("="*50)
    print(generate_header(respondent,
          respondent['case_number'], my_data, courts))

    choice = input(
        "\nХотите сгенерировать шапки для всех ответчиков? (введите + или -): ")
    if choice.strip() == "+":
        generate_all_headers(respondents, my_data, courts)


if __name__ == "__main__":
    main()