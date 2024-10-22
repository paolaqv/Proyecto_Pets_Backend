from app import db
from app.models import Mascota

class MascotaRepository:
    
    @staticmethod
    def add_mascota(data):
        nueva_mascota = Mascota(
            nombre=data.get('nombre'),
            fecha_nacimiento=data.get('fecha_nacimiento'),  # Añadido
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
    
    @staticmethod
    def get_mascota_by_id(mascota_id):
        return Mascota.query.get(mascota_id)
    
    @staticmethod
    def update_mascota(mascota_id, data):
        mascota = Mascota.query.get(mascota_id)
        if mascota:
            mascota.nombre = data.get('nombre')
            mascota.fecha_nacimiento = data.get('fecha_nacimiento')  # Añadido
            mascota.raza = data.get('raza')
            mascota.peso = data.get('peso')
            mascota.sexo = data.get('sexo')
            mascota.descripcion = data.get('descripcion')
            mascota.foto = data.get('foto')
            mascota.Usuario_id_usuario = data.get('Usuario_id_usuario')
            mascota.especie_id_especie = data.get('especie_id_especie')
            db.session.commit()
        return mascota

    @staticmethod
    def delete_mascota(mascota_id):
        mascota = Mascota.query.get(mascota_id)
        if mascota:
            db.session.delete(mascota)
            db.session.commit()
        return mascota
    
    #Obtener mascotas registradas por IDusuario
    @staticmethod
    def get_mascotas_by_usuario_id(usuario_id):
        return Mascota.query.filter_by(Usuario_id_usuario=usuario_id).all()
