# Geniotest

Geniotest is a Django project created by Michael Assanama. It utilizes Redis for caching and Celery for handling asynchronous tasks.

## Prerequisites

Before running the Geniotest project, you need to have Redis and Celery installed. Follow the instructions below to set up your environment.

### Install Redis

1. **Linux:**
   - Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install redis-server
     ```
   - Fedora:
     ```bash
     sudo dnf install redis
     ```
   - Other distributions: Refer to your distribution's package manager.

2. **Mac:**
   ```bash
   brew install redis

3. **Install Celery:**
   ```bash
   pip install celery

4. **Running Redis:**
   ```bash
   redis-server
   ```
   - Start the Redis server using the following command.
  
5. **Running Celery:**
   ```bash
   python3 -m celery -A config worker -l info
   ```
   - To run Celery, use the following command:

6. **Running the Django Project:**
   ```bash
   python manage.py runserver
   ```
   - Make sure you have Python and Django installed. If not, install Django using:
   - Visit http://127.0.0.1:8000/ to access the local development server.
  
  # API Documentation
  Access the API documentation at http://127.0.0.1:8000/documentation for details on available endpoints and usage.


