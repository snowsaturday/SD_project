import csv
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudioDoctor_project.settings")
django.setup()

from StudioDoctor_project import settings
from services.models import service


FILE_NAME = 'csv/price.csv'

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f, delimiter=";", fieldnames=('ID',
                                                            'CATEGORY',
                                                            'ADD_TO_CATEGORY',
                                                            'SERVICE',
                                                            'TIME',
                                                            'COUNTRY',
                                                            'COST_FROM',
                                                            'COST_TO',
                                                            'ON_ORDER',
                                                            'DESCRIPTION',
                                                            '',)):
        print(row)

        if row['ON_ORDER']:
            ON_ORDER = True
        else:
            ON_ORDER = False

        if not row['COST_TO']:
            row['COST_TO'] = 0

        if not row['TIME']:
            row['COST_TO'] = 0

        data_set = service.objects.create(name=row['SERVICE'].strip(),
                                          group_id=row['ID'].strip(),
                                          add_to_group=row['ADD_TO_CATEGORY'].strip(),
                                          price_from=int(row['COST_FROM']),
                                          price_to= int(row['COST_TO']),
                                          to_order=ON_ORDER,
                                          service_time=int(row['TIME']),
                                          manufacturer_country=row['COUNTRY'].strip(),
                                          description=row['DESCRIPTION'].strip(),
                                          )
        #        data_set.save()
        print(row)
