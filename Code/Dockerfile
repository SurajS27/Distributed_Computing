# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the specific chunk file into the container
COPY chunk32/ /app/chunk/

# Copy the Python service file into the container
COPY pi_service.py /app/pi_service.py

# Install any necessary Python packages
RUN pip install flask

# Expose the service port
EXPOSE 5000

# Run the Python service
CMD ["python", "pi_service.py"]
