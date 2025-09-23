from pyodide.http import pyfetch
import json

async def proxy_get(url):
    try:
        response = await pyfetch(url)
        content_type = response.headers.get("content-type", "")
        text = await response.string()

        # Try to pretty-print JSON if possible
        if "application/json" in content_type:
            try:
                data = json.loads(text)
                return json.dumps(data, indent=2)[:2000]  # Trim if too long
            except Exception:
                return text[:2000]
        else:
            return text[:2000]

    except Exception as e:
        return f"❌ Error: {e}"
