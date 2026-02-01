import os
from fastapi import FastAPI, UploadFile, File
from rag.loader import extract_text_from_file
from rag.embeddings import index_text

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
    
    text = extract_text_from_file(file_path)

    return {
        "filename": file.filename,
        "chars": len(text)
    }

@app.post("/index")
async def index_file(file : UploadFile):
    """
    Full indexing pipeline:
    upload → extract → chunk → embed → store
    
    :param file: Description
    :type file: UploadFile
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    text = extract_text_from_file(file_path)

    if not text.split():
        return {"status": "error", "message": "no text extracted" }
    
    index_text(text=text, source= file.filename)

    return {
        "status": "indexed"
    }