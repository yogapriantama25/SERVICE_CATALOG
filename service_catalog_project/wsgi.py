"""
WSGI config for service_catalog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_catalog_project.settings')

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Django
import django
django.setup()

# Run migrations and populate data on deployment
try:
    from django.core.management import execute_from_command_line
    
    # Check if database needs setup
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='catalog_category';")
        if not cursor.fetchone():
            # Database is empty, run migrations and populate data
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
            execute_from_command_line(['manage.py', 'populate_data'])
except Exception as e:
    # Log error but continue
    print(f"Setup error (continuing): {e}")

application = get_wsgi_application()

# Vercel compatibility
app = application
