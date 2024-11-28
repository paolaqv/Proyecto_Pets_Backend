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
    
    
    def obtener_todas1():
        # Obtener las actividades desde el repositorio
        actividades = ActividadRepository.get_todas1()

        # Procesar datos para incluir nombres
        actividades_data = []
        for actividad in actividades:
            actividades_data.append({
                "id_actividad": actividad.id_actividad,
                "fecha_hora": actividad.fecha_hora,
                "descripcion": actividad.descripcion,
                "mascota_nombre": actividad.mascota.nombre,  # Nombre de la mascota
                "tipo_actividad_nombre": actividad.tipo_actividad.tipo  # Nombre del tipo de actividad
            })

        return actividades_data


