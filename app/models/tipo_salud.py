from app import db

class TipoSalud(db.Model):
    __tablename__ = 'tipo_salud'
    
    id_tipoSalud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50), nullable=False)
