# Static data for the service catalog - no database required
from datetime import datetime, timedelta
from django.utils import timezone

# Generate some realistic dates
now = timezone.now()
base_date = now - timedelta(days=30)

CATEGORIES = [
    {
        'id': 1,
        'name': 'Autentikasi & Akses',
        'description': 'Layanan autentikasi dan kontrol akses untuk sistem kampus',
        'icon': 'fas fa-shield-alt'
    },
    {
        'id': 2,
        'name': 'Aplikasi Akademik',
        'description': 'Sistem aplikasi untuk kegiatan akademik dan pembelajaran',
        'icon': 'fas fa-graduation-cap'
    },
    {
        'id': 3,
        'name': 'Aplikasi Kepegawaian',
        'description': 'Sistem manajemen kepegawaian dan administrasi SDM',
        'icon': 'fas fa-users'
    },
    {
        'id': 4,
        'name': 'Layanan Pendukung',
        'description': 'Layanan pendukung operasional kampus',
        'icon': 'fas fa-cogs'
    }
]

SERVICES = [
    # Autentikasi & Akses
    {
        'id': 1,
        'name': 'Single Sign-On (SSO)',
        'description': 'Layanan autentikasi terpusat untuk akses ke berbagai sistem kampus',
        'category_id': 1,
        'users': 'Dosen, Mahasiswa, Staf',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 30 menit, selesai 1 jam',
        'pic': 'Tim Infrastruktur',
        'icon': 'fas fa-key',
        'created_at': base_date,
        'updated_at': now - timedelta(days=1)
    },
    {
        'id': 2,
        'name': 'Email UMKT (Google Workspace)',
        'description': 'Layanan email institusi berbasis Google Workspace',
        'category_id': 1,
        'users': 'Dosen, Mahasiswa, Staf',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'Tim Infrastruktur',
        'icon': 'fab fa-google',
        'created_at': base_date,
        'updated_at': now - timedelta(days=2)
    },
    {
        'id': 3,
        'name': 'WiFi Kampus',
        'description': 'Akses internet nirkabel di seluruh area kampus',
        'category_id': 1,
        'users': 'Dosen, Mahasiswa, Staf',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'Tim Jaringan',
        'icon': 'fas fa-wifi',
        'created_at': base_date,
        'updated_at': now - timedelta(days=3)
    },
    {
        'id': 4,
        'name': 'SIAKAD',
        'description': 'Sistem Informasi Akademik untuk administrasi akademik',
        'category_id': 2,
        'users': 'Mahasiswa, Dosen, BAA',
        'request_method': 'Helpdesk / Admin Prodi',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'TIM BAA',
        'icon': 'fas fa-university',
        'created_at': base_date,
        'updated_at': now - timedelta(days=4)
    },
    {
        'id': 5,
        'name': 'PMB Online',
        'description': 'Sistem Penerimaan Mahasiswa Baru secara online',
        'category_id': 2,
        'users': 'Calon Mahasiswa, BAA',
        'request_method': 'Website PMB',
        'sla': 'Respon 30 menit, selesai 1 jam',
        'pic': 'Tim Aplikasi',
        'icon': 'fas fa-user-graduate',
        'created_at': base_date,
        'updated_at': now - timedelta(days=5)
    },
    {
        'id': 6,
        'name': 'E-Learning',
        'description': 'Platform pembelajaran online untuk perkuliahan',
        'category_id': 2,
        'users': 'Mahasiswa, Dosen',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 15 menit, selesai 1 jam',
        'pic': 'Tim Aplikasi',
        'icon': 'fas fa-laptop',
        'created_at': base_date,
        'updated_at': now - timedelta(days=6)
    },
    {
        'id': 7,
        'name': 'My Wisuda',
        'description': 'Sistem pendaftaran dan administrasi wisuda online',
        'category_id': 2,
        'users': 'Mahasiswa, Prodi, BAA',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 15 menit, selesai 1 jam',
        'pic': 'Tim Aplikasi, Tim BAA',
        'icon': 'fas fa-graduation-cap',
        'created_at': base_date,
        'updated_at': now - timedelta(days=7)
    },
    {
        'id': 8,
        'name': 'SIMPEQ',
        'description': 'Sistem Informasi Manajemen Peralatan dan Equipment',
        'category_id': 3,
        'users': 'TKD, Dosen, Tendik',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'Tim Aplikasi',
        'icon': 'fas fa-tools',
        'created_at': base_date,
        'updated_at': now - timedelta(days=8)
    },
    {
        'id': 9,
        'name': 'E-Office',
        'description': 'Sistem administrasi perkantoran elektronik',
        'category_id': 3,
        'users': 'Semua Unit',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'Tim Aplikasi',
        'icon': 'fas fa-briefcase',
        'created_at': base_date,
        'updated_at': now - timedelta(days=9)
    },
    {
        'id': 10,
        'name': 'Helpdesk IT',
        'description': 'Layanan bantuan teknis dan dukungan IT',
        'category_id': 4,
        'users': 'Semua Pengguna',
        'request_method': 'Portal Helpdesk',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'Tim Support',
        'icon': 'fas fa-headset',
        'created_at': base_date,
        'updated_at': now - timedelta(days=10)
    },
    {
        'id': 11,
        'name': 'Aplikasi Absensi',
        'description': 'Sistem absensi digital untuk pegawai',
        'category_id': 4,
        'users': 'Dosen, Tendik',
        'request_method': 'Helpdesk IT',
        'sla': 'Respon 1 jam, selesai 1 hari',
        'pic': 'Tim Aplikasi',
        'icon': 'fas fa-clock',
        'created_at': base_date,
        'updated_at': now - timedelta(days=11)
    }
]

