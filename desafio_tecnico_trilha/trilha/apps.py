from django.apps import AppConfig


class TrilhaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trilha'

    def ready(self):
        import trilha.signals