#!/bin/bash
echo "Starting backend app..."

# Navigate to the backend folder in Azure
cd /home/site/wwwroot
echo "Current folder: $(pwd)"

# Install dependencies (optional if Azure already did it)
pip install -r requirements.txt
echo "Dependencies installed"

# Start FastAPI with Gunicorn + Uvicorn worker
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
