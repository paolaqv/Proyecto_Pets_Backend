from flask import Blueprint, request, jsonify
from app.services.mascota_service import MascotaService

mascota_routes = Blueprint('mascota_routes', __name__)

@mascota_routes.route('/create', methods=['POST'])
def agregar_mascota():
    data = request.get_json()
    print("Datos recibidos:", data)  # Esto imprimirá los datos recibidos en la consola del servidor

    # Llamar al servicio para validar y crear la mascota
    nueva_mascota, error = MascotaService.crear_mascota(data)
    
    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "id": nueva_mascota.id_mascota,
        "nombre": nueva_mascota.nombre,
        "fecha_nacimiento": nueva_mascota.fecha_nacimiento,  # Añadido
        "raza": nueva_mascota.raza,
        "peso": nueva_mascota.peso,
        "sexo": nueva_mascota.sexo,
        "descripcion": nueva_mascota.descripcion,
        "foto": nueva_mascota.foto,
        "Usuario_id_usuario": nueva_mascota.Usuario_id_usuario,
        "especie_id_especie": nueva_mascota.especie_id_especie
    }), 201

# Ruta para obtener las mascotas del usuario logueado
@mascota_routes.route('/mis-mascotas', methods=['GET'])
def obtener_mis_mascotas():
    usuario_id = request.args.get('Usuario_id_usuario')  # Se obtiene desde los query params
    if not usuario_id:
        return jsonify({"error": "Usuario_id_usuario no proporcionado"}), 400

    mascotas = MascotaService.obtener_mascotas_por_usuario(usuario_id)
    
    if not mascotas:
        return jsonify({"error": "No se encontraron mascotas para este usuario"}), 404

    mascotas_data = [
        {
            "id_mascota": mascota.id_mascota,
            "nombre": mascota.nombre,
            "fecha_nacimiento": mascota.fecha_nacimiento,
            "raza": mascota.raza,
            "peso": mascota.peso,
            "sexo": mascota.sexo,
            "descripcion": mascota.descripcion,
            "foto": mascota.foto,
            "Usuario_id_usuario": mascota.Usuario_id_usuario,
            "especie_id_especie": mascota.especie_id_especie
        }
        for mascota in mascotas
    ]
    
    return jsonify(mascotas_data), 200

