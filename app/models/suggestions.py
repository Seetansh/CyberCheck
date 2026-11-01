from app import db

# Suggestion model
class Suggestions(db.Model):
    __tablename__ = 'suggestions'

    suggestion_id = db.Column(db.Integer, primary_key=True)
    vulnerability_id = db.Column(db.Integer, db.ForeignKey('vulnerabilities.vulnerability_id'), nullable=False)
    suggestion_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    def __repr__(self):
        return f'<Suggestion {self.suggestion_id} - Vulnerability {self.vulnerability_id}>'