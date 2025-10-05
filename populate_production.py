#!/usr/bin/env python3
"""
Post-deployment script to populate database with sample data.
Run this after deploying to production to get sample data.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_catalog_project.settings')
django.setup()

from catalog.models import Category, Service

def populate_data():
    """Populate database with sample data"""
    print("🚀 Starting data population...")
    
    # Create Categories
    categories_data = [
        'Autentikasi & Akses',
        'Aplikasi Akademik', 
        'Infrastruktur IT',
        'Email & Komunikasi',
        'Website & Portal',
        'Dukungan Teknis'
    ]

    categories = {}
    for cat_name in categories_data:
        category, created = Category.objects.get_or_create(name=cat_name)
        categories[cat_name] = category
        if created:
            print(f"✅ Created category: {cat_name}")

    # Create Services (sample data)
    services_data = [
        {
            'category': 'Autentikasi & Akses',
            'name': 'Single Sign-On (SSO)',
            'description': 'Layanan autentikasi terpusat untuk akses ke semua sistem UMKT dengan satu akun',
            'users': 'Dosen, Mahasiswa, Staf',
            'request_method': 'Helpdesk IT atau Portal Helpdesk',
            'sla': 'Respon 30 menit, selesai dalam 2 jam',
            'pic': 'Tim Infrastruktur'
        },
        {
            'category': 'Email & Komunikasi',
            'name': 'Email UMKT',
            'description': 'Layanan email resmi dengan domain @umkt.ac.id untuk civitas akademika',
            'users': 'Dosen, Staf',
            'request_method': 'Form online di portal atau Helpdesk IT',
            'sla': 'Respon 1 jam, selesai dalam 24 jam',
            'pic': 'Tim Aplikasi'
        },
        # Add more sample services as needed
    ]

    for service_data in services_data:
        category = categories[service_data['category']]
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            category=category,
            defaults={
                'description': service_data['description'],
                'users': service_data['users'],
                'request_method': service_data['request_method'],
                'sla': service_data['sla'],
                'pic': service_data['pic']
            }
        )
        if created:
            print(f"✅ Created service: {service_data['name']}")

    print("🎉 Data population completed successfully!")
    print(f"📊 Total categories: {Category.objects.count()}")
    print(f"📋 Total services: {Service.objects.count()}")

if __name__ == '__main__':
    populate_data()