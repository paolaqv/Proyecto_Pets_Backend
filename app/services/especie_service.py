from app.repositories.especie_repository import EspecieRepository

class EspecieService:
    
    @staticmethod
    def obtener_todas_especies():
        # Obtiene todas las especies desde el repositorio
        return EspecieRepository.get_all_especies()
