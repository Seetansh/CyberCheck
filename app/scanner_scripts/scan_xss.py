from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

XSS_PAYLOADS = ['<script>alert(1)</script>', '"><script>alert(1)</script>']

def scan_xss(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        results = []

        for form in forms:
            action = form.get('action')
            method = form.get('method', 'get').lower()
            inputs = form.find_all('input')
            form_url = urljoin(url, action)

            for payload in XSS_PAYLOADS:
                data = {input.get('name'): payload for input in inputs if input.get('name')}
                if method == 'post':
                    res = requests.post(form_url, data=data, timeout=10)
                else:
                    res = requests.get(form_url, params=data, timeout=10)

                if payload in res.text:
                    results.append({"form": form_url, "payload": payload, "vulnerable": True})
                    break

        return {"status": "success", "vulnerabilities": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
