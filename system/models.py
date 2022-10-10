from django.db import models


# Create your models here.


class Warehouse(models.Model):
    # 仓库编号
    warehouse_id = models.CharField(max_length=10, primary_key=True,
                                    verbose_name='仓库编号')
    # 仓库名称
    warehouse_name = models.CharField(max_length=10, verbose_name='仓库名称')
    # 存放类别
    warehouse_type = models.CharField(max_length=10, verbose_name='存放类别')

    class Meta:
        verbose_name = "仓库管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.warehouse_id


# 定义员工类
class Staff(models.Model):
    # 员工编号
    staff_id = models.CharField(max_length=10, primary_key=True
                                , verbose_name='员工编号')
    # 员工姓名
    staff_name = models.CharField(max_length=10,
                                verbose_name='姓名')
    # 员工性别
    staff_sex = models.CharField(max_length=10, choices=[("男", "男"), ("女", "女")],
                                null=False,
                                verbose_name="性别")
    # 手机号
    staff_phone = models.CharField(max_length=11, null=True, verbose_name='手机号')
    # 负责库房
    staff_warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE,
                                        verbose_name='负责库房')

    class Meta:
        verbose_name = "负责库房"
        verbose_name_plural = "员工管理"

    def __str__(self):
        return self.staff_warehouse.warehouse_id
