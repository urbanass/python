# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите число от 1 до 7: ')
a = int(input())

if a > 5:
    print('Это выходной день')
else:
    print('Это не выходной день')
