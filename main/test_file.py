# -*- coding: utf-8 -*-

# Функция log_push() завписывает в файл и\или выводит в коммандную строку
# информвацию о ключевых этапах работы программы
def log_push(file_path=None, type='info', message=None, time=True, minimal=True):
	# -------------------------------------АГРУМЕНТЫ---------------------------------------
	# file_path - путь к файлу логирования
	# type - success[+]успешно, info[i]информация, warning[!]предупреждение, error[-]ошибка
	# message - Текст сообщения (обязательный агрумент)
	# time - добавлять вывод времени в командную строку (по умолчанию True)
	# minimal - Минималистичный вывод в консоль (по умолчанию True) ([+] Успешно [+] vs [+])
	# -------------------------------------------------------------------------------------

	# Если задан обязательный аргумент message
	if message:
		# Определяем метрику текущего момента с проверкой на импорт соответствующего модуля
		try:
			now = datetime.datetime.today()
		except NameError:
			import datetime
			now = datetime.datetime.today()
		# Если аргумет file_path определен формируем сообщение для лога
		if file_path: log_message = '{}|{}\n'.format(now.strftime("%H:%M:%S|%d-%m-%Y"), message)
		# Продолжаем формировать сообщение в соответствии с указаными аргументами
		if type == 'success':

			prompt_message = '\x1b[1;32;0m[+]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(message)

			if file_path:
				log_message = '+|{}'.format(log_message)

			if not minimal:
				prompt_message = '\x1b[1;32;0m[+] Успешно \x1b[0m{}'.format(prompt_message)

			if time:
				prompt_message = '{} {}'.format(now.strftime("[%H:%M:%S]"), prompt_message)
		if type == 'info':

			prompt_message = '\x1b[1;34;0m[i]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(message)

			if file_path:
				log_message = 'i|{}'.format(log_message)

			if not minimal:
				prompt_message = '\x1b[1;34;0m[i] Информация \x1b[0m{}'.format(prompt_message)

			if time:
				prompt_message = '{} {}'.format(now.strftime("[%H:%M:%S]"), prompt_message)
		if type == 'warning':

			prompt_message = '\x1b[1;33;0m[!]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(message)

			if file_path:
				log_message = '!|{}'.format(log_message)

			if not minimal:
				prompt_message = '\x1b[1;33;0m[!] Предупреждение \x1b[0m{}'.format(prompt_message)

			if time:
				prompt_message = '{} {}'.format(now.strftime("[%H:%M:%S]"), prompt_message)
		if type == 'error':

			prompt_message = '\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(message)

			if file_path:
				log_message = '-|{}'.format(log_message)

			if not minimal:
				prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m{}'.format(prompt_message)

			if time:
				prompt_message = '{} {}'.format(now.strftime("[%H:%M:%S]"), prompt_message)
		# Если аргумет file_path определен пишем в лог файл строку с информацией
		if file_path:
			try:
				with open(file_path, 'a') as f:
					f.write(log_message)
			except FileNotFoundError:
				with open(file_path, 'w') as f:
					f.write(log_message)
		# Выводим сообщение в коммандную строку
		print(prompt_message)
	# Ошибка - не задан обязательный аргумент
	else:
		prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(
			'Отсутствует обязательный аргумент \'message\' функции log_push()')
		print(prompt_message)


