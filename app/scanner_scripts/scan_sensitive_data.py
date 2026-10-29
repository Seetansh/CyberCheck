import requests


def scan_sensitive_data(url):
    try:
        if not url.startswith("https://"):
            return {"status": "success", "message": "Site is not using HTTPS, data may be exposed"}
        
        response = requests.get(url, timeout=10)
        headers = response.headers
        missing_headers = []

        secure_headers = ["Strict-Transport-Security", "Content-Security-Policy"]
        for header in secure_headers:
            if header not in headers:
                missing_headers.append(header)

        return {
            "status": "success",
            "message": "Site is using HTTPS but missing secure headers",
            "missing_headers": missing_headers,
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
