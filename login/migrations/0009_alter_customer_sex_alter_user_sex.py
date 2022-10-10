# Generated by Django 4.0.5 on 2022-06-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_user_options_alter_order_signed_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=32, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32, verbose_name='性别'),
        ),
    ]
