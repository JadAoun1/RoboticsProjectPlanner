#!/usr/bin/env bash

echo "Starting production server..."

# Debug: Print environment info
echo "Environment variables:"
echo "PORT: ${PORT:-'not set'}"
echo "RENDER: ${RENDER:-'not set'}"
echo "DATABASE_URL present: $(if [ -n "$DATABASE_URL" ]; then echo 'yes'; else echo 'no'; fi)"

# Set default port if not provided
PORT=${PORT:-10000}
echo "Using port: $PORT"

# Run database migrations and setup
echo "Setting up database..."
python manage.py migrate --noinput
python manage.py setup_production

# Start the server
echo "Starting gunicorn server on 0.0.0.0:$PORT..."
exec gunicorn robotics_planner.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --timeout 120 