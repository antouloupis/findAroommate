# app/Dockerfile

FROM python:3.12-bullseye

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for psycopg2 and others
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./findaroommate /app

#Run collectstatic
RUN python manage.py collectstatic --noinput

# Gunicorn will serve the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "findaroommate.wsgi:application"]