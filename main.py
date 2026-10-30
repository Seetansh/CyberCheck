from flask import Flask, flash, render_template, request, jsonify, redirect
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
from app.forms import RegisterForm, LoginForm, ContactForm
from app.utils import is_valid_url, convert_to_hash, check_hash

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("The form is valid, but message delivery is not configured yet.", "info")
    return render_template('public/contact.html', form=form)


# auth routes

users = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email= form.email.data
        password = form.password.data
        user = users.get(email.lower())
        print(check_hash(password, user["email"]))
        # if password == check_hash(password,user["password_hash"]) and email == user["email"]:
        #     flash(f"Welcome Back {user["username"]}", "success")
        #     return "Dashboard"
        # else:
        #     flash("Invalid Email or Password", "danger")
    return render_template('public/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = convert_to_hash(form.password.data)
            confirm_password = form.confirm_password.data

            # db operations
            # ----
            users[email.lower()] = {
                "email": email,
                "username": username,
                "password_hash": password,
            }
            flash(f"User {username} registered successfully!", "success")
            return redirect('/login')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    return render_template('public/register.html', form=form)


# user routes
@app.route('/dashboard')
def dashboard():
    return render_template('user/dashboard.html')

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