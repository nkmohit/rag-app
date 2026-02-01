from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "RAG App Started"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/upload")
async def upload_file(file : UploadFile):
    """
    Accept a file and save it locally.
    STEP 1 of Ingestion pipeline.
    
    :param file: File to be embeded
    :type file: UploadFile
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return {
        "filename" : file.filename,
        "status": "saved"
    }