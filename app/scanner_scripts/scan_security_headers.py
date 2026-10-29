import requests


def scan_security_headers(url):
    try:
        response = requests.head(url, timeout=10)
        headers = response.headers
        missing_headers = []

        required_headers = [
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "X-Frame-Options",
        ]

        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)

        return {"status": "success", "missing_headers": missing_headers}

    except Exception as e:
        return {"status": "error", "message": str(e)}
