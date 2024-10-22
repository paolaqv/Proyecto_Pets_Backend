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
