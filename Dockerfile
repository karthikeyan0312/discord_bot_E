FROM python:3.8-slim-buster

WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8502

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "test.py"]
