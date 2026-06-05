import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)
from google import genai
from app.core.config import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say HermesGuardian Gemini integration successful."
)

print(response.text)