# routes/actividad_routes.py
from flask import Blueprint, request, jsonify
from app.services.actividad_service import ActividadService

actividad_routes = Blueprint('actividad_routes', __name__)

@actividad_routes.route('/citas', methods=['POST'])
def registrar_cita_medica():
    data = request.get_json()
    
    nueva_cita = ActividadService.crear_cita_medica(data)
    
    if nueva_cita:
        return jsonify({
            "id_actividad": nueva_cita.id_actividad,
            "fecha_hora": nueva_cita.fecha_hora,
            "descripcion": nueva_cita.descripcion,
            "tipo_actividad_id_cita": nueva_cita.tipo_actividad_id_cita,
            "Mascota_id_mascota": nueva_cita.Mascota_id_mascota
        }), 201
    else:
        return jsonify({"error": "Error al registrar la cita médica"}), 400
    
    
# Ruta para registrar un paseo
@actividad_routes.route('/paseo', methods=['POST'])
def registrar_paseo():
    data = request.get_json()
    nuevo_paseo = ActividadService.crear_paseo(data)

    if nuevo_paseo:
        return jsonify({
            "id_actividad": nuevo_paseo.id_actividad,
            "fecha_hora": nuevo_paseo.fecha_hora,
            "descripcion": nuevo_paseo.descripcion,
            "tipo_actividad_id_cita": nuevo_paseo.tipo_actividad_id_cita,
            "Mascota_id_mascota": nuevo_paseo.Mascota_id_mascota
        }), 201
    else:
        return jsonify({"error": "Error al registrar el paseo"}), 400


# Ruta para registrar una comida
@actividad_routes.route('/comida', methods=['POST'])
def registrar_comida():
    data = request.get_json()
    nueva_comida = ActividadService.crear_comida(data)

    if nueva_comida:
        return jsonify({
            "id_actividad": nueva_comida.id_actividad,
            "fecha_hora": nueva_comida.fecha_hora,
            "descripcion": nueva_comida.descripcion,
            "tipo_actividad_id_cita": nueva_comida.tipo_actividad_id_cita,
            "Mascota_id_mascota": nueva_comida.Mascota_id_mascota
        }), 201
    else:
        return jsonify({"error": "Error al registrar la comida"}), 400


# Ruta para registrar otra actividad
@actividad_routes.route('/otra_actividad', methods=['POST'])
def registrar_otra_actividad():
    data = request.get_json()
    nueva_otra_actividad = ActividadService.crear_otra_actividad(data)

    if nueva_otra_actividad:
        return jsonify({
            "id_actividad": nueva_otra_actividad.id_actividad,
            "fecha_hora": nueva_otra_actividad.fecha_hora,
            "descripcion": nueva_otra_actividad.descripcion,
            "tipo_actividad_id_cita": nueva_otra_actividad.tipo_actividad_id_cita,
            "Mascota_id_mascota": nueva_otra_actividad.Mascota_id_mascota
        }), 201
    else:
        return jsonify({"error": "Error al registrar la otra actividad"}), 400