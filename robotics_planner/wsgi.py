"""
WSGI config for robotics_planner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robotics_planner.settings')

# Debug: Print startup info
print("WSGI Application starting...")
print(f"RENDER environment: {os.environ.get('RENDER', 'Not set')}")
print(f"DATABASE_URL present: {bool(os.environ.get('DATABASE_URL'))}")

application = get_wsgi_application()

print("WSGI Application ready!")
