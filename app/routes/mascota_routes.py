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
