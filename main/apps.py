from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'  # Здесь указываем исходное имя приложения
    verbose_name = 'Главная страница'  # А здесь, имя которое необходимо отобразить в админке
