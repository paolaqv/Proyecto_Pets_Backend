from app import db

class Actividad(db.Model):
    __tablename__ = 'Actividad'
    
    id_actividad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_hora = db.Column(db.TIMESTAMP, nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='En proceso')  # Nuevo campo
    tipo_actividad_id_cita = db.Column(db.Integer, db.ForeignKey('tipo_actividad.id_cita'), nullable=False)
    Mascota_id_mascota = db.Column(db.Integer, db.ForeignKey('Mascota.id_mascota'), nullable=False)
    
    # Relaciones con lazy='joined' para cargar automáticamente los datos relacionados
    mascota = db.relationship('Mascota', backref='actividades', lazy='joined')
    tipo_actividad = db.relationship('TipoActividad', backref='actividades', lazy='joined')
