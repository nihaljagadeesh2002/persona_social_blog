from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"   #doubt whether above line of code is required or not
    name = "users"

    def ready(self):
        import users.signals