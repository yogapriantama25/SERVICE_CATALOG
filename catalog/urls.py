from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.service_catalog_list, name='service_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]