# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите число: x')
x = int(input())
print('Введите число: y')
y = int(input())
print('Введите число: z')
z = int(input())

a = x * y * z
b = x + y + z

if a == b:
    print('Истинно')
elif a != b:
    print('Ложно')

# Не сделана, попытка не удалась