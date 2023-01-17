# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


import random
name1 = input('Игрок №1 Введите ваше имя: ')
name2 = input('Игрок №2 Введите ваше имя: ')

if random.randrange(1, 3) == 1:
    print('Ходит игрок: ' + name1)
    nextMove = name1
else:
    print('Ходит игрок: ' + name2)
    nextMove = name2

total = int(input('Введите кол-во конфет в общей куче: '))

while total > 0:
    if total >= 28:
        move = int(
            input(f'{nextMove}, сколько вы берете конфет из общей кучи (от 1 до 28): '))
    else:
        move = int(input(
            f'{nextMove}, сколько вы берете конфет из общей кучи (от 1 до {total}): '))
    if move <= total and move > 0 and move <= 28:
        total = total - move
        print(f'В общей куче осталось {total} конфет')
        if nextMove == name1:
            nextMove = name2
        else:
            nextMove = name1
    else:
        print(f'{nextMove}, ввели некорректное значение, повторите ход.')
if nextMove == name2:
    print(f'{name1}, вы победили!')
else:
    print(f'{name2}, вы победили!')
