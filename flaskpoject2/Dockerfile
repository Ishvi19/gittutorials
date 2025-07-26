FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the Flask app
CMD ["python", "app.py"]