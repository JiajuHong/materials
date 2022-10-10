from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="名称")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.EmailField(unique=True, verbose_name="邮箱")
    sex = models.CharField(max_length=32, choices=[("male", "男"), ("female", "女")], default="男", verbose_name="性别")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "登录用户管理"
        verbose_name_plural = "登录用户管理"


class Customer(models.Model):
    name = models.CharField(max_length=128, verbose_name="客户名")
    phone = models.CharField(max_length=256, verbose_name="联系电话")
    email = models.EmailField(verbose_name="邮箱")
    sex = models.CharField(max_length=32, choices=[("男", "男"), ("女", "女")], default="男", verbose_name="性别")
    register_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    recent_time = models.DateTimeField(verbose_name="最近活跃时间")
    credibility = models.CharField(max_length=256, verbose_name="信用等级")  # 信用,高 中 低
    job = models.CharField(max_length=256, verbose_name="职业")
    industry = models.CharField(max_length=256, verbose_name="行业")
    place = models.CharField(max_length=256, verbose_name="地址")
    company = models.CharField(max_length=256, verbose_name="公司")
    value = models.CharField(max_length=256, verbose_name="客户价值")  # 客户的价值,高,中,低

    class Meta:
        verbose_name = "客户管理"
        verbose_name_plural = "客户管理"

    def __str__(self):
        return self.name


class Order(models.Model):
    def __str__(self):
        return str(self.customer.id)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_name = models.CharField(max_length=256, verbose_name="订单名")
    Signed_time = models.DateTimeField(verbose_name="签订时间")
    cost = models.IntegerField(default=0, verbose_name="成本")
    price = models.IntegerField(default=0, verbose_name="价格")
    status = (
        (1, "签订"),
        (2, "未签订"),
        (3, "违约"))
    order_status = models.IntegerField(choices=status, default="签订", verbose_name="订单状态")

    class Meta:
        verbose_name = "客户ID"
        verbose_name_plural = "订单管理"


class Supplier(models.Model):
    name = models.CharField(max_length=128, verbose_name="供应商名称")
    category = models.CharField(max_length=256, verbose_name="供货类别")
    city = models.CharField(max_length=256, verbose_name="供货城市")
    phone = models.CharField(max_length=256, verbose_name="联系电话")
    time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "供应商管理"
        verbose_name_plural = "供应商管理"
