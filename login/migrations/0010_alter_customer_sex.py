# Generated by Django 4.0.5 on 2022-06-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_customer_sex_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=32, verbose_name='性别'),
        ),
    ]
