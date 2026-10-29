import re
import requests

def scan_known_vulnerabilities(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        libraries = re.findall(r"([a-zA-Z\-]+)-([\d\.]+)\.js", response.text)
        vulnerabilities = []

        for lib, version in libraries:
            # Match with a known database (for demonstration purposes, this is static)
            if lib == "jquery" and version < "3.5.0":
                vulnerabilities.append({"library": lib, "version": version, "vulnerable": True})
        
        return {"status": "success", "vulnerabilities": vulnerabilities}

    except Exception as e:
        return {"status": "error", "message": str(e)}
