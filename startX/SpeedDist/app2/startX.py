from startX.serivce.v1 import site, StartXHandler
from django.shortcuts import HttpResponse
from app2 import models
from django.urls import path, re_path, reverse
from django.utils.safestring import mark_safe


class HostHandler(StartXHandler):
    list_display = ['id', 'host', 'ip', StartXHandler.display_edit, StartXHandler.display_del]

    def extra_url(self):
        return [
            re_path(r'^detail/$', self.detail_view)
        ]

    def detail_view(self, request):
        return HttpResponse('主机列表详情')

    # def get_list_display(self):
    #     return ['host']


site.register(models.Host, HostHandler, prev='public')
