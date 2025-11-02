#!/bin/bash
# Navigate to backend folder (optional if already there)
cd /home/site/wwwroot/backend

# Install dependencies (optional if already installed by Azure)
pip install -r requirements.txt

# Start FastAPI using Gunicorn + Uvicorn worker
# main:app -> main.py file with FastAPI instance named app
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