# Функция line_pull_from_file() забирает строку из файла в соответствии с переданными
# аргументами и возвращает её значение
def line_pull_from_file(file=None, log_file=None, index=0, random=False):
	# -------------------------------------АГРУМЕНТЫ---------------------------------------
	# file - путь к файлу с искомыми строками (обязательный агрумент)
	# log_file - путь к файлу если требуется логирование действия
	# index - номер возвращаемой строки (по умолчанию 1я строка)
	# -------------------------------------------------------------------------------------

	# Если задан обязательный аргумент file
	if file:
		# Открываем файл. Считываем все строки. Забираем нужную в соответствии с переданными аргументами
		try:
			with open(file, 'r') as f:
				lines = f.readlines()
				try:
					item = lines.pop(index)
					return item
				except IndexError:
					if lines:
						item = lines.pop(len(lines) - 1)
						if log_file:
							log_push(file_path=log_file, type='warning',
							         message='Отсутствует элемент с запрошеным индексом [{}] в файле \'{}\' - возвращен последний элемент'.format(
								         index, file))
						if not log_file:
							log_push(type='warning',
							         message='Отсутствует элемент с запрошеным индексом [{}] в файле \'{}\' - возвращен последний элемент'.format(
								         index, file))
						return item
					else:
						if log_file:
							log_push(file_path=log_file, type='error',
							         message='Файл \'{}\' не содержит ни одной строки'.format(file))
						if not log_file:
							log_push(type='error', message='Файл \'{}\' не содержит ни одной строки'.format(file))
						return None
		# Если файл не найден формируем сообщение об ошибке
		except FileNotFoundError:
			if log_file:
				log_push(file_path=log_file, type='error',
				         message='Файл \'{}\' не найден функцией line_pull_from_file()'.format(file))
			if not log_file:
				log_push(type='error', message='Файл \'{}\' не найден функцией line_pull_from_file()'.format(file))
			return None
		finally:
			# Если в списке lines есть обьекты - открываем файл и сохраняем обьекты
			if lines:
				with open(file, 'w') as f:
					for i in lines:
						f.write(i)
			# Если в списке lines нет обьектов - обнуляем файл
			else:
				with open(file, 'w'):
					pass
	# Если не задан обязательный аргумент file - выводим ошибку
	else:
		prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(
			'Отсутствует обязательный аргумент \'file\' функции line_pull_from_file()')
		print(prompt_message)


# Функция line_push_to_file() добавляет строку в файл в соответствии
# с переданными аргументами
def line_push_to_file(file=None, line=None, log_file=None, index=0, random=False):
	# -------------------------------------АГРУМЕНТЫ---------------------------------------
	# file - путь к файлу для добавления данных (обязательный агрумент)
	# line - строка которая добаляется в файл (обязательный агрумент)
	# log_file - путь к файлу если требуется логирование действия
	# index - номер строки для добабления данных (по умолчанию 1я строка)
	# -------------------------------------------------------------------------------------

	# Если задан обязательный аргумент file
	if file:
		# Если задан обязательный аргумент line
		if line:
			try:
				# Открываем файл. Считываем все строки в список
				# Добавляем строку в список в соответствии с переданными аргументами
				with open(file, 'r') as f:
					lines = f.readlines()
					if len(lines) > index:
						lines.insert(index, '{}\n'.format(line))
					else:
						lines.insert(index, '\n{}'.format(line))
						if log_file:
							log_push(file_path=log_file, type='warning',
							         message='Отсутствует запрошенный индекс [{}] в файле \'{}\' - элемент добавлен в конец файла'.format(
								         index, file))
						if not log_file:
							log_push(type='warning',
							         message='Отсутствует запрошенный индекс [{}] в файле \'{}\' - элемент добавлен в конец файла'.format(
								         index, file))
			# Если файл не найден формируем сообщение об ошибке
			except FileNotFoundError:
				if log_file:
					log_push(file_path=log_file, type='error',
					         message='Файл \'{}\' не найден функцией line_push_to_file()'.format(file))
				if not log_file:
					log_push(type='error', message='Файл \'{}\' не найден функцией line_push_to_file()'.format(file))
				return None
			# Записываем в файл список с добаленной строкой
			with open(file, 'w') as f:
				for i in lines:
					f.write(i)
		# Если не задан обязательный аргумент line - выводим ошибку
		else:
			prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(
				'Отсутствует обязательный аргумент \'line\' функции line_push_to_file()')
			print(prompt_message)
	# Если не задан обязательный аргумент file - выводим ошибку
	else:
		prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(
			'Отсутствует обязательный аргумент \'file\' функции line_push_to_file()')
		print(prompt_message)


