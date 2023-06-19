# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app folder containing the code and templates to the container
COPY app/ /app

# Install the required dependencies
RUN pip install flask

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose a different port for the application (e.g., port 8080)
EXPOSE 8080

# Start the Flask application on the specified port
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]