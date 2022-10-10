# Generated by Django 4.0.5 on 2022-06-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_supplier_category_alter_supplier_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '客户管理', 'verbose_name_plural': '客户管理'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '客户ID', 'verbose_name_plural': '订单管理'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-c_time'], 'verbose_name': '登录用户管理', 'verbose_name_plural': '登录用户管理'},
        ),
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=256, verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credibility',
            field=models.CharField(max_length=256, verbose_name='信用等级'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='industry',
            field=models.CharField(max_length=256, verbose_name='行业'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='job',
            field=models.CharField(max_length=256, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=128, verbose_name='客户名'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=256, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='place',
            field=models.CharField(max_length=256, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='recent_time',
            field=models.DateTimeField(verbose_name='最近活跃时间'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='女', max_length=32, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='value',
            field=models.CharField(max_length=256, verbose_name='客户价值'),
        ),
    ]
