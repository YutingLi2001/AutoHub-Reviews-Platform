# Use an official Python runtime as a base image
FROM python:3.8.2

# Set environment variables for Django to run in unbuffered mode, recommended for Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define environment variables for static and media files
# These should match the Django settings in settings.py
ENV APP=/app \
    STATIC_URL=/static/ \
    MEDIA_URL=/media/ \
    # Set STATIC_ROOT to the absolute path where collectstatic will collect static files
    STATIC_ROOT=/app/staticfiles \
    # MEDIA_ROOT should be the absolute path where your media files will be stored
    MEDIA_ROOT=/app/mediafiles

# Create the directories for static and media files
RUN mkdir -p $STATIC_ROOT $MEDIA_ROOT

# Install netcat for network utilities
RUN apt-get update \
    && apt-get install -y netcat \
    && apt-get clean

# Set the working directory in the container
WORKDIR $APP

# Install the Python dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Collect static files
RUN python3 manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Give execution rights on the entrypoint script
RUN chmod +x /app/entrypoint.sh

# Define the entrypoint script to start the services
ENTRYPOINT ["/app/entrypoint.sh"]

# Start Gunicorn with 3 worker processes
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "djangobackend.wsgi:application"]
