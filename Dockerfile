FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Make the entry point script executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

# Use our entrypoint script that waits for the DB
ENTRYPOINT ["/app/entrypoint.sh"]