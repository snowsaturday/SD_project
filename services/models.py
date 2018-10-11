from django.db import models


class service_group(models.Model):

    name = models.CharField(max_length=100, blank=False, verbose_name='Название группы услуг')
    specialist_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название для главной')
    is_main = models.BooleanField(default=False, verbose_name='Выводить группу на главную страницу раздела')
    is_active = models.BooleanField(default=True, verbose_name='Выводить в категории на сайт?')
    group_description = models.TextField(blank=True, verbose_name='Информация относящаяся ко всей группе')
    icon = models.ImageField(null=True, blank=True, verbose_name='Иконка категории ')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class service(models.Model):

    name = models.CharField(max_length=300, verbose_name='Название услуги')
    group = models.ForeignKey(service_group, on_delete=models.CASCADE, verbose_name='Название группы услуг')
    add_to_group = models.IntegerField(null=True, verbose_name='Дополнительно загружать услугу в группы')
    price_from = models.IntegerField(blank=False, null=True, verbose_name='Цена от')
    price_to = models.IntegerField(blank=True, null=True, verbose_name='Цена до')
    to_order = models.BooleanField(default=False, verbose_name='Тербуется предварительный заказ')
    service_time = models.IntegerField(blank=True, null=True, verbose_name='Продолжительность услуги')
    manufacturer_country = models.CharField(max_length=20, blank=True, null=True, verbose_name='Страна производитель')
    description = models.TextField(blank=True, null=True, verbose_name='Описание услуги')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
