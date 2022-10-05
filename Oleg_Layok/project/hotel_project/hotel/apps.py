from django.apps import AppConfig


class HotelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotel'

    def ready(self):
        import hotel.signals
        super().ready()