import os
import httpx
from dotenv import load_dotenv

load_dotenv()

CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
CANVAS_API_URL = os.getenv("CANVAS_API_URL")

if not CANVAS_TOKEN or not CANVAS_API_URL:
    raise RuntimeError("Canvas environment variables are not set")

def _headers() -> dict:
    return {
        "Authorization": f"Bearer {CANVAS_TOKEN}"
    }

async def get_canvas(path: str, params: dict | None = None):
    url = f"{CANVAS_API_URL}{path}"

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers=_headers(),
            params=params,
        )

    response.raise_for_status()
    return response.json()