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

application = get_wsgi_application()

# Initialize database for Vercel after Django is fully loaded
if os.environ.get('VERCEL'):
    def ensure_db_setup():
        try:
            import django
            from django.core.management import execute_from_command_line
            from django.db import connection
            
            # Check if tables exist
            with connection.cursor() as cursor:
                try:
                    cursor.execute("SELECT COUNT(*) FROM catalog_category")
                    # Tables exist, check if we have data
                    count = cursor.fetchone()[0]
                    if count == 0:
                        # Tables exist but no data, populate
                        execute_from_command_line(['manage.py', 'populate_data'])
                except:
                    # Tables don't exist, create them
                    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
                    execute_from_command_line(['manage.py', 'populate_data'])
                    
        except Exception as e:
            print(f"Database setup error: {e}")
    
    # Set up database on first request
    ensure_db_setup()

# Vercel compatibility
app = application
