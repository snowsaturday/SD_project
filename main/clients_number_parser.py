# import csv
#
#
# FILENAME_FROM = "clients.csv"
# FILE_NAME_TO = 'number_to_call'
#
# with open(FILENAME_FROM, 'r') as f:
# 	reader = csv.DictReader(f, delimiter=';')
# 	counter = 0
# 	for line in reader:
# 		if len(line['TEL_1']) == 11:
# 			with open(FILE_NAME_TO, 'a') as ft:
# 				ft.write('{}|0\n'.format(line['TEL_1']))
# 				counter += 1
#
# # регулярное выражение номер телефона
# # /^\s*(\+?(8|7)?([\s()-]*[0-9][\s()-]*){10})?\s*$/
#
# print(counter)


# import requests
# from bs4 import BeautifulSoup
# import re
# import warnings
# warnings.filterwarnings("ignore")
# from requests.auth import HTTPDigestAuth
# url = 'https://lk.megafon.ru/remainders/'
# r = requests.get(url, auth=HTTPDigestAuth('89299405433', 'cjp5g5'))
# sts = r.status_code
# print(sts)
# txt = r.text
# print(txt)
# soup = BeautifulSoup(txt)
# word = soup.find('div', 'gadget-remainders-td gadget-remainders-td-3 gadget-remainders-summ gadget-remainders-mobile')
# word = str(word)
# test = re.sub('\<[^>]*\>', '', word)
# print(test)вов

import pymysql

HOST = '192.168.1.204'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'rR0959379911'
DB_NAME = 'data'
# DB_NAME = 'doctor'

# r[0] - id записи в базе
# r[1].split('\n')[0] - Фамилия
# r[1].split('\n')[1] - Имя
# r[1].split('\n')[2] - Отчество
# r[2] - Пол 1(М) 2(Ж)
# r[3] - Телефон
# r[4] - Доп телефон
# r[6] - День рождения
# r[9] - Просил не слать смс [1|0]
# r[10] - Ребенок [1|0]
# r[12] - Просил не присылать рекламный контент [1|0]

conn = pymysql.connect(host=HOST, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=DB_NAME, charset='utf8')
cur = conn.cursor()
cur.execute("SELECT * FROM client WHERE birthday > \'1983-00-00\' AND birthday < \'1993-00-00\' AND sex = \'1\'")
# cur.execute("SELECT * FROM timetable WHERE time > \'1519344000\' AND expert_id = \'142\'")

counter = 0

for r in cur:
	if not r[9]:
		if int(len(r[3])) == 10:
			if r[3][0] is '9':
				print('8'+r[3]+'|0')
				counter += 1
			if r[4]:
				if r[4][:1] is '9':
					print('8'+r[4]+'|0')
					counter += 1


print(counter)

cur.close()
conn.close()

# x = input('Введите значение: ')
# if not x: x = 'Не введено значение'
# print(x)
