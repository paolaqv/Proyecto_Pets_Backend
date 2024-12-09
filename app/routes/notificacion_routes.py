from flask import Blueprint, request, jsonify
from app.services.notificacion_service import NotificacionService

notificacion_routes = Blueprint('notificacion_routes', __name__)

@notificacion_routes.route('/postNotificacion', methods=['POST'])
def registrar_notificacion():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos de notificación no proporcionados"}), 400

    try:
        nueva_notificacion = NotificacionService.crear_notificacion(data)
        return jsonify({
            "id_notificacion": nueva_notificacion.id_notificacion,
            "mensaje": nueva_notificacion.mensaje,
            "fecha_inicio": nueva_notificacion.fecha_inicio.isoformat(),
            "fecha_fin": nueva_notificacion.fecha_fin.isoformat() if nueva_notificacion.fecha_fin else None,
            "intervalo": nueva_notificacion.intervalo,
            "unidad_intervalo": nueva_notificacion.unidad_intervalo,
            "Actividad_id_actividad": nueva_notificacion.Actividad_id_actividad,
            "Usuario_id_usuario": nueva_notificacion.Usuario_id_usuario
        }), 201
    except ValueError as ve:
        return jsonify({"error": f"Validación fallida: {str(ve)}"}), 400
    except Exception as e:
        print(f"Error inesperado: {str(e)}")  # Para depuración en la terminal
        return jsonify({"error": "Error inesperado en el servidor."}), 500
