#!/bin/bash
# intră în directorul backend
cd backend

# instalează dependențele (într-un virtual environment dacă vrei)
pip install -r requirements.txt

# pornește aplicația FastAPI cu gunicorn + uvicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT