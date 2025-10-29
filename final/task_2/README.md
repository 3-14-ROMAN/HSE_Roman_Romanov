# Парсер ЦБ РФ — курсы валют (final/task_2)

# Установка: 

python3 -m venv .venv
source .venv/bin/activate
pip install -r final/task_2/requirements.txt
pip install lxml


# Сбор данных:

PYTHONPATH=final python3 -m task_2.cli 2024-01-01 2024-01-09

результат: final/task_2/parsed_data/cbr_rates.json

# Работа с данными:

# Список валют:

PYTHONPATH=final python3 -m task_2.cli_rates list

# Последний курс по коду:

PYTHONPATH=final python3 -m task_2.cli_rates last USD

# Курс по дате:

PYTHONPATH=final python3 -m task_2.cli_rates bydate USD 2024-01-02

# Курсы за период:

PYTHONPATH=final python3 -m task_2.cli_rates range USD 2024-01-06 2024-01-09