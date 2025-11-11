# Use Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app

# Expose the port Flask will run on
EXPOSE 5000

# Command to start app
CMD ["python", "app/main.py"]