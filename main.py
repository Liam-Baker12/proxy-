from pyodide.http import pyfetch

async def proxy_get(url):
    try:
        # Try to fetch the resource
        response = await pyfetch(url)
        text = await response.string()

        # Return only first 1000 chars to avoid crashing browser
        return f"✅ Success ({response.status}):\n" + text[:1000]

    except Exception as e:
        # More detailed error messages
        err_type = type(e).__name__
        err_msg = str(e)

        if "CORS" in err_msg or "cross-origin" in err_msg:
            return f"❌ CORS Error: The site {url} blocked the request."
        elif "404" in err_msg:
            return f"❌ Not Found (404): {url}"
        elif "Failed to fetch" in err_msg:
            return f"❌ Network Error: Could not reach {url}"
        else:
            return f"❌ {err_type}: {err_msg}"
