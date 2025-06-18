#!/usr/bin/env python
"""
Production startup script for Render deployment
"""
import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    print(f"Command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(f"SUCCESS - {description}")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR - {description}: {e}")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def main():
    print("Starting production server...")
    
    # Debug environment
    port = os.environ.get('PORT', '10000')
    render = os.environ.get('RENDER', 'not set')
    database_url = os.environ.get('DATABASE_URL')
    
    print(f"PORT: {port}")
    print(f"RENDER: {render}")
    print(f"DATABASE_URL present: {'yes' if database_url else 'no'}")
    if database_url:
        print(f"DATABASE_URL starts with: {database_url[:50]}...")
    
    # Show Django database configuration
    print("Checking Django database configuration...")
    if not run_command("python -c \"import django; django.setup(); from django.conf import settings; print('Database engine:', settings.DATABASES['default']['ENGINE']); print('Database name:', settings.DATABASES['default']['NAME'])\"", "Django database config check"):
        print("Django config check failed")
    
    # Run migrations with verbose output
    print("Running database migrations...")
    if not run_command("python manage.py migrate --verbosity=2", "database migrations"):
        print("CRITICAL: Migration failed - this will cause signup errors")
        # Try to show what tables exist
        run_command("python -c \"from django.db import connection; cursor = connection.cursor(); cursor.execute(\\\"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';\\\"); print('Existing tables:', [row[0] for row in cursor.fetchall()])\"", "list existing tables")
    else:
        print("Migrations completed successfully")
    
    # Verify auth_user table exists
    print("Verifying auth_user table exists...")
    if not run_command("python -c \"from django.contrib.auth.models import User; print('User table exists, count:', User.objects.count())\"", "verify auth_user table"):
        print("CRITICAL: auth_user table does not exist")
        sys.exit(1)
    
    # Run production setup
    if not run_command("python manage.py setup_production", "production setup"):
        print("Warning: Production setup failed, continuing anyway...")
    
    # Start gunicorn
    gunicorn_cmd = f"gunicorn robotics_planner.wsgi:application --bind 0.0.0.0:{port} --workers 1 --timeout 120 --log-level info"
    print(f"Starting server: {gunicorn_cmd}")
    
    # Use exec to replace the current process
    os.execvp("gunicorn", [
        "gunicorn",
        "robotics_planner.wsgi:application",
        "--bind", f"0.0.0.0:{port}",
        "--workers", "1",
        "--timeout", "120",
        "--log-level", "info"
    ])

if __name__ == "__main__":
    main() 