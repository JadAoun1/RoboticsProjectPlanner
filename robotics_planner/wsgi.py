"""
WSGI config for robotics_planner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robotics_planner.settings')

# Debug: Print startup info
print("WSGI Application starting...")
print(f"RENDER environment: {os.environ.get('RENDER', 'Not set')}")
print(f"DATABASE_URL present: {bool(os.environ.get('DATABASE_URL'))}")

# Run migrations on startup if on Render
if os.environ.get('RENDER'):
    print("Running migrations on WSGI startup...")
    try:
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        print("Migrations completed successfully")
        
        # Run production setup
        try:
            execute_from_command_line(['manage.py', 'setup_production'])
            print("Production setup completed")
        except Exception as e:
            print(f"Production setup warning: {e}")
            
    except Exception as e:
        print(f"Migration error: {e}")
        # Continue anyway - don't crash the app

application = get_wsgi_application()

print("WSGI Application ready!")
