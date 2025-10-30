# Base image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY backend /app

# Expose port
EXPOSE 8000

# Run server via gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cmdb.wsgi:application"]
