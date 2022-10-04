from django.apps import AppConfig


class FarmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farm'

    def ready(self):
        from . import signals
