from django.contrib import admin

# Register your models here.
from system.models import Staff, Warehouse


admin.site.site_header = '物料管理系统后台'
admin.site.site_title = '后台登录'


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'staff_sex', '__str__') # 展示字段
    list_per_page = 5 # 每页显示条数
    list_filter = ('staff_sex',)   # 过滤字段 下拉框过滤
    search_fields = ('staff_id', 'staff_name')  # 搜索字段
    # 以员工id排序
    ordering = ('staff_id',)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_id', 'warehouse_name', 'warehouse_type')
    list_per_page = 5
    ordering = ('warehouse_id',)
    search_fields = ('warehouse_id', 'warehouse_name')


