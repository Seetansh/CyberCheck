from app import db

class Scans(db.Model):
    __tablename__ = 'scans'

    scan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    website_url = db.Column(db.String(255), nullable=False)
    scan_date_time = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    result = db.Column(db.Text, nullable=False)
    time_taken = db.Column(db.Float, nullable=False)

    vulnerabilities = db.relationship('Vulnerability', backref=db.backref('scan', lazy='select'), lazy='select')

    def __repr__(self):
        return f'<Scan {self.scan_id} - User {self.user_id} - Website {self.website_url}>'


