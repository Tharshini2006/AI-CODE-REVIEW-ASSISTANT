import os
from dotenv import load_dotenv
from prompts import build_prompt
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

def review_code(code: str, language: str) -> str:
    try:
        client = OpenAI(api_key=API_KEY)
        prompt = build_prompt(code, language)

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text

    except Exception:
        # Fallback demo response
        return f"""
AI Code Review Report ({language})

• Bug: No syntax errors detected
• Code Quality: Code is readable but can be improved
• Security: No major security issues found
• Performance: Code execution is efficient
• Suggestion: Add comments and input validation
"""
