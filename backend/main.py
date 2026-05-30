from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Flash Boot Tool API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "name": "Flash Boot Tool",
        "status": "running"
    }

@app.get("/usb")
def usb():
    return [
        {
            "name": "USB Drive",
            "size": "32GB"
        }
    ]
