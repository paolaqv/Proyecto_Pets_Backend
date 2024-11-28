from app import db

class Notificacion(db.Model):
    __tablename__ = 'notificacion'

    id_notificacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mensaje = db.Column(db.String(50), nullable=False)
    fecha_inicio = db.Column(db.TIMESTAMP, nullable=False)
    fecha_fin = db.Column(db.TIMESTAMP, nullable=True)  # Opcional para "una vez"
    intervalo = db.Column(db.Integer, nullable=True)  # Intervalo para "repetir"
    unidad_intervalo = db.Column(db.String(10), nullable=True)  # "horas" o "días"
    recordatorio_tipo = db.Column(db.String(10), nullable=False)  # "en la hora" o "antes de"
    recordatorio_cantidad = db.Column(db.Integer, nullable=True)  # Cantidad de horas o días
    recordatorio_hora = db.Column(db.Time, nullable=True)  # Hora del recordatorio
    Actividad_id_actividad = db.Column(db.Integer, db.ForeignKey('Actividad.id_actividad'), nullable=False)
    Usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)

    actividad = db.relationship('Actividad', backref='notificaciones')
    usuario = db.relationship('Usuario', backref='notificaciones')
