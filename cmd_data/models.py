from django.db import models


class cmd_groups(models.Model):
	# Активно (Можно выводить на сайт)
	active = models.BooleanField(default=True, verbose_name='Выводить на сайт?')
	# Идентификатор группы по прайсу CMD
	id_item = models.IntegerField(default=0, verbose_name='Идентификатор группы по прайсу CMD')
	# Заголовок глобальной группы
	group_title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок группы иследований')
	# Родитель (если это подгруппа)
	parent_group = models.ForeignKey('self')

	def __str__(self):
		return '{} | {} | {} '.format(self.id_item,
		                              self.group_title,
		                              self.parent_group
		                              )

	class Meta:
		verbose_name = 'Группа исследований | CMD'
		verbose_name_plural = 'Группы исследований | CMD'


class cmd_items(models.Model):
	# Активно (Можно выводить на сайт)?
	active = models.BooleanField(default=True, verbose_name='Выводить на сайт?')
	# Идентификатор услуги по прайсу CMD
	id_item = models.CharField(primary_key=True, max_length=255, null=False,
	                           verbose_name='Идентификатор услуги по прайсу CMD')
	# CMD url
	cmd_url = models.CharField(max_length=255, blank=False, verbose_name='Ссылка на описание cmd сайт')
	# Родитель
	# group = models.ForeignKey(cmd_groups, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Группа исследования')
	# Название конкретного исследования
	item_title = models.TextField(null=True, blank=True, verbose_name='Идентификатор ссылки')
	# Цена конкретного исследования
	price_cmd = models.IntegerField(default=None, null=True, blank=True, verbose_name='Цена у CMD')
	# Полное описание исследования
	description = models.TextField(null=True, blank=True, verbose_name='О исследовании')
	# Входит в состав комплексной услуги
	in_group_service = models.BooleanField(default=False, verbose_name='Входит в состав комплексной услуги')
	# __________________________________________________________________________________________________________________
	# Цена конкретного исследования
	price_doctor = models.IntegerField(default=None, null=True, blank=True, verbose_name='Цена для доктора')
	# Разница цены в процентах
	price_difference = models.FloatField(default=None, null=True, blank=True, verbose_name='Разница цены в процентах')
	# Входит в топ 30?
	top_30 = models.BooleanField(default=False, verbose_name='Входит в топ 30?')
	# Время на исследование от
	time_to_result_from = models.PositiveIntegerField(default=1, verbose_name='Время на исследование от')
	# Время на исследование до
	time_to_result_to = models.PositiveIntegerField(blank=True, null=True, verbose_name='Время на исследование до')
	# Этой услугой заказывают
	with_this_order = models.ForeignKey('self')

	# biological_material = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ссылка на описание cmd сайт')
	# result = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ссылка на описание cmd сайт')

	def __str__(self):
		analysis_name_array = self.item_title
		return '{} | {} | Стоимость: D: {} CMD: {} руб.'.format(self.id_item,
		                                                        str(analysis_name_array)[:100],
		                                                        self.price_doctor,
		                                                        self.price_cmd,
		                                                        )

	class Meta:
		verbose_name = 'Исследование | Анализ | CMD'
		verbose_name_plural = 'Исследования | Анализы | CMD'
		ordering = ['-id_item', 'item_title', 'price_cmd', 'price_doctor', 'price_difference']
