from flask import Blueprint, render_template

user_bp = Blueprint("user", __name__)

@user_bp.route('/user_profile')
def user_profile():
    return "hello"

@user_bp.route('/edit_profile')
def edit_profile():
    return "edit_profile"

@user_bp.route('/dashboard')
def dashboard():
    return render_template('user/dashboard.html')

