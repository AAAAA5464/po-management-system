# routers/ai.py
from fastapi import APIRouter
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@router.post("/generate-description")
async def generate_description(data: dict):
    product_name     = data.get("product_name", "")
    product_category = data.get("category", "General")

    prompt = f"""Generate a professional 2-sentence marketing description 
    for a product called '{product_name}' in the '{product_category}' category. 
    Keep it concise and appealing."""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }, timeout=30)
            
            result = response.json()
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return {"description": text}

    except Exception as e:
        return {"description": f"A premium quality {product_name} designed for excellence and reliability."}