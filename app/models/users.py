from app import db
from app.utils import convert_to_hash


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String(), nullable=True)
    contact_number = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='registered')
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    scans = db.relationship('Scan', backref=db.backref('user', lazy='select'), lazy='select')

    def __init__(self, email, password, name, contact_number):
        self.name = name
        self.email = email
        self.password = convert_to_hash(password)
        self.contact_number = contact_number

        return {name, email, password, contact_number}

    def __repr__(self):
        return f'<User {self.name}>'