# src\llm.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



def llm_response(query: str, vc_db_result: str):
    
    prompt = f"""
    Use the following context to answer the question accurately.
    Context: {vc_db_result}
    Question: {query}
    """



    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text