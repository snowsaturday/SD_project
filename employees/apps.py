from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    name = 'employees' # Здесь указываем исходное имя приложения
    verbose_name = "Сотрудники"  # А здесь, имя которое необходимо отобразить в админке