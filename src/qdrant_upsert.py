# src\qdrant_upsert.py
from qdrant_client import QdrantClient, models
from src.create_collection import create_collection


client = QdrantClient("http://localhost:6333")


def upsert_function(id: int, payload: str, vector: list):

    if not client.collection_exists(collection_name="my_collection"):
        create_collection()

    result = client.upsert(
        collection_name="my_collection",
        points=[
            models.PointStruct(
                id=id,
                vector=vector,
                payload={"text": payload}
            )
        ],
        wait=True
    )

    return result