import os
import httpx

def _get_config():
    token = os.getenv("CANVAS_TOKEN")
    base_url = os.getenv("CANVAS_API_URL")

    if not token or not base_url:
        raise RuntimeError("Canvas environment variables are not set")

    return token, base_url.rstrip("/")

def _headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}"
    }

async def get_canvas(path: str, params: dict | None = None):
    token, base_url = _get_config()
    url = f"{base_url}{path}"

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(
            url,
            headers=_headers(token),
            params=params,
        )

    response.raise_for_status()
    return response.json()