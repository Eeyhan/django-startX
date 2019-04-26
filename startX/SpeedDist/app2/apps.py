from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class App2Config(AppConfig):
    name = 'app2'

    def ready(self):
        autodiscover_modules('startX')
