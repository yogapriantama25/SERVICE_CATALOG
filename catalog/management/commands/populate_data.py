from django.core.management.base import BaseCommand
from catalog.models import Category, Service


class Command(BaseCommand):
    help = 'Populate database with sample service catalog data'

    def handle(self, *args, **options):
        self.stdout.write('Populating service catalog with sample data...')

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
                self.stdout.write(f'Created category: {cat_name}')

        # Create Services
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
            {
                'category': 'Infrastruktur IT',
                'name': 'WiFi Kampus',
                'description': 'Akses internet nirkabel di seluruh area kampus UMKT',
                'users': 'Dosen, Mahasiswa, Staf, Tamu',
                'request_method': 'Registrasi mandiri atau Helpdesk IT',
                'sla': 'Registrasi langsung, troubleshooting 15 menit',
                'pic': 'Tim Infrastruktur'
            },
            {
                'category': 'Aplikasi Akademik',
                'name': 'SIAKAD (Sistem Informasi Akademik)',
                'description': 'Sistem informasi untuk pengelolaan data akademik mahasiswa dan dosen',
                'users': 'Mahasiswa, Dosen, Staf Akademik',
                'request_method': 'Helpdesk IT atau Admin Fakultas',
                'sla': 'Respon 15 menit, troubleshooting 1 jam',
                'pic': 'Tim Aplikasi'
            },
            {
                'category': 'Aplikasi Akademik',
                'name': 'E-Learning Platform',
                'description': 'Platform pembelajaran online untuk mendukung aktivitas perkuliahan',
                'users': 'Dosen, Mahasiswa',
                'request_method': 'Portal e-learning atau Helpdesk IT',
                'sla': 'Respon 30 menit, selesai dalam 4 jam',
                'pic': 'Tim Aplikasi'
            },
            {
                'category': 'Website & Portal',
                'name': 'Website PMB',
                'description': 'Portal penerimaan mahasiswa baru dan informasi pendaftaran',
                'users': 'Calon Mahasiswa, Staf PMB',
                'request_method': 'Website PMB atau Kontak PMB',
                'sla': 'Respon 2 jam, selesai dalam 8 jam',
                'pic': 'Tim Support'
            },
            {
                'category': 'Dukungan Teknis',
                'name': 'Helpdesk IT',
                'description': 'Layanan bantuan teknis untuk semua permasalahan IT di UMKT',
                'users': 'Dosen, Mahasiswa, Staf',
                'request_method': 'Telepon, Email, atau Portal Helpdesk',
                'sla': 'Respon 15 menit, eskalasi sesuai kompleksitas',
                'pic': 'Tim Support'
            },
            {
                'category': 'Infrastruktur IT',
                'name': 'Akses VPN',
                'description': 'Layanan VPN untuk akses sistem internal dari luar kampus',
                'users': 'Dosen, Staf',
                'request_method': 'Form permohonan ke Helpdesk IT',
                'sla': 'Respon 1 jam, setup dalam 24 jam',
                'pic': 'Tim Infrastruktur'
            },
            {
                'category': 'Aplikasi Akademik',
                'name': 'Perpustakaan Digital',
                'description': 'Akses ke koleksi digital dan katalog perpustakaan UMKT',
                'users': 'Mahasiswa, Dosen, Staf',
                'request_method': 'Registrasi di perpustakaan atau online',
                'sla': 'Registrasi langsung, troubleshooting 30 menit',
                'pic': 'Tim Aplikasi'
            },
            {
                'category': 'Website & Portal',
                'name': 'Portal Mahasiswa',
                'description': 'Portal khusus mahasiswa untuk akses informasi akademik dan layanan',
                'users': 'Mahasiswa',
                'request_method': 'Auto-register atau Helpdesk IT',
                'sla': 'Setup otomatis, troubleshooting 30 menit',
                'pic': 'Tim Aplikasi'
            }
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
                self.stdout.write(f'Created service: {service_data["name"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated service catalog with sample data!')
        )