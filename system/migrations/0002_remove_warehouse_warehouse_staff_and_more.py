# Generated by Django 4.0.5 on 2022-06-20 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='warehouse_staff',
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.warehouse', verbose_name='负责库房'),
        ),
    ]