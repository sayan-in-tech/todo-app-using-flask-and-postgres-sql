FROM python:3.13.1-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

# # Set the working directory
# WORKDIR /app
# # Copy the everything into the container at /app
# COPY . /app
# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
# # Expose the port the app runs on
# EXPOSE 5000
# # Run the application
# CMD ["python", "app.py"]
