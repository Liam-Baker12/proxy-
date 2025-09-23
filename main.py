from pyodide.http import pyfetch

async def proxy_get(url):
    try:
        response = await pyfetch(url)
        text = await response.string()
        return text[:1000]  # Only return first 1000 characters
    except Exception as e:
        return f"Error: {e}"
