FROM python:3.10

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port Flask runs on
EXPOSE 7860

# Command to run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
