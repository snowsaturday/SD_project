from django.apps import AppConfig


class BotConfig(AppConfig):
    name = "scraping_bot"  # Здесь указываем исходное имя приложения
    verbose_name = "Настройки скрапера"  # А здесь, имя которое необходимо отобразить в админке

