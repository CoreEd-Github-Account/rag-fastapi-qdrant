# main.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
import rich
from src.llm import llm_response
from src.qdrant_retrival import retrieve_function
from src.qdrant_upsert import upsert_function
from src.embedding import get_embedding
from src.validator.upsert_validation import UpsertValidation
from fastapi.middleware.cors import CORSMiddleware
# --------------------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Local development only
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------

@app.get("/")
async def hello():
    return {"message": "Hello from fastapi-rag!"}
# --------------------------------------

@app.post("/upsert")
async def api_upsert(upsert_data: UpsertValidation):

    embedded_vector = get_embedding(upsert_data.payload)

    result = upsert_function(upsert_data.id, upsert_data.payload, embedded_vector)
    
    rich.print("🚀 ~ api_upsert ~ result:", result)
    
    return {"message": "Upsert successful"}

# --------------------------------------

@app.post("/retrieve")
async def api_retrieve(query: str):

    query_vector = get_embedding(query)
    
    vc_db_result = retrieve_function(query_vector) # check

    llm_jawab = llm_response(query, vc_db_result)

    return {"llm_jawab": f"{llm_jawab}"}