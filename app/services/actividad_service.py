from app.repositories.actividad_repository import ActividadRepository

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