# Функция time_control() проверяет входит ли метрика текущего момента
# в интервал переданный в агрументах и возвращает значение True|False
def time_control(start_time='11:00', stop_time='19:00'):
	# -------------------------------------АГРУМЕНТЫ---------------------------------------
	# start_time - начало временного интервала
	# stop_time - конец временного интервала
	# -------------------------------------------------------------------------------------

	error = False

	# Определяем метрику текущего момента с проверкой на импорт соответствующего модуля
	try:
		now = datetime.datetime.today()
	except NameError:
		import datetime
		now = datetime.datetime.today()

	# преобразуем время к числовым значениям
	now_hour = int(now.strftime("%H"))
	now_minute = int(now.strftime("%M"))
	start_time_hour = int(start_time.split(':')[0])
	start_time_minute = int(start_time.split(':')[1])
	stop_time_hour = int(stop_time.split(':')[0])
	stop_time_minute = int(stop_time.split(':')[1])

	# Проверка на недопустимый интервал между аргументами функции
	if start_time == stop_time:
		error = True
		prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(
			'Минимальная разница во времени между аргументами функции time_control() - 1 минута')
		print(prompt_message)
	if start_time_hour > stop_time_hour:
		error = True
		prompt_message = '\x1b[1;31;0m[-] Ошибка \x1b[0m\x1b[1;31;0m[-]\x1b[0m\x1b[0;30;0m {}\x1b[0m'.format(
			'Аргумент \'start_time\' функции time_control() > аргумента \'stop_time\'')
		print(prompt_message)
	# Проверка на вхождение текущего времени в интервал функции
	if not error:
		if (start_time_hour + (start_time_minute / 60)) \
				< (now_hour + (now_minute / 60)) \
				< (stop_time_hour + (stop_time_minute / 60)):
			return True
		else:
			return False


