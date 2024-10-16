from app import db

class TipoActividad(db.Model):
    __tablename__ = 'tipo_actividad'
    
    id_cita = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
