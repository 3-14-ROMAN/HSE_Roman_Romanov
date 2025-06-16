print('Hello world')

import csv
import json
import decimal

abs_path_txt = '/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.txt'
rel_path_txt = 'lesson_3/traders.txt'

with open(rel_path_txt, 'r') as file:
    data = file.readlines()

abs_path_json = '/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/1000_efrsb_messages.json'
rel_path_json = '1000_efrsb_messages.json'

with open(abs_path_json, 'r') as file:
    data = json.load(file)


abs_path_csv = '/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.csv'
rel_path_csv = 'traders.csv'

with open(abs_path_csv, 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        print(', '.join(row))

best_delimiter = | 



# # with open('/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.txt', 'r') as file:
# #     data = file.readlines()

# file = open(rel_path_txt, 'r')
# data = file.readlines()
# file.close()


print('stop')