from app import db
from app.models import TipoActividad

class TipoActividadRepository:

    @staticmethod
    def add_tipo_actividad(data):
        nuevo_tipo_actividad = TipoActividad(
            tipo=data.get('tipo')
        )
        db.session.add(nuevo_tipo_actividad)
        db.session.commit()
        return nuevo_tipo_actividad

    @staticmethod
    def get_tipo_actividad_by_id(tipo_actividad_id):
        return TipoActividad.query.get(tipo_actividad_id)

    @staticmethod
    def update_tipo_actividad(tipo_actividad_id, data):
        tipo_actividad = TipoActividad.query.get(tipo_actividad_id)
        if tipo_actividad:
            tipo_actividad.tipo = data.get('tipo')
            db.session.commit()
        return tipo_actividad

    @staticmethod
    def delete_tipo_actividad(tipo_actividad_id):
        tipo_actividad = TipoActividad.query.get(tipo_actividad_id)
        if tipo_actividad:
            db.session.delete(tipo_actividad)
            db.session.commit()
        return tipo_actividad
