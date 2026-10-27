# src\embedding.py
from qdrant_client import QdrantClient, models
import rich

# Initialize client (e.g., local instance)
client = QdrantClient(url="http://localhost:6333")

# Create the collection
def create_collection():
    return client.create_collection(
                collection_name="my_collection",
                vectors_config=models.VectorParams(
                    size=768,  # Size of the embedding vector
                    distance=models.Distance.COSINE # COSINE, DOT, or EUCLID
                )
            )





