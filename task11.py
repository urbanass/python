# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
my_list = []
for _ in range(5):
    amount = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 20), amount))
print(my_list)
max = 0
min = 1
for i in range(5):
    x = my_list[i] % 1
    if x!=0:
        if x > max:
            max = x
        if x < min:
            min = x
# res = sum([x % 1 for x in my_list])
# ressred = res/len(my_list)
# print(round(res,3))
# print(ressred)
print(round(max-min,3))
print(max-min) # Просьба напомнить на семинаре почему без округления разница между 2 числами имеет так много "0" и цифрой в конце
