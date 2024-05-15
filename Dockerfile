# Start with the Python 3.8 Alpine image
FROM python:3.8-alpine

# Install bash
RUN apk add --no-cache bash

# Set the working directory in the Docker container
WORKDIR /calendar_app

# Copy the application's files into the container
COPY . /calendar_app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the application
EXPOSE 8000

# Set environment variables
ENV APP_NAME="CalendarService"

# Add the wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Command to run the wait-for-it script before starting the application
CMD ["/wait-for-it.sh", "calendar_db:5432", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
