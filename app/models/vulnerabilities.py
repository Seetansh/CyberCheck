from app import db

class Vulnerabilities(db.Model):

    __tablename__ = 'vulnerabilities'

    vulnerability_id = db.Column(db.Integer, primary_key=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scans.scan_id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)

    suggestion = db.relationship('Suggestion', backref=db.backref('vulnerability', lazy='select'), uselist=False, lazy='select')

    def __repr__(self):
        return f'<Vulnerability {self.vulnerability_id} - Scan {self.scan_id} - Name {self.name}>'
