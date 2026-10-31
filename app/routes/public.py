from flask import Blueprint, render_template, flash
from app.forms import ContactForm

public_bp = Blueprint("public", __name__)

@public_bp.route('/')
def index():
    return render_template('index.html')

@public_bp.route('/about')
def about():
    return render_template('public/about.html')

@public_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("The form is valid, but message delivery is not configured yet.", "info")
    return render_template('public/contact.html', form=form)


