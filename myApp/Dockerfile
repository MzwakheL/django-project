# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /myApp

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Install dependencies
RUN pip install django

# Install dependencies
RUN pip install django Pillow

# Set the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# reference - https://www.youtube.com/watch?v=LQjaJINkQXY