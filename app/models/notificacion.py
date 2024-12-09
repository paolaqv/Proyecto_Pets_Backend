from app import db

class Notificacion(db.Model):
    __tablename__ = 'notificacion'

    id_notificacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mensaje = db.Column(db.String(50), nullable=False)
    fecha_inicio = db.Column(db.TIMESTAMP, nullable=False)
    fecha_fin = db.Column(db.TIMESTAMP, nullable=True)  # Opcional para "una vez"
    intervalo = db.Column(db.Integer, nullable=True)  # Intervalo para "repetir"
    unidad_intervalo = db.Column(db.String(10), nullable=True)  # "horas" o "días"
    estado = db.Column(db.String(20), nullable=False, default='Activo')  # Nuevo campo

    Actividad_id_actividad = db.Column(db.Integer, db.ForeignKey('Actividad.id_actividad'), nullable=False)
    Usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)

    actividad = db.relationship('Actividad', backref='notificaciones')
    usuario = db.relationship('Usuario', backref='notificaciones')
