from fastapi import  UploadFile, File,APIRouter, HTTPException, Request
import json
import os
from fastapi.templating import Jinja2Templates
from .utility import analyze_urine_strip

templates = Jinja2Templates(directory="templates")


router = APIRouter()



@router.post("/analyze")
async def analyze_image(request: Request,file: UploadFile = File(...)):
    
    try:
        os.makedirs("./temp", exist_ok=True)

        file_path = f"./temp/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        color_result = analyze_urine_strip(file_path)
        result_json = json.loads(color_result)

        os.remove(file_path)

        return templates.TemplateResponse("result.html", {"request": request, "result": result_json})

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error") from e


@router.get("/{catch_all:path}")
async def home(request:Request,catch_all:str):
    return templates.TemplateResponse("index.html", context={"request":request})