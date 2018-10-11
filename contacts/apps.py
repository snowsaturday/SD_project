from django.apps import AppConfig


class ContactsConfig(AppConfig):
    name = 'contacts'  # Здесь указываем исходное имя приложения
    verbose_name = 'Контактная информация'  # А здесь, имя которое необходимо отобразить в админке
