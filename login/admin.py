from django.contrib import admin

# Register your models here.
from login.models import User, Customer, Order, Supplier


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'email', 'c_time')
    list_per_page = 10
    search_fields = ('id', 'name',)
    list_filter = ('sex', )
    ordering = ('-c_time',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'sex', 'register_time',
                    'recent_time', 'credibility', 'job', 'industry', 'place',
                    'company', 'value')
    search_fields = ('name', 'phone',)
    list_filter = ('credibility', 'value', 'sex')
    ordering = ('-register_time',)
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_name', 'Signed_time', 'price', 'order_status', '__str__')
    search_fields = ('id',)
    list_filter = ('order_status', 'order_name')
    ordering = ('-Signed_time',)
    list_per_page = 10


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'city', 'phone', 'time')
    search_fields = ('id', 'name',)
    list_filter = ('category', 'city',)
    ordering = ('-time',)
    list_per_page = 10
