# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random 

total = int(input('Введите кол-во конфет: '))
max = 28
name1 = input('Игрок №1 Введите ваше имя: ')
name2 = 'iBot'
players = [name1, name2]

one = random.randrange(1, 3)

print(f'{players[one-1]} Ваш ход')

while total > 0:
    one += 1
    if players[one % 2] == 'iBot':
        print(f'Ходит {players[one%2]}')

        if total < 29:
            motion = total
        else:
            logic = total//28
            motion = total - ((logic*max)+1)
            if motion == -1:
                motion = max - 1
            if motion == 0:
                motion = max
        while motion > 28 or motion < 1:
            motion = randint(1, 28)
        print(motion)
    else:
        motion = int(input(f'ходи,{players[one%2]} Осталось {total}: '))
        while motion > max or motion < 1:
            motion = int(input('Недопутимое число,Вы можите взять 1-28 конфет: '))
    total = total - motion

print(f'осталось {total} Победил {players[one%2]}')
