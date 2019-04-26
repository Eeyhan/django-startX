from startX.serivce.v1 import site, StartXHandler, get_field_display, StartXModelForm
from django.urls import path, re_path, reverse
from app1 import models
from django.utils.safestring import mark_safe
from django import forms
from startX.serivce.v1 import Option

class UserForm(StartXModelForm):
    memo = forms.CharField()

    class Meta:
        model = models.UserInfo
        fields = ['name', 'age', 'email', 'memo']


class UserInfoHandler(StartXHandler):
    has_add_btn = True
    model_form_class = UserForm
    per_page_count = 5

    search_group = [
        Option('gender',is_multi=True),
        Option('depart', db_condition={'id__gt': 0})
    ]

    search_list = ['name__contains', 'email__contains']
    action_list = [StartXHandler.action_multi_delete, ]
    list_display = [StartXHandler.display_checkbox,
                    'name', 'age', 'email', 'depart',
                    get_field_display('性别', 'gender'),
                    get_field_display('学历', 'education'),
                    StartXHandler.display_edit, StartXHandler.display_del]

    # def save(self, form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()

    # def get_urls(self):
    #     patterns = [
    #         re_path(r'^list/$', self.changelist),
    #         re_path(r'^add/$', self.add_view),
    #         re_path(r'^change/(\d+)/$', self.change_view),
    #
    #     ]
    #     return patterns


class DepartHander(StartXHandler):
    has_add_btn = True
    order_by = ['-id']
    list_display = ['id', 'title', StartXHandler.display_edit, StartXHandler.display_del]


site.register(models.Depart, DepartHander)
site.register(models.UserInfo, UserInfoHandler)
