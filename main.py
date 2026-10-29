from flask import Flask, render_template, request, jsonify
from app.scanner_scripts import (
    scan_sql_injection,
    scan_xss,
    scan_csrf,
    scan_security_headers,
    scan_insecure_deserialization,
    scan_sensitive_data,
    scan_broken_authentication,
    scan_known_vulnerabilities,
    scan_insufficient_logging,
)
from app.utils import is_valid_url

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = 'secret_key_123'

VULNERABILITY_SCANNERS = {
    "sql_injection": scan_sql_injection.scan_sql_injection,
    "xss": scan_xss.scan_xss,
    "csrf": scan_csrf.scan_csrf,
    "security_headers": scan_security_headers.scan_security_headers,
    "insecure_deserialization": scan_insecure_deserialization.scan_insecure_deserialization,
    "sensitive_data": scan_sensitive_data.scan_sensitive_data,
    "broken_authentication": scan_broken_authentication.scan_broken_authentication,
    "known_vulnerabilities": scan_known_vulnerabilities.scan_known_vulnerabilities,
    "insufficient_logging": scan_insufficient_logging.scan_insufficient_logging,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/login')
def login():
    return render_template('public/login.html')

@app.route('/register')
def register():
    return render_template('public/register.html')

@app.route('/user_profile')
def user_profile():
    return "hello"

@app.route('/scan', methods = ['POST', 'GET'])
def scan():

    try:
        if request.method == 'POST':
            data = request.json or request.form or {}
            url = data.get('url')
            vulnerability_type = data.get('vulnerability', 'all')

            # validations
            if not url:
                return jsonify({"status": "error", "message": "URL is required."}),400

            if not is_valid_url(url):
                 return jsonify({"status": "error", "message": "URL is not valid."}),400

            if vulnerability_type not in VULNERABILITY_SCANNERS and vulnerability_type != 'all':
                 return jsonify({"status": "error", "message": f"Invalid vulnerability type: {vulnerability_type}."}),400

            # scanning loop
            results = {}
            # multiple scanning
            if vulnerability_type == 'all':
                for vuln, scanner in VULNERABILITY_SCANNERS.items():
                    try:
                        results[vuln] = scanner(url)
                    except Exception as e:
                        results[vuln] = f"Error scanning {vuln}: {str(e)}"
            else:
                # Single scanning
                scanner = VULNERABILITY_SCANNERS[vulnerability_type]
                try:
                    results[vulnerability_type] = scanner(url)
                except Exception as e:
                    results[vulnerability_type] = f"Error scanning {vulnerability_type}: {str(e)}"

                return jsonify({"status": "success", "results": results}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e),}), 400 
       
    return render_template('public/trial_scanpage.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)