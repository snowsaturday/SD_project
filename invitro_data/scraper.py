import django
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudioDoctor_project.settings")
django.setup()

from StudioDoctor_project import settings
from invitro_data.models import *

from scraping_bot import phantom
from bs4 import BeautifulSoup as bs

BASE_URL = invitro_base_url.objects.all()[0]
BASE_URL = BASE_URL.slug


def _parse_invitro_profile():
    driver = phantom.get_driver()
    driver.implicitly_wait(10)
    driver.get(BASE_URL)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    category = []
    for link in soup.find_all('a'):
        if str(link.get('href'))[:22] == '/analizes/for-doctors/':
            category.append(str(link))

    for data in category[6:23]:
        slug_id = data.split('\"')[1].split('/')[3]
        profile_title = data.split('/')[4][2:-1]
        c = invitro_profile(slug_id=slug_id, profile_title=profile_title)
        c.save()
    driver.close()


def _parse_invitro_group():
    for item in invitro_profile.objects.all():
        SLUG_ID = item.slug_id
        driver = phantom.get_driver()
        driver.implicitly_wait(10)
        driver.get('{}{}'.format(BASE_URL, SLUG_ID))
        html = driver.page_source
        soup = bs(html, 'html.parser')
        table = []
        for tab in soup.find_all('tbody')[4:]:
            table.append(str(tab))

        counter = 0
        for _ in table:
            group_name = table[counter].split('<tr>')[1].split('<')[2][3:].strip()
            print(str(group_name))
            group_id = table[counter].split('<tr>')[2].split('<td>')[2].split('/')[3]
            print(str(group_id))
            counter += 1
            cur = invitro_group(group_title=group_name,
                                slug_id=group_id,
                                profile_id=item.pk
                                )
            cur.save()

        driver.close()


def _parse_invitro_items():
    for item in invitro_group.objects.all():
        SLUG_ID_GROUP = item.slug_id
        driver = phantom.get_driver()
        driver.implicitly_wait(10)
        driver.get('{}{}'.format(BASE_URL, SLUG_ID_GROUP))
        html = driver.page_source
        soup = bs(html, 'html.parser')
        table = []
        for tab in soup.find_all('tbody'):
            table.append(str(tab))

        data_string = table[3].split('<tr>')

        for _ in data_string[2:]:
            name = _.split('<td>')[2].split('/')[5][2:-1]
            SLUG_ID_ITEM = _.split('<td>')[2].split('/')[4]
            code = _.split('<td>')[1].split('</td>')[0].strip()
            price = _.split('<td>')[3].split('</td>')[0].strip()

            driver.get('{}{}/{}'.format(BASE_URL, SLUG_ID_GROUP, SLUG_ID_ITEM))
            html = driver.page_source
            soup = bs(html, 'html.parser')
            for tab in soup.find_all(class_='tabs_block'):
                # Нормализуем данные
                tab = str(tab).replace('\n', '')
                tab = str(tab).replace('<br>', '')
                tab = str(tab).replace('<br><br>', '')
                tab = str(tab).replace('</br>', '')
                tab = str(tab).replace('<strong>', '<strong><br>')
                tab = str(tab).replace('<b>', '<strong><br>')
                tab = str(tab).replace('</b>', '</strong>')
                tab = str(tab).replace('<font color="#00736a">', '')
                tab = str(tab).replace('<font color="#000000">', '')
                tab = str(tab).replace('<font color="#008080">', '')
                tab = str(tab).replace('<p style="color:#008285;">', '<p>')
                tab = str(tab).replace('<p style="font-weight:bold; text-align:justify; font-size:13px;">', '<p>')
                tab = str(tab).replace('<font color="#ff0000">', '')
                tab = str(tab).replace('<font color="#FF0000">', '')
                tab = str(tab).replace('</font>', '')
                tab = str(tab).replace('tab_cont small_text', 'small_text')
                tab = str(tab).replace('style="display:none;"', '')
                tab = str(tab).replace('<strong><br></strong>', '')
                tab = str(tab).replace('<strong></strong>', '')
                tab = str(tab).replace('<div></div>', '')
                tab = str(tab).replace('<strong><br><br><strong>', '<strong>')
                tab = str(tab).replace('<strong><strong>', '<strong>')
                tab = str(tab).replace('</strong><strong>', '')
                tab = str(tab).replace('</strong></strong>', '</strong>')
                tab = str(tab).replace('/analizes/for-doctors/', '/analizes/')
                tab = str(tab).replace('https://www.invitro.ru', '')
                tab = str(tab).replace('http://www.invitro.ru', '')
                tab = str(tab).replace('invitro.ru', '')
                # Регулярное выражение для поиска ссылок на картинки
                regular = re.compile(
                    r'<div align="center" class="import_div"><a href=".*" onclick=".*"><img class=".*" height=".*" src=".*" width=".*"> </img></a></div>*.'
                )
                tab = re.sub(regular, '', str(tab))
                tab = re.sub(r'\s+', ' ', str(tab))

                # Тут что-то сломалось - будет время разобраться
                tab = str(tab).replace('div align="justify">', '<div align="justify">')
                tab = str(tab).replace('<<', '<')

                # Разбрендирование статей
                tab = str(tab).replace('в лаборатории ИНВИТРО', 'в медицинском центре СТУДИЯ ДОКТОР')
                tab = str(tab).replace('в Независимой лаборатории ИНВИТРО', 'в медицинском центре СТУДИЯ ДОКТОР')
                tab = str(tab).replace('ИНВИТРО', 'СТУДИЯ ДОКТОР')

                cur = invitro_items(group_id=item.pk,
                                    analysis_name=name,
                                    price=price,
                                    code=code,
                                    description=tab,
                                    slug_id=SLUG_ID_ITEM
                                    )
                cur.save()

                if settings.DEBUG:
                    print(
                        '-----------------------------------------------------------------------------------------------')
                    print('Обработан адрес {}{}/{}'.format(BASE_URL, SLUG_ID_GROUP, SLUG_ID_ITEM))
                    print(
                        'В базу сделана запись: {} | {} | {} | (Описание длинной {} символов)'.format(code, name, price,
                                                                                                      len(str(tab))))
                    print(
                        '-----------------------------------------------------------------------------------------------')
    driver.close()

if __name__ == '__main__':
    #_parse_invitro_profile()
    #_parse_invitro_group()
    _parse_invitro_items()
