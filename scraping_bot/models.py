from django.db import models


class bot_settings(models.Model):
    proxy_enable = models.BooleanField(default=False, verbose_name='Активный прокси')
    proxy_ip = models.GenericIPAddressField(null=True)
    proxy_port = models.CharField(max_length=5, null=True)

    def __str__(self):
        if self.proxy_enable:
            return '[+] Проксирование по адресу | {}:{}'.format(self.proxy_ip, self.proxy_port)
        else:
            return '[-] Проксирование по адресу | {}:{}'.format(self.proxy_ip, self.proxy_port)

    class Meta:
        verbose_name = 'Прокси сервер'
        verbose_name_plural = 'Прокси серверы'
