from typing import Annotated, List
import uuid
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi import Request
from pydantic import BaseModel
import os
from core.paths import UPLOADS_DIR

router = APIRouter(prefix="/chat", tags=["chat"])

def save_image(file: UploadFile) -> str:
    os.makedirs(UPLOADS_DIR, exist_ok=True)

    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{ext}"
    path = os.path.join(UPLOADS_DIR, filename)

    with open(path, "wb") as f:
        f.write(file.file.read())
    return path

class ChatText(BaseModel):
    chat: List[str] | None

@router.post("/")
async def chat(
    text: str | None = Form(None),
    picture: UploadFile | None = File(None)
):
    if text is not None:
        return JSONResponse({
            "data": text,
            "source_type": "TEXT"
        })
    
    if picture is not None:
        path = save_image(picture)
        return JSONResponse({
            "data": path,
            "source_type": "IMAGE"
        })
    