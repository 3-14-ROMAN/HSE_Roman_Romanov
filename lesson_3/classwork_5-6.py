import json

print('Hello world')


abs_path = '/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.txt'
rel_path = 'lesson_3/traders.txt'

file = open(rel_path, 'r')
data = file.readlines()
file.close()

file = open('/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/1000_efrsb_messages.json', 'rb') as file
data = json.load(file)
file.close()

with open('/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.txt', 'r') as file:
    data = file.readlines()


print('stop')