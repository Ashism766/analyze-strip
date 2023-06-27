import cv2
import json
from fastapi import FastAPI, UploadFile, File
import os
import uvicorn
from fastapi.staticfiles import StaticFiles

from app.routes import upload_photo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(upload_photo.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)