from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Docs Registry API", docs_url="/swagger")

class Document(BaseModel):
    id: str
    name: str
    type: str

fake_docs_db = [
    {"id": "1", "name": "Protocolo de Seguridad Runner", "type": "pdf"},
    {"id": "2", "name": "Arquitectura Hibrida", "type": "docx"},
]

# --- ENDPOINTS ---

@app.get("/health")
def read_health():
    return {"status": "ok", "project": "Runner Factory"}

@app.get("/docs", response_model=List[Document])
def list_docs():
    return fake_docs_db

@app.get("/docs/{doc_id}",response_model=Document)
def read_doc(doc_id:str):
    for doc in fake_docs_db:
        if doc["id"] == doc_id:
            return doc
    raise HTTPException(status_code = 404, detail="Document not found")
