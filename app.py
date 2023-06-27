from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
load_dotenv()
import os
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(routes.router)

PORT = os.environ.get('PORT') or 8000



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=int(PORT))