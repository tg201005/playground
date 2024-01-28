# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    dumb-init \
    netcat-openbsd \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip\
    && pip install django \
    && pip install requests django-oauth-toolkit django-cors-headers \
    && pip install python-dotenv



# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app/myproject
COPY ./myproject/ /usr/src/app/myproject

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
