#!/bin/bash
echo "Starting backend app..."

# Already in /home/site/wwwroot, no need to cd
echo "Current folder: $(pwd)"

# Install dependencies
pip install -r requirements.txt
echo "Dependencies installed"

# Start FastAPI with Gunicorn + Uvicorn worker
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
