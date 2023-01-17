# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random
name1 = input('Введите ваше имя: ')
name2 = 'iRobot'
if random.randrange(1, 3) == 1:
	print('Первым ходит игрок: ' + name1)
	nextMove = name1
else:
	nextMove = name2
	print('Первым ходит игрок: ' + name2)

total = int(input('Введите кол-во конфет в общей куче: '))

while total > 0:
	if nextMove == name1:
		if total >= 28:
			move = int(input(f'{name1}, сколько конфет вы берете из общей кучи (от 1 до 28): '))
		else:
			move = int(input(f'{name1}, сколько конфет вы берете из общей кучи (от 1 до {total}): '))
		if move <= total and move > 0:
			total = total - move
			print(f'В общей куче осталось {total} конфет')
			nextMove = name2   
		else:
			print(f'{name1}, ввели некорректное значение, повторите ход.')
	else:
		if total > 28:
			if (total % 28) > 1:
				move = (total % 28) - 1
			elif (total % 28) == 0:
				move = 27
			else:
				move = random.randrange(1, 29)
		else:
			move = total
		print(f'{name2} берет {move} конфет')
		total = total - move
		print(f'В общей куче осталось {total} конфет')	
		nextMove = name1
if nextMove == name2:
	print(f'{name1}, вы победили!')
else:
	print(f'{name2}, вы победили!')