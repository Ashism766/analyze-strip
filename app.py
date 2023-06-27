from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from app.api import routes

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)