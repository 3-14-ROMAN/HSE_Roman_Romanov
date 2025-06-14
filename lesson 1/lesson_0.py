# Запрашиваем имя
first_name = input("Введите ваше имя: ")

# Запрашиваем отчество
middle_name = input("Введите ваше отчество: ")

# Выводим результат
print("Здравствуйте,", first_name, middle_name + "!")


a = 1 # int
print ('a befor', id(a))
a = 1 + 5
print ('a after', id(a))
b = 5.5 # float
c = True # bool
d = False # bool
print(a+b+c+True-False)

name = 'Roman'
surmame = 'Romanov'
print (name + ' ' + surmame)
print (name [-3]+name [-4]+name [-5])

company = 'АО "Gate 127"'
print (company)

company_list = ['АО "Gate 127"',
                 'ООО "Б 152"',
                 'ООО "Футбол"']
print (company_list)
print (company_list[0])


company_tuple = ('АО "Gate 127"',
                 'ООО "Б 152"',
                 'ООО "Футбол"')
print (company_tuple)
print (company_tuple[-1])


company_dict = {'name': 'АО "Gate 127"',
                'inn': '781633333333',
                'address': 'Krasnoyaskrk, Dubenskogo 3', 
                'employers': 14,
                'active': True}
print ('company_dict befor', company_dict)
company_dict['address'] = 'Krasnoyaskrk, Dubenskogo 8'
company_dict['employers'] -= 2
print ('company_dict after', company_dict)

 