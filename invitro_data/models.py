from django.db import models


class invitro_base_url(models.Model):
    slug = models.URLField(verbose_name='Базовый URL')

    # Базовый URL для парсера

    def __str__(self):
        title = 'Базовый URL таблицы исследований INVITRO | {}'.format(self.slug)
        return title

    class Meta:
        verbose_name = 'Базовый URL'
        verbose_name_plural = 'Базовый URL'


class invitro_profile(models.Model):
    profile_title = models.CharField(max_length=255, blank=False, verbose_name='Профиль исследований')
    # Глобальная группа исследований (например: Исследования крови)
    slug_id = models.CharField(max_length=10, null=True, verbose_name='Идентификатор ссылки')
    # id списка групп и исследований включенных в глобальную группу

    def __str__(self):
        return '{} | INVITRO PROFILE ID - {}'.format(self.profile_title,
                                                     self.slug_id
                                                     )

    class Meta:
        verbose_name = 'Глобальная группа исследования'
        verbose_name_plural = 'Глобальные группы исследований'


class invitro_group(models.Model):
    group_title = models.CharField(max_length=255, blank=False, verbose_name='Имя группы исследований')
    # Более узкая группа исследований (например: Клинический анализ крови)
    profile = models.ForeignKey(invitro_profile, on_delete=models.CASCADE, verbose_name='Профиль исследований')
    # Родитель - глобальная группа
    slug_id = models.CharField(max_length=10, null=True, verbose_name='Идентификатор ссылки')

    # id списка исследований включенных в группу

    def __str__(self):
        return '{} | INVITRO GROUP ID - {}'.format(self.group_title,
                                                   self.slug_id
                                                   )

    class Meta:
        verbose_name = 'Узкая группа исследования'
        verbose_name_plural = 'Узкие группы исследований'


class invitro_items(models.Model):
    group = models.ForeignKey(invitro_group, on_delete=models.CASCADE, verbose_name='Название исследования')
    # Родитель - узкая группа
    analysis_name = models.CharField(max_length=255, blank=False, verbose_name='Идентификатор ссылки')
    # Название конкретного исследования
    price = models.IntegerField(default=0, verbose_name='Цена')
    # Цена конкретного исследования
    code = models.CharField(max_length=255, verbose_name='Идентификатор анализа')
    # Номер исследовани по каталогу ИНВИТРО (ХЗ пока зачем)
    slug_id = models.CharField(max_length=10, null=True, verbose_name='Идентификатор ссылки')
    # id полного описания исследования на сайте ИНВИТРО
    description = models.TextField(blank=True, verbose_name='О исследовании')
    # Полное описание исследования

    def __str__(self):
        analysis_name_array = self.analysis_name
        return '{} | {} | Стоимость: {} руб.'.format(self.code,
                                                     str(analysis_name_array)[:100],
                                                     self.price
                                                     )

    class Meta:
        verbose_name = 'Исследование | Анализ'
        verbose_name_plural = 'Исследования | Анализы'
