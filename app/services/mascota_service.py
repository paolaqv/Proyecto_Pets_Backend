from app.repositories.mascota_repository import MascotaRepository

class MascotaService:
    @staticmethod
    def validar_datos_mascota(data):
        # Lista de campos obligatorios, incluyendo fecha_nacimiento
        campos_obligatorios = ['nombre', 'fecha_nacimiento', 'raza', 'peso', 'sexo', 'descripcion', 'Usuario_id_usuario', 'especie_id_especie']
        # Verificar que todos los campos estén presentes
        for campo in campos_obligatorios:
            if campo not in data or not data[campo]:
                return False, f"El campo {campo} es obligatorio."
        return True, None

    @staticmethod
    def crear_mascota(data):
        # Validar los datos antes de pasarlos al repositorio
        es_valido, error = MascotaService.validar_datos_mascota(data)
        if not es_valido:
            return None, error

        # Crear la mascota si los datos son válidos
        mascota = MascotaRepository.add_mascota(data)
        return mascota, None
    
    @staticmethod
    def obtener_mascotas_por_usuario(usuario_id):
        return MascotaRepository.get_mascotas_by_usuario_id(usuario_id)
    
    @staticmethod
    def obtener_mascota_por_id(mascota_id):
        # Llamar al repositorio para obtener la mascota por ID
        mascota = MascotaRepository.get_mascota_by_id(mascota_id)
        
        if not mascota:
            raise ValueError(f"Mascota con ID {mascota_id} no encontrada")
        
        return mascota

    @staticmethod
    def actualizar_mascota(mascota_id, data):
        mascota = MascotaRepository.get_mascota_by_id(mascota_id)
        
        if not mascota:
            return None, "Mascota no encontrada"
        
        # Actualizar la mascota con los nuevos datos
        mascota_actualizada = MascotaRepository.update_mascota(mascota_id, data)
        return mascota_actualizada, None