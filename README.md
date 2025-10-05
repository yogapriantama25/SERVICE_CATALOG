# 🎯 Service Catalog UMKT

<div align="center">

![Service Catalog](https://img.shields.io/badge/Service_Catalog-v1.0.0-blue?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-5.2.7-green?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple?style=for-the-badge&logo=bootstrap)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

**Sistem manajemen katalog layanan IT yang modern dan responsif untuk Universitas Muhammadiyah Kalimantan Timur**

[🚀 Demo Live](#) • [📖 Dokumentasi](#fitur) • [🛠️ Instalasi](#instalasi) • [🎨 Preview](#preview)

</div>

---

## 🌟 Preview

### 🎨 Design Modern dengan Brand Colors
- **Primary**: `#003366` (Navy Blue)
- **Secondary**: `#FFAF42` (Warm Orange)
- **Accent**: `#FF8C42` (Bright Orange)

### 📱 Responsive & Professional UI
- Hero section dengan gradient background
- Card-based layout dengan hover effects
- Modern typography dengan Inter font
- Smooth animations dan transitions
- Professional color scheme

## ✨ Fitur

### 🎯 Core Features
- **📋 Katalog Layanan Lengkap**: Daftar semua layanan IT UMKT dengan detail informasi
- **🔍 Pencarian Canggih**: Search real-time dengan multiple filters
- **📊 Dashboard Analytics**: Statistik dan visualisasi data layanan
- **🏷️ Manajemen Kategori**: Organisasi layanan berdasarkan kategori
- **👥 Multi-PIC Support**: Pengelolaan layanan dengan berbagai tim PIC

### 🎨 UI/UX Features
- **🌟 Modern Design**: Clean, professional interface dengan brand colors UMKT
- **📱 Fully Responsive**: Perfect di desktop, tablet, dan mobile
- **🎭 Smooth Animations**: Fade-in effects dan hover transitions
- **🚀 Fast Loading**: Optimized assets dan efficient queries
- **♿ Accessibility**: ARIA labels dan keyboard navigation

### 🔧 Technical Features
- **⚡ High Performance**: Optimized database queries dengan select_related
- **🔒 Secure**: Django security best practices
- **📈 Scalable**: Modular architecture untuk easy expansion
- **🛠️ Admin Interface**: Django admin dengan custom configurations
- **📊 Analytics**: Built-in dashboard dengan real-time statistics

## 🗂️ Struktur Database

### 📋 Model Category
```python
- name: CharField(max_length=100, unique=True)
- created_at: DateTimeField(auto_now_add=True)
- updated_at: DateTimeField(auto_now=True)
```

### 🔧 Model Service
```python
- category: ForeignKey(Category)
- name: CharField(max_length=200)
- description: TextField()
- users: CharField(max_length=255)          # Target pengguna
- request_method: CharField(max_length=255) # Cara request
- sla: CharField(max_length=255)            # Service Level Agreement
- pic: CharField(max_length=100)            # Person in Charge
- is_active: BooleanField(default=True)
- created_at: DateTimeField(auto_now_add=True)
- updated_at: DateTimeField(auto_now=True)
```

## 🚀 Instalasi

### 📋 Prerequisites
- Python 3.10+
- Git
- Virtual Environment

### ⚡ Quick Start

```bash
# 1. Clone repository
git clone <repository-url>
cd service-catalog

# 2. Setup virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Database setup
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Load sample data
python manage.py populate_data

# 7. Start development server
python manage.py runserver
```

### 🌐 Access Points
- **🏠 Homepage**: http://127.0.0.1:8000/
- **📊 Dashboard**: http://127.0.0.1:8000/dashboard/
- **⚙️ Admin Panel**: http://127.0.0.1:8000/admin/

### 🔐 Default Admin Credentials
```
Username: admin
Password: admin123
Email: admin@umkt.ac.id
```

## 🗺️ URL Structure

| URL | View | Description |
|-----|------|-------------|
| `/` | service_list | Homepage dengan daftar semua layanan |
| `/dashboard/` | dashboard | Analytics dashboard |
| `/service/<id>/` | service_detail | Detail layanan specific |
| `/category/<id>/` | category_detail | Layanan berdasarkan kategori |
| `/admin/` | Django Admin | Interface manajemen |

## 🛠️ Tech Stack

### Backend
- **🐍 Django 5.2.7**: Python web framework
- **🗄️ SQLite**: Default database (upgradeable to PostgreSQL)
- **🔧 Django Admin**: Built-in admin interface

### Frontend
- **🎨 Bootstrap 5.3.0**: CSS framework
- **⭐ Font Awesome 6.4.0**: Icon library
- **🔤 Inter Font**: Modern typography
- **✨ Custom CSS**: Brand-specific styling

### Features
- **📱 Responsive Design**: Mobile-first approach
- **🎭 Smooth Animations**: CSS transitions dan JavaScript
- **🔍 Real-time Search**: Dynamic filtering
- **📊 Charts & Analytics**: Custom dashboard

## 📁 Project Structure

```
service-catalog/
├── 📁 catalog/                  # Main Django app
│   ├── 📁 management/          # Custom commands
│   │   └── 📁 commands/
│   │       └── populate_data.py
│   ├── 📁 migrations/          # Database migrations
│   ├── 📁 static/catalog/      # Static assets
│   │   ├── 📁 css/
│   │   │   └── style.css       # Custom styles
│   │   └── 📁 images/
│   ├── 📁 templates/catalog/   # HTML templates
│   │   ├── base.html
│   │   ├── service_list.html
│   │   ├── service_detail.html
│   │   ├── category_detail.html
│   │   └── dashboard.html
│   ├── admin.py               # Admin configuration
│   ├── models.py              # Database models
│   ├── views.py               # View controllers
│   └── urls.py                # URL routing
├── 📁 service_catalog_project/ # Django settings
├── manage.py                  # Django CLI
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## 🎨 Customization

### 🎨 Brand Colors
Edit `catalog/static/catalog/css/style.css`:
```css
:root {
    --primary-color: #003366;    /* Navy Blue */
    --secondary-color: #FFAF42;  /* Warm Orange */
    --accent-color: #FF8C42;     /* Bright Orange */
}
```

### 📊 Dashboard Metrics
Customize in `catalog/views.py` - `dashboard` function:
```python
def dashboard(request):
    # Add custom statistics
    custom_metric = Service.objects.filter(...).count()
    # Add to context
```

### 🎭 Animations
Modify CSS animations in `style.css`:
```css
.fade-in {
    animation: fadeIn 0.6s ease-in-out;
}
```

## 🚀 Production Deployment

### 🔧 Environment Setup
```bash
# Update settings for production
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# Database (PostgreSQL recommended)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # ... config
    }
}
```

### 📦 Static Files
```bash
python manage.py collectstatic
```

### 🌐 Web Server
- **Recommended**: Gunicorn + Nginx
- **Alternative**: Apache + mod_wsgi

## 🤝 Contributing

1. **🍴 Fork** the repository
2. **🌿 Create** feature branch (`git checkout -b feature/AmazingFeature`)
3. **💫 Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **📤 Push** to branch (`git push origin feature/AmazingFeature`)
5. **🔀 Open** Pull Request

## 📞 Support

### 🆘 Getting Help
- **📖 Documentation**: Check this README
- **🐛 Issues**: Create GitHub issue
- **💬 Discussions**: GitHub Discussions

### 📧 Contact
- **🏫 Institution**: Universitas Muhammadiyah Kalimantan Timur
- **📍 Address**: Jl. Ir. H. Juanda No.15, Samarinda, Kaltim
- **📞 Phone**: (0541) 7777039
- **📧 Email**: info@umkt.ac.id

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

**🎯 Made with ❤️ for UMKT IT Services**

[![⭐ Give it a star!](https://img.shields.io/github/stars/username/repo?style=social)](https://github.com/username/repo)

</div>