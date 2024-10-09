# app/Dockerfile

FROM python:3.12-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for psycopg2 and others
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./findaroommate/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django app into the container
COPY ./findaroommate/ /app/findaroommate

COPY ./findaroommate/manage.py /app/

EXPOSE 8000
