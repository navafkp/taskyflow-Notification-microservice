#!/bin/bash

echo "Waiting for RabbitMQ to be available..."
# Wait for RabbitMQ to be available
while ! timeout 1 bash -c 'until echo "" | nc -z docker-taskyflow-microservice-rabbitmq-container-1 5672; do sleep 1; done'; do sleep 1; done
echo "RabbitMQ is available. Running migrations..."

echo "Waiting for PostgreSQL to be available..."
# Wait for PostgreSQL to be available
while ! timeout 1 bash -c 'until echo "" | nc -z docker-taskyflow-microservice-postgres-notification-1 5432; do sleep 1; done'; do sleep 1; done
echo "PostgreSQL is available. Running migrations..."

# Run migrations
python manage.py makemigrations
sleep 2
python manage.py migrate
sleep 2

echo "Migrations complete. Starting the application..."
# Start the application
exec gunicorn taskynotification.wsgi:application --bind 0.0.0.0:8300 & 

# Check if the Django server is ready
tries=0
while ! curl -s http://localhost:8300/healthcheck/ >/dev/null; do
    sleep 1
    ((tries++))
    if [ "$tries" -gt 30 ]; then
        echo "Error: Django server did not start within a reasonable time."
        exit 1
    fi
done

echo "Django server is ready. Starting the consumer..."
python consumer.py
