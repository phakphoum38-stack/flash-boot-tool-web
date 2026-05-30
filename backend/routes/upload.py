from fastapi import UploadFile
import shutil
import os

@app.post("/upload")
async def upload_iso(file: UploadFile):

    os.makedirs("uploads", exist_ok=True)

    save_path = f"uploads/{file.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "success": True,
        "file": file.filename
    }
