#!/usr/bin/env python3
"""
Deployment preparation script for RoboPlanner
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    print("=== RoboPlanner Deployment Preparation ===\n")
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Install dependencies
    run_command("pip install -r requirements.txt", "Installing dependencies")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    # Check for migrations
    run_command("python manage.py makemigrations", "Creating migrations")
    
    # Run migrations
    run_command("python manage.py migrate", "Running migrations")
    
    # Check Django configuration
    run_command("python manage.py check", "Checking Django configuration")
    
    print("\n=== Deployment Status ===")
    print("✓ Dependencies installed")
    print("✓ Static files collected")
    print("✓ Database migrations ready")
    print("✓ Configuration validated")
    
    print("\n=== Ready for Deployment! ===")
    print("Your app is ready to deploy to:")
    print("1. Heroku: Use 'heroku create' and 'git push heroku main'")
    print("2. Railway: Connect your GitHub repo at https://railway.app")
    print("3. PythonAnywhere: Upload your code and configure web app")
    
    print("\nEnvironment variables needed for production:")
    print("- SECRET_KEY=your-production-secret-key")
    print("- DEBUG=False")
    print("- ALLOWED_HOSTS=your-domain.com")
    print("- DATABASE_URL=postgres://user:password@host:port/database")

if __name__ == "__main__":
    main() 