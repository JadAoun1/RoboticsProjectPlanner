# Robotics Project Planner - Deployment Guide

This guide covers deploying your Django application to various platforms.

## Prerequisites

1. PostgreSQL configured locally
2. All dependencies installed: `pip install -r requirements.txt`
3. Environment variables configured in `.env`

## Local PostgreSQL Setup

1. **Update `.env` file** with your PostgreSQL password:

   ```
   DATABASE_PASSWORD=your_actual_postgres_password
   ```

2. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Test locally:**
   ```bash
   python manage.py runserver
   ```

## Deployment Options

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI:** https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku:**

   ```bash
   heroku login
   ```

3. **Create Heroku app:**

   ```bash
   heroku create your-robotics-planner
   ```

4. **Set environment variables:**

   ```bash
   heroku config:set SECRET_KEY="your-secret-key-here"
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS="your-robotics-planner.herokuapp.com"
   ```

5. **Add PostgreSQL addon:**

   ```bash
   heroku addons:create heroku-postgresql:essential-0
   ```

6. **Deploy:**

   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push heroku main
   ```

7. **Run migrations on Heroku:**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Option 2: PythonAnywhere

1. **Upload your code** to PythonAnywhere
2. **Create a PostgreSQL database** in the Databases tab
3. **Set up environment variables** in your web app configuration
4. **Configure WSGI file** to point to your application
5. **Run migrations** in a console

### Option 3: Railway

1. **Connect GitHub repo** to Railway
2. **Add PostgreSQL service**
3. **Set environment variables**
4. **Deploy automatically** on git push

## Environment Variables for Production

```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgres://user:password@host:port/database
```

## Static Files

The app is configured with WhiteNoise to serve static files in production. Run:

```bash
python manage.py collectstatic
```

## Security Checklist

- [ ] DEBUG=False in production
- [ ] Strong SECRET_KEY
- [ ] ALLOWED_HOSTS properly configured
- [ ] Database password secure
- [ ] SSL/HTTPS enabled
- [ ] Static files properly served

## Troubleshooting

### Database Connection Issues

- Verify PostgreSQL is running
- Check database credentials in .env
- Ensure database exists and user has permissions

### Static Files Not Loading

- Run `python manage.py collectstatic`
- Check STATIC_ROOT and STATIC_URL settings
- Verify WhiteNoise is in MIDDLEWARE

### Migration Errors

- Check database connection
- Run `python manage.py showmigrations`
- Use `python manage.py migrate --fake-initial` if needed
