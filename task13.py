# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = int(input('Введите число: '))


def fibonacci(k):
    nums = []
    a = 1
    b = 1
    for i in range(k):
        nums.append(a)
        x = a
        a = b
        b = x + b
    a = 0
    b = 1
    for i in range(k+1):
        nums.insert(0, a)
        x = a
        a = b
        b = x - b

    return nums


nums = fibonacci(k)
print(fibonacci(k))
