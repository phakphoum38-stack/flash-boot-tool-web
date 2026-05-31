from fastapi import APIRouter
from fastapi import UploadFile
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

@router.post("/upload")

async def upload_iso(
    file: UploadFile
):

    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "success": True,
        "file": file.filename
    }
