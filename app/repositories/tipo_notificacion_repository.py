from app import db
from app.models import TipoNotificacion

class TipoNotificacionRepository:

    @staticmethod
    def add_tipo_notificacion(data):
        nuevo_tipo_notificacion = TipoNotificacion(
            tipo=data.get('tipo')
        )
        db.session.add(nuevo_tipo_notificacion)
        db.session.commit()
        return nuevo_tipo_notificacion

    @staticmethod
    def get_tipo_notificacion_by_id(tipo_notificacion_id):
        return TipoNotificacion.query.get(tipo_notificacion_id)

    @staticmethod
    def update_tipo_notificacion(tipo_notificacion_id, data):
        tipo_notificacion = TipoNotificacion.query.get(tipo_notificacion_id)
        if tipo_notificacion:
            tipo_notificacion.tipo = data.get('tipo')
            db.session.commit()
        return tipo_notificacion

    @staticmethod
    def delete_tipo_notificacion(tipo_notificacion_id):
        tipo_notificacion = TipoNotificacion.query.get(tipo_notificacion_id)
        if tipo_notificacion:
            db.session.delete(tipo_notificacion)
            db.session.commit()
        return tipo_notificacion
