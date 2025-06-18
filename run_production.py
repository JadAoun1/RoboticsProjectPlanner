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
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error in {description}: {e}")
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
    
    # Run migrations
    if not run_command("python manage.py migrate --noinput", "database migrations"):
        sys.exit(1)
    
    # Run production setup
    if not run_command("python manage.py setup_production", "production setup"):
        print("Warning: Production setup failed, continuing anyway...")
    
    # Start gunicorn
    gunicorn_cmd = f"gunicorn robotics_planner.wsgi:application --bind 0.0.0.0:{port} --workers 1 --timeout 120"
    print(f"Starting server: {gunicorn_cmd}")
    
    # Use exec to replace the current process
    os.execvp("gunicorn", [
        "gunicorn",
        "robotics_planner.wsgi:application",
        "--bind", f"0.0.0.0:{port}",
        "--workers", "1",
        "--timeout", "120"
    ])

if __name__ == "__main__":
    main() 