# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to install dependencies
COPY backend/requirements.txt /app/

# Install the required dependencies (in this case, FastAPI and Uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . /app/backend/server

# Expose port 8000 (the default FastAPI port)
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "backend.server.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
