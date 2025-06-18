from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Set up production database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Setting up production database...')
        
        # Test database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                self.stdout.write(self.style.SUCCESS('Database connection successful'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database connection failed: {e}'))
            return
        
        # Check if auth_user table exists
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'auth_user')")
                auth_user_exists = cursor.fetchone()[0]
                if auth_user_exists:
                    self.stdout.write(self.style.SUCCESS('auth_user table exists'))
                else:
                    self.stdout.write(self.style.WARNING('auth_user table does not exist - migrations needed'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Could not check auth_user table: {e}'))
        
        # Run migrations
        try:
            self.stdout.write('Running database migrations...')
            call_command('migrate', verbosity=2)
            self.stdout.write(self.style.SUCCESS('Migrations completed'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Migration failed: {e}'))
            return
        
        # Verify User model works
        try:
            user_count = User.objects.count()
            self.stdout.write(self.style.SUCCESS(f'User model accessible - current count: {user_count}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'User model not accessible: {e}'))
            return
        
        # Create superuser if it doesn't exist
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
                self.stdout.write(self.style.SUCCESS('Superuser "admin" created (password: admin123)'))
            else:
                self.stdout.write(self.style.WARNING('Superuser "admin" already exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Superuser creation failed: {e}'))
        
        self.stdout.write(self.style.SUCCESS('Production setup complete!')) 