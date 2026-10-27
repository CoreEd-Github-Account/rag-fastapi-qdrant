# src\validator\upsert_validation.py
from pydantic import BaseModel


class UpsertValidation(BaseModel):
    id : int
    payload : str
