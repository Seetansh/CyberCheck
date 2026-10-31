from flask import Blueprint, request, jsonify, render_template
from app.utils import is_valid_url
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

scanner_bp = Blueprint("scan", __name__)

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

@scanner_bp.route('/scan', methods = ['POST', 'GET'])
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
