from app.repositories.actividad_repository import ActividadRepository

class ActividadService:

    @staticmethod
    def crear_cita_medica(data):
        data['tipo_actividad_id_cita'] = 1 
        return ActividadRepository.add_actividad(data)
