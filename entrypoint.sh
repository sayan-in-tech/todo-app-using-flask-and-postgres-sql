#!/bin/bash
set -e

echo "Waiting for PostgreSQL to start..."
# Wait for PostgreSQL to be ready on the host machine
while ! pg_isready -h host.docker.internal -p 5432 -U postgres; do
  echo "PostgreSQL is not ready yet... waiting"
  sleep 2
done
echo "PostgreSQL is up - starting application"

# Run the application
exec python app.py