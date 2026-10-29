import requests
import random
import string

def scan_broken_authentication(url):
    try:
        session_payloads = [
            "admin_session_id=12345",
            f"user_session_id={''.join(random.choices(string.ascii_lowercase, k=10))}",
        ]
        results = []

        for payload in session_payloads:
            cookies = {pair.split("=")[0]: pair.split("=")[1] for pair in payload.split(";")}
            response = requests.get(url, cookies=cookies, timeout=10)
            if response.status_code == 200 and "Welcome" in response.text:
                results.append({"cookie": payload, "vulnerable": True})
        
        return {"status": "success", "vulnerabilities": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
