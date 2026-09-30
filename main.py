from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Comic Craft AI")
app.include_router(router)
if os.path.exists("static"):
    try:
        app.mount("/static", StaticFiles(directory="static"), name="static")
    except:
        pass