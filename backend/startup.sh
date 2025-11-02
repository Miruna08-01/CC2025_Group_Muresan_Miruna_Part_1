#!/bin/bash

# verifică folderul curent
echo "Current directory: $(pwd)"

# listă fișierele din folderul curent
echo "Files in current directory:"
ls -la

# instalează dependențele
pip install -r backend/requirements.txt

# pornește aplicația FastAPI
gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.main:app --bind 0.0.0.0:$PORT
