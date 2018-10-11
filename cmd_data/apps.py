from django.apps import AppConfig


class CmdDataConfig(AppConfig):
    name = 'cmd_data' # Здесь указываем исходное имя приложения
    verbose_name = "Исследования (анализы) лаборатории  CMD"  # А здесь, имя которое необходимо отобразить в админке


