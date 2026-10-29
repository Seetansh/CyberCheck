import requests


def scan_insecure_deserialization(url):
    try:
        payloads = ['O:8:"Exploit":0:{}', 'a:1:{i:0;O:8:"Exploit":0:{}}']
        results = []

        for payload in payloads:
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {"serialized_data": payload}
            response = requests.post(url, headers=headers, data=data, timeout=10)
            if response.status_code == 500:  # Server error can indicate vulnerability
                results.append({"payload": payload, "vulnerable": True})
        
        return {"status": "success", "vulnerabilities": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
