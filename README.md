# Robotics Project Planner

A Django web application for planning and managing robotics projects with parts, tools, notes, and cost tracking.

## Security Setup

⚠️ **IMPORTANT**: Never commit sensitive information to version control!

### Environment Variables

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your actual values:
   - Generate a new SECRET_KEY for production
   - Set DEBUG=False for production
   - Configure your database credentials
   - Set appropriate ALLOWED_HOSTS

### Generate a New Secret Key for Production

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables (see Security Setup above)

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Features

- User authentication and project management
- Parts tracking with cost estimation
- Tools inventory management
- Project notes and documentation
- Moodboard/inspiration images
- Cost calculation and budgeting

## Security Notes

- All sensitive configuration is handled via environment variables
- Debug mode is disabled by default in production
- Security headers are configured for production deployment
- Database credentials are never hardcoded

## Production Deployment

1. Set environment variables on your server
2. Use a proper WSGI server (gunicorn, uWSGI)
3. Configure HTTPS/SSL
4. Use a production database (PostgreSQL recommended)
5. Set up proper logging and monitoring
