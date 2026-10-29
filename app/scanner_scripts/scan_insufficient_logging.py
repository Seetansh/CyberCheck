import requests

def scan_insufficient_logging(url):
    try:
        test_payload = {"username": "test", "password": "incorrect"}
        response = requests.post(url, data=test_payload, timeout=10)
        
        if response.status_code == 200 and "error" not in response.text.lower():
            return {
                "status": "success",
                "message": "Potential lack of error logging detected",
                "vulnerable": True,
            }

        return {"status": "success", "vulnerable": False}

    except Exception as e:
        return {"status": "error", "message": str(e)}
