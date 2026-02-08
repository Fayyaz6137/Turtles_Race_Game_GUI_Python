# Use lightweight Python image
FROM python:3.11-slim

# Install system dependencies required for turtle (tkinter)
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the game
CMD ["python", "main.py"]
