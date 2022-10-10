# Generated by Django 4.0.5 on 2022-06-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_customer_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '登录用户管理', 'verbose_name_plural': '登录用户管理'},
        ),
        migrations.AlterField(
            model_name='order',
            name='Signed_time',
            field=models.DateTimeField(verbose_name='签订时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='成本'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=256, verbose_name='订单名'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, '签订'), (2, '未签订'), (3, '违约')], default='签订', verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=32, verbose_name='性别'),
        ),
    ]