def get_all_categories():
    """Get all categories"""
    return CATEGORIES

def get_category_by_id(category_id):
    """Get a specific category by ID"""
    try:
        category_id = int(category_id)
        for category in CATEGORIES:
            if category['id'] == category_id:
                return category
    except (ValueError, TypeError):
        pass
    return None

def get_all_services():
    """Get all services"""
    return SERVICES

def get_service_by_id(service_id):
    """Get a specific service by ID"""
    try:
        service_id = int(service_id)
        for service in SERVICES:
            if service['id'] == service_id:
                return service
    except (ValueError, TypeError):
        pass
    return None

def get_services_by_category(category_id):
    """Get all services for a specific category"""
    try:
        category_id = int(category_id)
        return [service for service in SERVICES if service['category_id'] == category_id]
    except (ValueError, TypeError):
        return []

def search_services(query):
    """Search services by name or description"""
    if not query:
        return SERVICES
    
    query = query.lower()
    results = []
    
    for service in SERVICES:
        if (query in service['name'].lower() or 
            query in service['description'].lower() or
            query in service['pic'].lower()):
            results.append(service)
    
    return results

def get_category_name(category_id):
    """Get category name by ID"""
    category = get_category_by_id(category_id)
    return category['name'] if category else 'Unknown Category'

def get_dashboard_stats():
    """Get dashboard statistics"""
    total_services = len(SERVICES)
    total_categories = len(CATEGORIES)
    total_users = sum(service['users'] for service in SERVICES)
    
    # Calculate average SLA
    sla_hours = []
    for service in SERVICES:
        sla = service['sla']
        if 'hour' in sla:
            hours = int(sla.split()[0])
            sla_hours.append(hours)
        elif 'minute' in sla:
            minutes = int(sla.split()[0])
            sla_hours.append(minutes / 60)
    
    avg_sla = sum(sla_hours) / len(sla_hours) if sla_hours else 0
    
    return {
        'total_services': total_services,
        'total_categories': total_categories,
        'total_users': total_users,
        'avg_sla_hours': round(avg_sla, 1)
    }