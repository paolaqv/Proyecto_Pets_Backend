from app import db
from app.models import Usuario
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from flask import current_app

class UsuarioService:

    @staticmethod
    def login(email, contrasenia): 
        print(f"Email recibido: {email}")
        print(f"Contraseña recibida: {contrasenia}")
        # Busca al usuario por email
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        # Verifica la contraseña
        print(f"Hash en la base de datos: {usuario.contrasenia}")
        print(f"Contraseña ingresada: {contrasenia}")
        if not check_password_hash(usuario.contrasenia, contrasenia):  
            return {"error": "Contraseña incorrecta"}, 401

        # Generar el token JWT
        token = jwt.encode({
            'usuario_id': usuario.id_usuario,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

        # Devuelve el token y el nombre del usuario
        return {
            "message": "Login exitoso", 
            "id_usuario": usuario.id_usuario,
            "token": token, 
            "nombre": usuario.nombre  # Devuelve el nombre del usuario
        }, 200
    @staticmethod
    def create_usuario(data):
        # Hash de la contraseña antes de almacenarla
        hashed_password = generate_password_hash(data.get('contrasenia'))

        nuevo_usuario = Usuario(
            nombre=data.get('nombre'),
            email=data.get('email'),
            telefono=data.get('telefono'),
            contrasenia=hashed_password
        )
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return nuevo_usuario

    @staticmethod
    def get_usuario_by_id(usuario_id):
        return Usuario.query.get(usuario_id)

    #Para actualizar usuario sin correo 
    @staticmethod
    def update_usuario(usuario_id, data):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            usuario.nombre = data.get('nombre')
            #usuario.email = data.get('email')
            usuario.telefono = data.get('telefono')
            #if data.get('contrasenia'):
             #   usuario.contrasenia = generate_password_hash(data.get('contrasenia'))
            db.session.commit()
        return usuario
    
    

    @staticmethod
    def delete_usuario(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        return usuario
    
    #Para cambiar password
    @staticmethod
    def update_usuario_password(usuario_id, data):
        # Obtener el usuario por su ID
        usuario = Usuario.query.get(usuario_id)

        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        # Obtener la contraseña actual y nueva de la solicitud
        contrasenia_actual = data.get('contrasenia_actual')
        nueva_contrasenia = data.get('nueva_contrasenia')

        # Verificar que se proporcionaron ambas contraseñas
        if not contrasenia_actual or not nueva_contrasenia:
            return {"error": "Faltan contraseñas"}, 400

        # Verificar la contraseña actual con el hash almacenado en la base de datos
        if not check_password_hash(usuario.contrasenia, contrasenia_actual):
            return {"error": "La contraseña actual es incorrecta"}, 401

        # Generar el nuevo hash de la nueva contraseña
        usuario.contrasenia = generate_password_hash(nueva_contrasenia)

        # Guardar los cambios en la base de datos
        db.session.commit()

        return {"message": "Contraseña actualizada exitosamente"}, 200
