from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название организации')
    map = models.TextField(verbose_name='Код карты')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    phone_number_additional_1 = models.CharField(max_length=15, blank=True, verbose_name='Номер телефона дополнительный')
    phone_number_additional_2 = models.CharField(max_length=15, blank=True, verbose_name='Номер телефона дополнительный')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
