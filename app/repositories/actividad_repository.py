from datetime import datetime
import pytz
from app import db
from sqlalchemy.orm import joinedload
from app.models import Actividad

class ActividadRepository:

    @staticmethod
    def add_actividad(data):
        # Configura la zona horaria
        zona_horaria = pytz.timezone('America/La_Paz')

        # Convierte la fecha y hora proporcionada a la zona horaria deseada
        fecha_hora = data.get('fecha_hora')
        if isinstance(fecha_hora, str):  # Si viene como string, conviértela a datetime
            fecha_hora = datetime.fromisoformat(fecha_hora)
        fecha_hora_local = zona_horaria.localize(fecha_hora)

        nueva_actividad = Actividad(
            fecha_hora=fecha_hora_local,  # Guarda la fecha ajustada
            descripcion=data.get('descripcion'),
            tipo_actividad_id_cita=data.get('tipo_actividad_id_cita'),
            Mascota_id_mascota=data.get('Mascota_id_mascota')
        )
        db.session.add(nueva_actividad)
        db.session.commit()
        return nueva_actividad

    @staticmethod
    def get_actividad_by_id(actividad_id):
        return Actividad.query.get(actividad_id)

    @staticmethod
    def update_actividad(actividad_id, data):
        actividad = Actividad.query.get(actividad_id)
        if actividad:
            actividad.fecha_hora = data.get('fecha_hora')
            actividad.descripcion = data.get('descripcion')
            actividad.tipo_actividad_id_cita = data.get('tipo_actividad_id_cita')
            actividad.mascota_id_mascota = data.get('mascota_id_mascota')
            db.session.commit()
        return actividad

    @staticmethod
    def delete_actividad(actividad_id):
        actividad = Actividad.query.get(actividad_id)
        if actividad:
            db.session.delete(actividad)
            db.session.commit()
        return actividad
    
    @staticmethod
    def get_todas1():
        # Configura la zona horaria
        zona_horaria = pytz.timezone('America/La_Paz')

        # Incluye las relaciones con Mascota y TipoActividad
        actividades = Actividad.query.options(
            joinedload(Actividad.mascota),  # Carga la relación con Mascota
            joinedload(Actividad.tipo_actividad)  # Carga la relación con TipoActividad
        ).all()

        # Ajusta las fechas de cada actividad a la zona horaria deseada
        for actividad in actividades:
            print(f"Fecha antes de ajuste: {actividad.fecha_hora}")
            actividad.fecha_hora = actividad.fecha_hora.astimezone(zona_horaria)

        return actividades

