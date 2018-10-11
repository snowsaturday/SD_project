from django.db import models


class employe_speciality(models.Model):
    specialty = models.CharField(max_length=50, verbose_name='Специализация сотрудника')

    def __str__(self):
        return '{}'.format(self.specialty)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class employe(models.Model):
    man = models.BooleanField(default=False, verbose_name='Мужчина?')
    is_head = models.BooleanField(default=True, verbose_name='Главный врач?')
    is_active = models.BooleanField(default=True, verbose_name='Работает?')
    candidate_of_medical_sciences = models.BooleanField(default=False, verbose_name='Кандидат медицинских наук?')
    surname = models.CharField(max_length=20, blank=False, verbose_name='Фамилия сотрудника')
    name = models.CharField(max_length=20, blank=False, verbose_name='Имя сотрудника')
    second_name = models.CharField(max_length=20, blank=False, verbose_name='Отчество сотрудника')
    birth_day = models.DateField(null=True, blank=True, verbose_name='День рожденья')
    work_with = models.DateField(null=True, blank=True, verbose_name='Поступил на работу')
    phone_mobile = models.IntegerField(null=True, blank=True, verbose_name='Мобильный телефон')
    photo = models.ImageField(null=True, verbose_name='Фото врача')
    specialty = models.CharField(max_length=200, verbose_name='Специализация сотрудника')
    description = models.TextField(null=True, blank=True, verbose_name='Биографические сведения')


    def __str__(self):
        return '{} {} {}'.format(self.surname, self.name, self.second_name)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def specialty_as_list(self):
        return self.specialty.split('|')

    def description_as_list(self):
        return self.description.split('|')


