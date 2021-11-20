from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auth_field = 'django.db.models.BigAutoField'
    name = 'users'
