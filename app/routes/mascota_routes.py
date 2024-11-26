from flask import Blueprint, request, jsonify
from app.services.mascota_service import MascotaService

# Definir el blueprint para las rutas relacionadas con mascotas
mascota_routes = Blueprint('mascota_routes', __name__)

# Ruta para agregar una nueva mascota
@mascota_routes.route('/create', methods=['POST'])
def agregar_mascota():
    data = request.get_json()
    print("Datos recibidos:", data)  # Para debug: imprime los datos recibidos en el servidor

    # Llamar al servicio para validar y crear la mascota
    nueva_mascota, error = MascotaService.crear_mascota(data)
    
    if error:
        return jsonify({"error": error}), 400

    # Si se crea la mascota con éxito, devolver la información de la nueva mascota
    return jsonify({
        "id": nueva_mascota.id_mascota,
        "nombre": nueva_mascota.nombre,
        "fecha_nacimiento": nueva_mascota.fecha_nacimiento,  # Asegúrate de tener este campo en tu modelo
        "raza": nueva_mascota.raza,
        "peso": nueva_mascota.peso,
        "sexo": nueva_mascota.sexo,
        "descripcion": nueva_mascota.descripcion,
        "foto": nueva_mascota.foto,  # Aquí deberías manejar la URL de la foto si es necesario
        "Usuario_id_usuario": nueva_mascota.Usuario_id_usuario,
        "especie_id_especie": nueva_mascota.especie_id_especie
    }), 201

# Ruta para obtener las mascotas de un usuario
@mascota_routes.route('/mis-mascotas', methods=['GET', 'OPTIONS'])
def obtener_mis_mascotas():
    if request.method == 'OPTIONS':
        # Responder a la solicitud preflight de CORS
        return jsonify({"message": "OK"}), 200
    
    usuario_id = request.args.get('Usuario_id_usuario')  # Se obtiene desde los query params

    # Validar que el ID del usuario se haya proporcionado
    if not usuario_id:
        return jsonify({"error": "Usuario_id_usuario no proporcionado"}), 400

    # Llamar al servicio para obtener las mascotas del usuario
    mascotas = MascotaService.obtener_mascotas_por_usuario(usuario_id)
    
    if not mascotas:
        return jsonify({"error": "No se encontraron mascotas para este usuario"}), 404

    # Transformar la lista de mascotas en un formato adecuado para JSON
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
    
    # Devolver las mascotas en formato JSON
    return jsonify(mascotas_data), 200

# Ruta para obtener el perfil de una mascota por su ID
@mascota_routes.route('/perfil/<int:mascota_id>', methods=['GET'])
def obtener_perfil_mascota(mascota_id):
    try:
        mascota = MascotaService.obtener_mascota_por_id(mascota_id)
        if not mascota:
            return jsonify({"error": "Mascota no encontrada"}), 404
        
        return jsonify({
            "id_mascota": mascota.id_mascota,
            "nombre": mascota.nombre,
            "fecha_nacimiento": mascota.fecha_nacimiento,
            "raza": mascota.raza,
            "peso": mascota.peso,
            "sexo": mascota.sexo,
            "descripcion": mascota.descripcion,
            "foto": mascota.foto
        }), 200

    except Exception as e:
        print(f"Error al obtener el perfil de la mascota: {str(e)}")
        return jsonify({"error": "Error interno del servidor"}), 500

# Ruta para actualizar la información de una mascota existente
@mascota_routes.route('/update/<int:mascota_id>', methods=['PUT'])
def actualizar_mascota(mascota_id):
    data = request.get_json()
    
    # Llamar al servicio para actualizar la mascota
    mascota_actualizada, error = MascotaService.actualizar_mascota(mascota_id, data)
    
    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Mascota actualizada exitosamente",
        "mascota": {
            "id_mascota": mascota_actualizada.id_mascota,
            "nombre": mascota_actualizada.nombre,
            "fecha_nacimiento": mascota_actualizada.fecha_nacimiento,
            "raza": mascota_actualizada.raza,
            "peso": mascota_actualizada.peso,
            "sexo": mascota_actualizada.sexo,
            "descripcion": mascota_actualizada.descripcion,
            "foto": mascota_actualizada.foto
        }
    }), 200

# Ruta para eliminar una mascota por su ID
@mascota_routes.route('/eliminar/<int:id_mascota>', methods=['DELETE'])
def eliminar_mascota(id_mascota):
    # Llamar al servicio para eliminar la mascota
    exito, error = MascotaService.eliminar_mascota(id_mascota)

    if error:
        return jsonify({"error": error}), 400

    # Confirmar que la mascota fue eliminada
    return jsonify({"message": "Mascota eliminada correctamente"}), 200
