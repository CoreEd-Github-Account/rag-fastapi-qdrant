# src\qdrant_retrival.py
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
import rich


client = QdrantClient(url="http://localhost:6333")


def retrieve_function(query_vector : list):

    results = client.query_points(
        collection_name="my_collection",
        query=query_vector,
        limit=5
    )

    return results.points[0].payload['text']
 

    
