# Generated by Django 4.0.5 on 2022-06-20 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouse_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='仓库编号')),
                ('warehouse_name', models.CharField(max_length=10, verbose_name='仓库名称')),
                ('warehouse_type', models.CharField(max_length=10, verbose_name='存放类别')),
                ('warehouse_staff', models.CharField(max_length=10, verbose_name='负责人')),
            ],
            options={
                'verbose_name': '仓库管理',
                'verbose_name_plural': '仓库管理',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='员工编号')),
                ('staff_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('staff_sex', models.CharField(max_length=10, verbose_name='性别')),
                ('staff_warehouse', models.ForeignKey(default='01', on_delete=django.db.models.deletion.CASCADE, to='system.warehouse')),
            ],
            options={
                'verbose_name': '员工管理',
                'verbose_name_plural': '员工管理',
            },
        ),
    ]