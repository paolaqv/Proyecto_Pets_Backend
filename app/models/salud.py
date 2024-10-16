from app import db

class Salud(db.Model):
    __tablename__ = 'Salud'
    
    id_salud = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.TIMESTAMP, nullable=False)
    observacion = db.Column(db.String(250), nullable=False)
    archivo = db.Column(db.String(100), nullable=False)
    Mascota_id_mascota = db.Column(db.Integer, db.ForeignKey('Mascota.id_mascota'), nullable=False)
    tipo_salud_id_tipoSalud = db.Column(db.Integer, db.ForeignKey('tipo_salud.id_tipoSalud'), nullable=False)
    
    mascota = db.relationship('Mascota', backref='salud')
    tipo_salud = db.relationship('TipoSalud', backref='salud')
