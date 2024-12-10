from app.repositories.actividad_repository import ActividadRepository
from datetime import datetime
import pytz
from app import db


class ActividadService:

    @staticmethod
    def crear_cita_medica(data):
        data['tipo_actividad_id_cita'] = 1 
        return ActividadRepository.add_actividad(data)
    
    def crear_paseo(data):
        data['tipo_actividad_id_cita'] = 2 
        return ActividadRepository.add_actividad(data)
    
    def crear_comida(data):
        data['tipo_actividad_id_cita'] = 3
        return ActividadRepository.add_actividad(data)

    def crear_otra_actividad(data):
        data['tipo_actividad_id_cita'] = 4
        return ActividadRepository.add_actividad(data)
    
    
    @staticmethod
    def obtener_todas1():
        zona_horaria = pytz.timezone('America/La_Paz')
        actividades = ActividadRepository.get_todas1()

        actividades_data = []
        now = datetime.now(zona_horaria)  # Hora actual

        for actividad in actividades:
            # Omitir actividades canceladas
            if actividad.estado == "Cancelado":
                continue

            fecha_hora = actividad.fecha_hora.astimezone(zona_horaria)

            # Procesa los datos
            actividades_data.append({
                "id_actividad": actividad.id_actividad,
                "fecha_hora": fecha_hora.isoformat(),
                "descripcion": actividad.descripcion,
                "mascota": actividad.mascota.nombre if actividad.mascota else "Desconocida",
                "tipo_actividad": actividad.tipo_actividad.tipo if actividad.tipo_actividad else "Sin categoría",
                "estado": actividad.estado  # Incluye el estado
            })

        return actividades_data


    @staticmethod
    def cancelar_actividad(actividad_id):
        actividad = ActividadRepository.get_actividad_by_id(actividad_id)
        if actividad:
            actividad.estado = "Cancelado"  # Cambia el estado a "Cancelado"
            db.session.commit()  # Guarda los cambios en la base de datos
            return actividad
        return None




