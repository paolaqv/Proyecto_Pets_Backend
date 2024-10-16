from app import db

class Notificacion(db.Model):
    __tablename__ = 'notificacion'
    
    id_notificacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mensaje = db.Column(db.String(50), nullable=False)
    fecha_inicio = db.Column(db.TIMESTAMP, nullable=False)
    fecha_fin = db.Column(db.TIMESTAMP, nullable=False)
    Actividad_id_actividad = db.Column(db.Integer, db.ForeignKey('Actividad.id_actividad'), nullable=False)
    Usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)
    
    actividad = db.relationship('Actividad', backref='notificaciones')
    usuario = db.relationship('Usuario', backref='notificaciones')
