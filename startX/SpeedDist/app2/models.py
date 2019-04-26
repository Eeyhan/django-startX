from django.db import models


# Create your models here.

class Host(models.Model):
    host = models.CharField(verbose_name='主机名', max_length=32)
    ip = models.GenericIPAddressField(verbose_name='ip')

    def __str__(self):
        return self.host
