from django.db import models


# Create your models here.



class licenses(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название лицензии')
    license = models.ImageField(verbose_name='Сканированное изображение лицензии')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'
