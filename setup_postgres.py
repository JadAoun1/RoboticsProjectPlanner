#!/usr/bin/env python3
"""
PostgreSQL Database Setup Script for RoboPlanner

This script helps set up the PostgreSQL database for the RoboPlanner application.
Run this after installing PostgreSQL and before running Django migrations.

Usage:
    python setup_postgres.py

Requirements:
    - PostgreSQL installed and running
    - psycopg2-binary installed (included in requirements.txt)
    - .env file configured with database credentials
"""

import os
import sys
from pathlib import Path
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from dotenv import load_dotenv

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Load environment variables
load_dotenv()

def setup_django():
    """Initialize Django settings"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robotics_planner.settings')
    django.setup()

def check_database_connection():
    """Test database connection"""
    try:
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\nPlease ensure:")
        print("1. PostgreSQL is installed and running")
        print("2. Database 'robotics_planner' exists")
        print("3. User 'robotics_user' has proper permissions")
        print("4. .env file has correct database credentials")
        return False

def create_database_instructions():
    """Display database creation instructions"""
    db_name = os.getenv('DATABASE_NAME', 'robotics_planner')
    db_user = os.getenv('DATABASE_USER', 'robotics_user')
    db_password = os.getenv('DATABASE_PASSWORD', 'robotics_password')
    
    print("\n" + "="*60)
    print("PostgreSQL Database Setup Instructions")
    print("="*60)
    print("\n1. Open PostgreSQL command line (psql):")
    print("   psql -U postgres")
    print("\n2. Create database and user:")
    print(f"   CREATE DATABASE {db_name};")
    print(f"   CREATE USER {db_user} WITH PASSWORD '{db_password}';")
    print(f"   GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};")
    print("   \\q")
    print("\n3. Run this script again to test connection")
    print("="*60)

def run_migrations():
    """Run Django migrations"""
    try:
        print("\n🔄 Creating migrations...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        
        print("\n🔄 Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("✅ Migrations completed successfully!")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

def create_superuser_prompt():
    """Prompt to create superuser"""
    create_user = input("\n📝 Would you like to create a superuser account? (y/N): ").lower().strip()
    if create_user in ['y', 'yes']:
        try:
            execute_from_command_line(['manage.py', 'createsuperuser'])
            print("✅ Superuser created successfully!")
        except Exception as e:
            print(f"❌ Superuser creation failed: {e}")

def main():
    """Main setup function"""
    print("🤖 RoboPlanner PostgreSQL Setup Script")
    print("=====================================\n")
    
    # Check if .env file exists
    if not Path('.env').exists():
        print("❌ .env file not found!")
        print("Please copy .env.example to .env and configure your database settings.")
        return
    
    # Initialize Django
    setup_django()
    
    # Test database connection
    if not check_database_connection():
        create_database_instructions()
        return
    
    # Run migrations
    if not run_migrations():
        return
    
    # Offer to create superuser
    create_superuser_prompt()
    
    print("\n🎉 Setup completed successfully!")
    print("You can now run: python manage.py runserver")

if __name__ == "__main__":
    main() 