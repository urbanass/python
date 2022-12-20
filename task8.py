# Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int




my_list = [1, 2, 3, 4, 5, 6]
print ("Исходнй список : " + str(my_list))
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
new_my_list = my_list
for i in range(0, len(new_my_list)-2, 1):
    new_my_list[i], new_my_list[i+1] = new_my_list[i+1], new_my_list[i]
print ("Результат смешения : " +  str(new_my_list))