from flask import Blueprint, request, jsonify
from app.services.usuario_service import UsuarioService

# Definir el blueprint para las rutas de usuario
usuario_bp = Blueprint('usuario', __name__)

# Ruta para crear un nuevo usuario
@usuario_bp.route('/create', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = UsuarioService.create_usuario(data)
    return jsonify({"message": "Usuario creado", "usuario": nuevo_usuario.id_usuario}), 201

# Ruta para el login
@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    contrasenia = data.get('contrasenia')

    if not email or not contrasenia:
        return jsonify({"error": "Faltan las credenciales"}), 400

    response, status = UsuarioService.login(email, contrasenia)
    return jsonify(response), status

# Ruta para obtener un usuario por su ID
@usuario_bp.route('/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = UsuarioService.get_usuario_by_id(usuario_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({
        "id": usuario.id_usuario,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "telefono": usuario.telefono
    })

# Ruta para actualizar un usuario por su ID
@usuario_bp.route('/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    data = request.json
    usuario_actualizado = UsuarioService.update_usuario(usuario_id, data)
    if not usuario_actualizado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario actualizado", "usuario": usuario_actualizado.id_usuario})

# Ruta para eliminar un usuario por su ID
@usuario_bp.route('/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    usuario_eliminado = UsuarioService.delete_usuario(usuario_id)
    if not usuario_eliminado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado", "usuario": usuario_eliminado.id_usuario})


#Cambiar password
@usuario_bp.route('/cambiar', methods=['PUT'])
def cambiar_contrasenia_usuario():
    data = request.get_json()

    # Verificar que se proporcionen email y nueva contraseña
    email = data.get('email')
    nueva_contrasenia = data.get('nueva_contrasenia')

    if not email or not nueva_contrasenia:
        return jsonify({"error": "Faltan datos (email o nueva contraseña)"}), 400

    # Llamar al servicio para actualizar la contraseña
    result, status = UsuarioService.update_usuario_password(email, data)

    return jsonify(result), status




