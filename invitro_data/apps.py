from django.apps import AppConfig


class InvitroConfig(AppConfig):
    name = 'invitro_data'  # Здесь указываем исходное имя приложения
    verbose_name = "Исследования (анализы) лаборатории ИНВИТРО"  # А здесь, имя которое необходимо отобразить в админке
