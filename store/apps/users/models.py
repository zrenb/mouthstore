from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100, verbose_name="用户名")

    class Meta:
        db_table = 'zj_users'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Ports(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="用户id")
    port = models.IntegerField(default=0, verbose_name="积分")

    class Meta:
        db_table = 'zj_ports'
        verbose_name = '积分'
        verbose_name_plural = verbose_name
