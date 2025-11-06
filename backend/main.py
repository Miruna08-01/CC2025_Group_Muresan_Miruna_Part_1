from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "message": "Have a wonderful and productive day! 🌞",
        "current_time": now
    }
