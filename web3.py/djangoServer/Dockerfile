# Use an official Python runtime as a parent image
FROM python:latest

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
    && pip install requests django-cors-headers \
    && pip install python-dotenv \
    && pip install djangorestframework \
    && pip install web3 solc py-solc-x 

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app/myproject

# Expose port 8000
EXPOSE 8000

# Expose port 8545 for web3
EXPOSE 7545

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
