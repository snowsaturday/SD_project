import random

number_pool = 20

# Диван
player_1_win_number = (1, 2, 3)
# клиент
player_2_win_number = (4, 5, 6, 7, 8, 9)


def player_1_pool_generator():
	array = []

	for i in range(0, int(number_pool) - int((number_pool / 100) * 30)):
		x = random.choice(player_1_win_number)
		y = random.choice(range(1, 99))
		result = '{}{}'.format(x, y)
		array.append(int(result))

	for i in range(0, int(number_pool) - int((number_pool / 100) * 70)):
		y = random.choice(range(1, 999))
		array.append(y)

	# for i in range(0, int(number_pool)):
	# 	y = random.choice(range(1, 999))
	# 	array.append(y)

	print(array)
	return array


def player_2_pool_generator():
	array = []

	for i in range(0, int(number_pool)):
		y = random.choice(range(1, 999))
		array.append(y)

		# y = input('Введите число {} из {}:'.format(i + 1, number_pool))
		# try:
		# 	if y == '0':
		# 		raise ValueError
		# 	else:
		# 		array.append(int(y))
		#
		# except ValueError:
		# 	print('Вы ввели недопустимое значение, вводите любые цифры кроме 0 (ноль)')
		# 	y = input('Введите число {} из {}:'.format(i + 1, number_pool))
		# 	array.append(int(y))

	print(array)
	return array


p1_wins = 0
p2_wins = 0
no_winner = 0

for game in range(0, 100):

	p1_pool = player_1_pool_generator()
	p2_pool = player_2_pool_generator()

	array = []

	for _ in range(0, number_pool):
		x = p1_pool.pop()
		y = p2_pool.pop()
		z = x * y
		array.append(z)

	print(array)

	p1_points = 0
	p2_points = 0

	for _ in array:
		result = str(_)[0]
		# print(result)
		if result in '123':
			p1_points += 1
		else:
			p2_points += 1

	if p1_points == p2_points:
		print('Ничья!')
		print('{}:{}'.format(p1_points, p2_points))
		no_winner += 1
	elif p1_points > p2_points:
		print('ДИВАН победил!')
		print('{}:{}'.format(p1_points, p2_points))
		p1_wins += 1
	elif p1_points < p2_points:
		print('Клиент победил!')
		print('{}:{}'.format(p2_points, p1_points))
		p2_wins += 1

print('ДИВАН Победы: {}'.format(p1_wins))
print('Клиент Победы: {}'.format(p2_wins))
print('Ничьи: {}'.format(no_winner))
