from app import db
from app.models import Usuario
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime
from flask import current_app

class UsuarioService:

    @staticmethod
    def login(email, password):
        # Busca al usuario por email
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        # Verifica la contraseña
        if not check_password_hash(usuario.contrasenia, password):
            return {"error": "Contraseña incorrecta"}, 401

        # Generar el token JWT
        token = jwt.encode({
            'usuario_id': usuario.id_usuario,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

        return {"message": "Login exitoso", "token": token}, 200

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

    @staticmethod
    def update_usuario(usuario_id, data):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            usuario.nombre = data.get('nombre')
            usuario.email = data.get('email')
            usuario.telefono = data.get('telefono')
            if data.get('contrasenia'):
                usuario.contrasenia = generate_password_hash(data.get('contrasenia'))
            db.session.commit()
        return usuario

    @staticmethod
    def delete_usuario(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        return usuario
