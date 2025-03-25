FROM python:3.8-slim-buster

WORKDIR /app

# Install git for cloning
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/karthikeyan0312/discord_bot_E/ /tmp/app_clone && \
    cp -r /tmp/app_clone/* /app/ && \
    rm -rf /tmp/app_clone

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
