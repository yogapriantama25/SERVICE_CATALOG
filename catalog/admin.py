from django.contrib import admin
from .models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'users', 'pic', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'pic', 'created_at']
    search_fields = ['name', 'description', 'users', 'request_method', 'sla', 'pic']
    ordering = ['category', 'name']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Informasi Dasar', {
            'fields': ('category', 'name', 'description', 'is_active')
        }),
        ('Detail Layanan', {
            'fields': ('users', 'request_method', 'sla', 'pic')
        }),
    )
