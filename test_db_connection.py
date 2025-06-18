#!/usr/bin/env python
"""
Test database connectivity
"""
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robotics_planner.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User

def test_database():
    print("Testing database connection...")
    
    try:
        # Test basic connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        print("Database connection: SUCCESS")
        
        # Test if auth tables exist
        try:
            user_count = User.objects.count()
            print(f"User table accessible: SUCCESS (count: {user_count})")
        except Exception as e:
            print(f"User table error: {e}")
            return False
        
        # Test creating a user
        try:
            test_user = User.objects.create_user(
                username='testuser123',
                email='test@example.com',
                password='testpass123'
            )
            print(f"User creation: SUCCESS (created user: {test_user.username})")
            
            # Clean up
            test_user.delete()
            print("User deletion: SUCCESS")
            
        except Exception as e:
            print(f"User creation error: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"Database connection error: {e}")
        return False

if __name__ == "__main__":
    success = test_database()
    if success:
        print("All database tests passed!")
    else:
        print("Database tests failed!")
        exit(1) 