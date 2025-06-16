print('Hello world')

file = open('/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.txt', 'r')
data = file.readlines()
file.close()

with open('/Users/roman/Desktop/HSE_Roman_Romanov/lesson_3/traders.txt', 'r') as file:
    data = file.readlines()


print('stop')