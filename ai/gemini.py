import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

_client = None


def _get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Add it to your .env file as "
                "GEMINI_API_KEY=your_key_here"
            )
        _client = genai.Client(api_key=api_key)
    return _client


def ask_gemini(system_prompt, text, model="gemini-2.5-flash"):
    client = _get_client()

    response = client.models.generate_content(
        model=model,
        contents=text,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

    return response.text
