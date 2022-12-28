
# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random  # импорт библиотеки "random"
k = int(input('Введите максимальную степень k: '))
my_list = {}  # создание пустого списка(масива)
for i in range(k, -1, -1):
    my_list[i] = random.randint(-100, 100)
print(my_list)

my_list_str = ''  # создание пустой строки

str_cod = ['\u2070','\u00B9','\u00B2','\u00B3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079']

for index, meaning in my_list.items():
    str_index= ''
    for elem in str(index):
        str_index += str_cod[int(elem)]
        
    if meaning > 0 and my_list_str != '': #если коэффициент(множитель) положительный и строка не пустая, то добавляем в строку плюс 
        #(Если коэффициент отрицательный, минус будет у самого коэффициента, добавлять его не нужно. Если коэффициент 0, 
        #то мы ничего не добавим в строку, поэтому так же плюс добавлять не нужно - конструкции типа 0x**2 мы не добавляем.)
        my_list_str += ' + '
    elif meaning < 0 and my_list_str != '': 
        my_list_str += ' - '
    elif meaning < 0 and my_list_str == '': # elif meaning < 0 and index == k
        my_list_str += '-' 

    if meaning > 1 or meaning < -1:
        my_list_str += f'{abs(meaning)}'
        
    if meaning != 0 and index > 0:
        my_list_str += f'x{str_index}'
    elif meaning == 1 or meaning == -1 and index == 0:
        my_list_str += '1'
        
print(my_list_str+ ' = 0')
