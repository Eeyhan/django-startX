from django.db import models


# Create your models here.

class Depart(models.Model):
    title = models.CharField(verbose_name='部门名称', max_length=32, )

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.IntegerField(choices=gender_choices, default=1,verbose_name='性别')
    education_choices = (
        (1, '其他'),
        (2, '大专'),
        (3, '本科'),
        (4, '博士'),
        (5, '硕士'),
    )
    education = models.IntegerField(choices=education_choices, default=1,verbose_name='学历')
    email = models.CharField(max_length=32, verbose_name='邮箱')
    depart = models.ForeignKey(to='Depart', on_delete='cascade', verbose_name='部门')

    def __str__(self):
        return self.name
