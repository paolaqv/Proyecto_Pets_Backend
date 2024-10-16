from app import db

class Actividad(db.Model):
    __tablename__ = 'Actividad'
    
    id_actividad = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.TIMESTAMP, nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    tipo_actividad_id_cita = db.Column(db.Integer, db.ForeignKey('tipo_actividad.id_cita'), nullable=False)
    Mascota_id_mascota = db.Column(db.Integer, db.ForeignKey('Mascota.id_mascota'), nullable=False)
    
    mascota = db.relationship('Mascota', backref='actividades')
    tipo_actividad = db.relationship('TipoActividad', backref='actividades')
