from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class App1Config(AppConfig):
    name = 'app1'

    def ready(self):
        autodiscover_modules('startX')
