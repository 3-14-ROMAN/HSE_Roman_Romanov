# 1 ввод имени и изменения ID переменной a

a = 1  # int
print(a,'= a befor', id(a))
a = 1 + 5
print(a, '= a after', id(a))
b = 5.5  # float
c = True  # bool
d = False  # bool
print(a+b+c+True-False)


first_name = input("Введите ваше имя: ")  # Запрашиваем имя
middle_name = input("Введите ваше отчество: ")  # Запрашиваем отчество

print("Здравствуйте,", first_name, middle_name + "!")  # результат







# 2 конвектор секунд

while True:
    секунды = input("Введи время в секундах: ")

    if секунды.isdigit():
        часы = int(секунды) // 3600
        минуты = ((int(секунды)) % 3600) // 60
        остаток = int(секунды) % 60

        print("Часы:", часы)
        print("Минуты:", минуты)
        print("Секунды:", остаток)
        break
    else:
        print("Пиши только цифры, пожалуйста.")






# 3 арифметическая композиция

while True:
    n = input("Введите число от 1 до 9: ")

    if n.isdigit() and 1 <= int(n) <= 9:
        nn = n*2
        nnn = n*3

        print(n, '+', nn, '+', nnn, '=', (int(n)+int(nn)+int(nnn)))
        break

    else:
        print("Ошибка: введите ОДНУ цифру от 1 до 9.")
