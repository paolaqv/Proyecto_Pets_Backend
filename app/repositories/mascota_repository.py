from app import db
from app.models import Mascota

class MascotaRepository:
    @staticmethod
    def add_mascota(data):
        # Crear una nueva instancia de Mascota usando los datos recibidos
        nueva_mascota = Mascota(
            nombre=data.get('nombre'),
            raza=data.get('raza'),
            peso=data.get('peso'),
            sexo=data.get('sexo'),
            descripcion=data.get('descripcion'),
            foto=data.get('foto'),
            Usuario_id_usuario=data.get('Usuario_id_usuario'),
            especie_id_especie=data.get('especie_id_especie')
        )
        
        db.session.add(nueva_mascota)
        db.session.commit()
        return nueva_mascota
