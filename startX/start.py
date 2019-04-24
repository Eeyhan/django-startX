from django.urls import path
from app import views


class Common():
    def __init__(self):
        self.applist = []

    def __str__(self):
        return '%s' % self.applist

    def get_urls(self):
        patterns = []

        for item in self.applist:
            patterns.append(path('%s/' % item, views.index))

        return patterns

    @property
    def urls(self):
        return (self.get_urls(), None, None)


common = Common()
