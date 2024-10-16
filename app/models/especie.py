from app import db

class Especie(db.Model):
    __tablename__ = 'especie'
    
    id_especie = db.Column(db.Integer, primary_key=True)
    especie = db.Column(db.String(50), nullable=False)
