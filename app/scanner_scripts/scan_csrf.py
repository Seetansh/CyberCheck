from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def scan_csrf(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        results = []

        for form in forms:
            inputs = form.find_all('input')
            has_csrf = any(input.get('name') == 'csrf_token' for input in inputs)
            if not has_csrf:
                results.append({"form": urljoin(url, form.get('action')), "csrf_protected": False})

        return {"status": "success", "vulnerabilities": results}

    except Exception as e:
        return {"status": "error", "message": str(e)}
