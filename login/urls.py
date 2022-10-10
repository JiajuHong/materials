from django.urls import path
from . import views
urlpatterns = [
    path('customer/', views.show_customer),
    path('order/', views.show_order),
    path('supplier/', views.show_supplier),
    path('line/', views.show_line),
    path('bar/', views.show_bar),
    path('pie/', views.show_pie),
    path('scatter/', views.show_scatter),
    path('radar/', views.show_radar),
    path('dashboard/', views.show_dashboard)
]