from app import db
from app.models import Notificacion

class NotificacionRepository:

    @staticmethod
    def add_notificacion(data):
        nueva_notificacion = Notificacion(
            mensaje=data.get('mensaje'),
            fecha_inicio=data.get('fecha_inicio'),
            fecha_fin=data.get('fecha_fin'),
            mascota_id_mascota=data.get('mascota_id_mascota')
        )
        db.session.add(nueva_notificacion)
        db.session.commit()
        return nueva_notificacion

    @staticmethod
    def get_notificacion_by_id(notificacion_id):
        return Notificacion.query.get(notificacion_id)

    @staticmethod
    def update_notificacion(notificacion_id, data):
        notificacion = Notificacion.query.get(notificacion_id)
        if notificacion:
            notificacion.mensaje = data.get('mensaje')
            notificacion.fecha_inicio = data.get('fecha_inicio')
            notificacion.fecha_fin = data.get('fecha_fin')
            notificacion.mascota_id_mascota = data.get('mascota_id_mascota')
            db.session.commit()
        return notificacion

    @staticmethod
    def delete_notificacion(notificacion_id):
        notificacion = Notificacion.query.get(notificacion_id)
        if notificacion:
            db.session.delete(notificacion)
            db.session.commit()
        return notificacion