if __name__ == '__main__':
	# Импортируем необходимые модули
	import serial, time
	import RPi.GPIO as GPIO

	# Номер gsm устройства
	SOCKET_NUMBER = '15'
	# Номер пина на raspberry pi включающий плеер
	PIN = 27
	# Файл со списком номеров для обзвона
	NUMBER_LIST_FILE = 'number_to_call'
	# Длительность звукового файла
	SOUND_TIME = 60
	# Файл лога
	LOG_FILE = 'log_ttyUSB{}'.format(SOCKET_NUMBER)
	# Файл со списком номеров поднявших трубку
	SUCCESS_FILE = 'call_success_ttyUSB{}'.format(SOCKET_NUMBER)
	# Файл со списком номеров не поднявших трубку
	BUSY_FILE = 'call_busy_ttyUSB{}'.format(SOCKET_NUMBER)
	# Файл со списком номеров на которые сеть вернула NO CARRIER
	ERROR_FILE = 'call_error_ttyUSB{}'.format(SOCKET_NUMBER)

	while True:
		# Проверем удолетворяет ли текущее время аргументам time_control()
		if time_control():
			log_push(type='success', message='Текущее время входит в интервал времени рассылки')
			# Забираем номер из файла со списком номеров
			NUMBER_DATA = line_pull_from_file(file=NUMBER_LIST_FILE, log_file=LOG_FILE)
			# Если номер успешно получен
			if NUMBER_DATA:
				# Отделяем номер от счетчика попыток дозвона
				NUMBER = NUMBER_DATA.split('|')[0]
				RETRY_COUNT = int(NUMBER_DATA.split('|')[1])
				log_push(message='Получен номер для звонка \'{}\' Счетчик дозвона: {}'.format(NUMBER, RETRY_COUNT))
				# Формируем AT комманду для набора номера
				COMMAND = 'ATD{};'.format(NUMBER)

				SOCKET = serial.Serial('/dev/ttyUSB{}'.format(SOCKET_NUMBER), baudrate=115200, timeout=.1, rtscts=0)

				if SOCKET.isOpen():
					log_push(type='success',
					         message='Соединение с устройством /dev/ttyUSB{} установленно'.format(SOCKET_NUMBER))
					# Предаем комманду на дозвон
					SOCKET.write('{}\r\n'.format(COMMAND).encode('utf-8'))
					# Обнуляем список считанных с устройства ответов
					data_array = []
					log_push(message='Попытка дозвона на номер {}'.format(NUMBER))
					# Инициируем переменную "Установка связи" - True
					communication_setup = True
					# Пока переменная "Установка связи" - True
					while communication_setup:
						# Построчно читаем ответы устройства
						data = SOCKET.readline().strip()
						# Если есть ответ от устройства записываем его в список ответов
						if data:
							data_array.append(data)
							log_push(message='Содедержание переменной data_array')
							for i in data_array:
								log_push(message=i)
						# Если есть ответ OK в списке ответов (Связь установленна | Поднята трубка)
						if b'OK' in data_array:
							log_push(type='success', message='Получен код установленного соединения')
							# Обнуляем список считанных с устройства ответов
							data_array = []
							# Инициируем переменную "Связь установленна" - True
							communication_established = True
							# Настраиваем порты GPIO Raspberry Pi 3 model B
							try:
								log_push(message='Настраиваем порты GPIO Raspberry Pi 3 model B')
								GPIO.setmode(GPIO.BCM)
								GPIO.setwarnings(False)
								GPIO.setup(PIN, GPIO.OUT)
								# Включаем mp3 плеер с записью
								GPIO.output(PIN, True)
								log_push(message='Включен mp3 плеер с записью информационного сообщения')
								# Создаем метку начала отсчета времени
								start_time = time.time()
								# Пока "Связь установленна" - True
								while communication_established:
									# Построчно читаем ответы устройства
									data = SOCKET.readline().strip()
									# Если есть ответ от устройства записываем его в список ответов
									if data:
										data_array.append(data)
										log_push(message='Содедержание переменной data_array')
										for i in data_array:
											log_push(message=i)
									# Если есть ответ NO CARRIER в списке ответов (номер разорвал соединение)
									if b'NO CARRIER' in data_array:
										log_push(type='warning', message='Получен код разрыва соединения')
										# Обнуляем список считанных с устройства ответов
										data_array = []
										# Создаем метку конца отсчета времени
										stop_time = time.time()
										# Выключаем mp3 плеер с записью
										GPIO.output(PIN, False)
										log_push(message='Выключен mp3 плеер с записью информационного сообщения')
										# Вычесляем продолжительность вызова
										call_time = stop_time - start_time
										log_push(message='Продолжительность звонка: {} секунд'.format(call_time))
										# Делаем запись в файл успешного дозвона
										line_push_to_file(file=SUCCESS_FILE, log_file=LOG_FILE,
										                  line='{};{}'.format(NUMBER, call_time))
										# Инициируем переменную "Связь установленна" - False
										communication_established = False
									# Вычесляем продолжительность вызова
									call_time = time.time() - start_time
									# Если длительность вызова >= длительности записи сообщения
									if call_time >= SOUND_TIME:
										log_push(
											message='Аудиосообщение продолжительностью {} секунд полностью проигранно'.format(
												call_time))
										# Обнуляем список считанных с устройства ответов
										data_array = []
										# Разрываем соединение
										SOCKET.write('ATH\r\n'.encode('utf-8'))
										log_push(message='Разрыв соединения по таймауту {} секунд'.format(SOUND_TIME))
										# Делаем запись в файл успешного дозвона
										line_push_to_file(file=SUCCESS_FILE, log_file=LOG_FILE,
										                  line='{};{}'.format(NUMBER, call_time))
										# Инициируем переменную "Связь установленна" - False
										communication_established = False
										call_not_finish = True
										while call_not_finish:
											if not b'OK' in data_array:
												# Построчно читаем ответы устройства
												data = SOCKET.readline().strip()
												# Если есть ответ от устройства записываем его в список ответов
												if data:
													data_array.append(data)
													log_push(message='Содедержание переменной data_array')
													for i in data_array:
														log_push(message=i)
												if b'OK' in data_array:
													call_not_finish = False
													# Обнуляем список считанных с устройства ответов
													data_array = []


							# В завершении
							finally:
								# Обнуляем порты GPIO Raspberry Pi 3 model B
								GPIO.cleanup()
								log_push(message='Обнуляем порты GPIO Raspberry Pi 3 model B')
								# Инициируем переменную "Установка связи" - False
								communication_setup = False
								# Обнуляем таймер соединения
								call_time = 0
								SOCKET.close()
						# Если есть ответ BUSY в списке ответов (Вызов отклонен)
						if b'BUSY' in data_array:
							log_push(type='warning', message='Получен код \'Линия занята\'')
							# Обнуляем список считанных с устройства ответов
							data_array = []
							# Если счетчик попыток дозвонов > 0
							if RETRY_COUNT:
								# Заносим номер в файл со списком номеров не ответивших на вызов
								line_push_to_file(file=BUSY_FILE, log_file=LOG_FILE,
								                  line='{}'.format(NUMBER))
								log_push(
									message='Номер {} записан в файл-список \'{}\' неответивших на вызов'.format(NUMBER,
									                                                                             BUSY_FILE))
							# Если счетчик попыток дозвонов = 0
							else:
								# Заносим номер в файл со списком номеров для обзвона на 10-ю позицию
								line_push_to_file(file=NUMBER_LIST_FILE, log_file=LOG_FILE,
								                  line='{}|1'.format(NUMBER), index=9)
								log_push(
									message='Номер {} записан в файл-список \'{}\' на 10-ю позицию для повторной попытки дозвона'.format(
										NUMBER,
										NUMBER_LIST_FILE))
							# Инициируем переменную "Установка связи" - False
							communication_setup = False

							# Если есть ответ NO ANSWER в списке ответов (Вызов отклонен)
							if  b'NO ANSWER' in data_array:
								log_push(type='warning', message='Получен код \'Таймаут ожидания ответа на вызов\'')
								# Обнуляем список считанных с устройства ответов
								data_array = []
								# Если счетчик попыток дозвонов > 0
								if RETRY_COUNT:
									# Заносим номер в файл со списком номеров не ответивших на вызов
									line_push_to_file(file=BUSY_FILE, log_file=LOG_FILE,
									                  line='{}'.format(NUMBER))
									log_push(
										message='Номер {} записан в файл-список \'{}\' неответивших на вызов'.format(
											NUMBER,
											BUSY_FILE))
								# Если счетчик попыток дозвонов = 0
								else:
									# Заносим номер в файл со списком номеров для обзвона на 10-ю позицию
									line_push_to_file(file=NUMBER_LIST_FILE, log_file=LOG_FILE,
									                  line='{}|1'.format(NUMBER), index=9)
									log_push(
										message='Номер {} записан в файл-список \'{}\' на 10-ю позицию для повторной попытки дозвона'.format(
											NUMBER,
											NUMBER_LIST_FILE))
								# Инициируем переменную "Установка связи" - False
								communication_setup = False

						# Если есть ответ NO CARRIER в списке ответов (Ошибка соединения)
						if b'NO CARRIER' in data_array:
							log_push(type='error', message='Получен код \'Ошибка дозвона\'')
							# Обнуляем список считанных с устройства ответов
							data_array = []
							# Заносим номер в файл со списком номеров при попытке дозвона на которые возникла ошибка
							line_push_to_file(file=ERROR_FILE, log_file=LOG_FILE,
							                  line='{}'.format(NUMBER))
							log_push(
								message='Номер {} записан в файл-список \'{}\' (Ошибка сети)'.format(
									NUMBER,
									ERROR_FILE))
							# Инициируем переменную "Установка связи" - False
							communication_setup = False
				# Ошибка соединения с устройством
				else:
					log_push(type='error',
					         message='Соединение с устройством \'/dev/ttyUSB{}\' не установленно'.format(SOCKET_NUMBER))
					break
			# Файл со списком номеров пуст
			else:
				log_push(type='error',
				         message='Файл \'{}\' со списком номеров пуст'.format(NUMBER_LIST_FILE))
				data_array = []
				SOCKET.close()
				break
		# Текущее время не удовлетворяет аргументам time_control() - ждем пока удовлетворит
		else:
			waiting = True
			log_push(type='warning', message='Текущее время не входит в интервал времени рассылки')
			log_push(type='warning', message='Ждем разрешения продолжить рассылку от функции \'time_control()\'')
			while waiting:
				if time_control():
					waiting = False
				else:
					time.sleep(60)
