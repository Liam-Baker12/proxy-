from js import fetch
import asyncio

async def fetch_url(url: str):
    try:
        response = await fetch(url)
        text = await response.text()
        return text[:500]  # return first 500 chars
    except Exception as e:
        return f"⚠️ Error fetching {url}: {e}"
