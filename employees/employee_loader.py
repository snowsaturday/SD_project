import csv
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudioDoctor_project.settings")
django.setup()

from StudioDoctor_project import settings
from employees.models import employe

FILE_NAME = 'csv/employee.csv'

#HEAD;PHOTO;FULL_NAME;SPECIALITY;BIRTH;WORK_WITH;STUDY

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f, delimiter=";", fieldnames=('HEAD',
                                                            'PHOTO',
                                                            'FULL_NAME',
                                                            'SPECIALITY',
                                                            'BIRTH',
                                                            'WORK_WITH',
                                                            'STUDY',
                                                            )):

        if row['HEAD']:
            HEAD = True
        else:
            HEAD = False

        try:
            WORK_WITH = '{}-{}-{}'.format(row['WORK_WITH'].split('.')[2], row['WORK_WITH'].split('.')[1], row['WORK_WITH'].split('.')[0])
        except:
            WORK_WITH = None

        try:
            BIRTH = '{}-{}-{}'.format(row['BIRTH'].split('.')[2], row['BIRTH'].split('.')[1], row['BIRTH'].split('.')[0])
        except:
            BIRTH = None


        data_set = employe.objects.create(is_head=HEAD,
                                          surname=row['FULL_NAME'].split(' ')[0].strip(),
                                          name=row['FULL_NAME'].split(' ')[1].strip(),
                                          second_name=row['FULL_NAME'].split(' ')[2].strip(),
                                          birth_day=BIRTH,
                                          work_with=WORK_WITH,
                                          specialty=row['SPECIALITY'],
                                          description=row['STUDY'].strip(),
                                          )
        print(row)
