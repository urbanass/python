# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
for i in range(len(my_list)//2 + len(my_list) % 2):
    res = my_list[i] * my_list[(len(my_list)-1)-i]
    print(res)
