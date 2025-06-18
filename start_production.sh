#!/usr/bin/env bash

echo "Starting production server..."

# Run database migrations and setup
echo "Setting up database..."
python manage.py migrate --noinput
python manage.py setup_production

# Start the server
echo "Starting gunicorn server..."
exec gunicorn robotics_planner.wsgi:application --bind 0.0.0.0:$PORT 