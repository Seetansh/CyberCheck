from flask import Blueprint, render_template, flash, redirect, jsonify
from app import check_hash, convert_to_hash
from app import LoginForm, RegisterForm


auth_bp = Blueprint("auth", __name__)

users = {}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email= form.email.data
        password = form.password.data
        user = users.get(email.lower(), None)
        if user is None:
            flash("No account found! Register first", "danger")
            return redirect("/auth/register")
        if check_hash(password,user["password_hash"]) and email.lower() == user["email"]:
            flash(f"Welcome Back {user["username"]}", "success")
            return "Dashboard"
        else:
            flash("Invalid Email or Password", "danger")
    return render_template('public/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = convert_to_hash(form.password.data)
            # confirm_password = form.confirm_password.data

            # db operations
            # ----
            users[email.lower()] = {
                "email": email,
                "username": username,
                "password_hash": password,
            }
            flash(f"User {username} registered successfully!", "success")
            return redirect('/auth/login')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    return render_template('public/register.html', form=form)
