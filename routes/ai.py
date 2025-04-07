import os
from fastapi import APIRouter
from models import DebugRequest
from openai import OpenAI

router = APIRouter()

# Initialize OpenAI client with environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@router.post("/debug/", summary="Get AI debugging suggestions")
async def debug_code(request: DebugRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a debugging assistant. Analyze the code and suggest fixes for syntax errors, bugs, or performance issues."},
                {"role": "user", "content": f"Analyze this code:\n\n{request.code}"}
            ],
            max_tokens=150,
            temperature=0.5
        )
        suggestion = response.choices[0].message.content.strip()
        return {"suggestion": suggestion}
    except Exception as e:
        return {"suggestion": f"Error analyzing code: {str(e)}"}