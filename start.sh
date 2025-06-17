#!/bin/bash

echo "Starting RoboPlanner deployment..."

# Install/upgrade pip and requirements
echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn robotics_planner.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 