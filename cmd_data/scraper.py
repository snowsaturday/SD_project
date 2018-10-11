import django
import os
import re
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudioDoctor_project.settings")
django.setup()

from StudioDoctor_project import settings
from cmd_data.models import cmd_items
from cmd_data.models import cmd_groups

from scraping_bot import phantom
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.cmd-online.ru/analizy-i-tseny-po-gruppam/kompleksnyje-programmy-laboratornyh-issledovanij_323/'
ID_ITEM_CMD = []


def clean_id_array():
	with open('cmd_items', 'r') as f:
		id_array = []
		for i in f.readlines():
			if i.strip().isdigit():
				id_array.append(i)
			else:
				print(i)
		with open('cmd_items_filtered', 'w') as ff:
			ff.writelines(id_array)


with open('cmd_items_filtered', 'r') as f:
	for i in f.readlines():
		ID_ITEM_CMD.append(i)


counter = 0
max_items = len(ID_ITEM_CMD)
print(max_items)

try:
	for i in ID_ITEM_CMD:
		CHECK = False
		driver = phantom.get_driver()
		driver.implicitly_wait(10)
		driver.get(BASE_URL)
		find = driver.find_element_by_id("title-search-input")
		find.clear()
		find.send_keys(i)
		time.sleep(5)
		try:
			link_text = driver.find_element_by_class_name('item-search-link').text.strip()
			CHECK = True
		except:
			with open('cmd_items_not_parsed', 'a') as f:
				f.writelines(i)
			print('[-] Нет результатов в поиске по ID')
		if CHECK:
			link_price = driver.find_element_by_class_name('popUp-item-price').text.strip().split(' ')[0]
			link_url = driver.find_element_by_class_name('item-search-link').get_attribute('href')
			print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
			print(i, type(i))
			print(link_text, type(link_text))
			print(link_price)
			print(link_url)
			driver.get(link_url)
			html = driver.page_source
			soup = bs(html, 'html.parser')
			link_description = soup.find(attrs={'class': 'price-more-info-hide'})
			# print(link_description)
			try:
				is_complex = driver.find_element_by_class_name('show-complex-btn')
			except:
				is_complex = None
			finally:
				is_complex_result = False

			if is_complex:
				is_complex_result = True
				print('Входит в состав комплексной услуги')

			cur = cmd_items(
				id_item=i.replace('\n', '').strip(),
				item_title=link_text,
				cmd_url=link_url,
				price_cmd=link_price,
				description=str(link_description),
				in_group_service=is_complex_result

			)
			# print(cur.id_item, '\n', cur.item_title,'\n', cur.cmd_url,'\n', cur.price_cmd,'\n', str(cur.description),'\n',type(str(cur.description)),'\n', cur.in_group_service)
			cur.save()
			counter += 1
			print('Обработанно {} объектов из {}'.format(counter, max_items))
finally:
	if ID_ITEM_CMD:
		pass

	else:
		print('Парсинг успешно завершен')

	if driver:
		driver.close()
