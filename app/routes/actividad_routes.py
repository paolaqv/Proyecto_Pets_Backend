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
