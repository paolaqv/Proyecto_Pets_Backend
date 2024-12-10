from flask import Blueprint, request, jsonify
from app.services.notificacion_service import NotificacionService
from app.models import Notificacion
from datetime import datetime, timedelta


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
            "estado": nueva_notificacion.estado,
            "Actividad_id_actividad": nueva_notificacion.Actividad_id_actividad,
            "Usuario_id_usuario": nueva_notificacion.Usuario_id_usuario
        }), 201
    except ValueError as ve:
        return jsonify({"error": f"Validación fallida: {str(ve)}"}), 400
    except Exception as e:
        print(f"Error inesperado: {str(e)}")  # Para depuración en la terminal
        return jsonify({"error": "Error inesperado en el servidor."}), 500


@notificacion_routes.route('/enviarNotificaciones', methods=['GET'])
def enviar_notificaciones():
    try:
        NotificacionService.enviar_notificaciones_automaticas()
        return jsonify({"message": "Notificaciones enviadas correctamente."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


from sqlalchemy import and_, or_

@notificacion_routes.route('/notificaciones', methods=['GET'])
def obtener_notificaciones():
    try:
        # Obtener parámetros de fecha desde el query string
        fecha_inicio = request.args.get('fecha_inicio')
        fecha_fin = request.args.get('fecha_fin')

        # Convertir fechas a objetos datetime
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d') if fecha_inicio else None
        fecha_fin_dt = (datetime.strptime(fecha_fin, '%Y-%m-%d') + timedelta(days=1) - timedelta(seconds=1)) if fecha_fin else None

        # Consulta inicial
        query = Notificacion.query

        # Construir el filtro de rango de fechas
        if fecha_inicio_dt or fecha_fin_dt:
            query = query.filter(
                or_(
                    and_(Notificacion.fecha_inicio >= fecha_inicio_dt, Notificacion.fecha_inicio <= fecha_fin_dt) if fecha_inicio_dt and fecha_fin_dt else None,
                    and_(Notificacion.fecha_fin >= fecha_inicio_dt, Notificacion.fecha_fin <= fecha_fin_dt) if fecha_inicio_dt and fecha_fin_dt else None,
                    and_(Notificacion.fecha_inicio <= fecha_inicio_dt, Notificacion.fecha_fin >= fecha_fin_dt) if fecha_inicio_dt and fecha_fin_dt else None,
                    Notificacion.fecha_fin >= fecha_inicio_dt if fecha_inicio_dt and not fecha_fin_dt else None,
                    Notificacion.fecha_inicio <= fecha_fin_dt if fecha_fin_dt and not fecha_inicio_dt else None
                )
            )

        # Ejecutar la consulta
        notificaciones = query.all()

        # Formatear las notificaciones en JSON
        return jsonify([
            {
                "id": n.id_notificacion,
                "mensaje": n.mensaje,
                "fecha_inicio": n.fecha_inicio.isoformat(),
                "fecha_fin": n.fecha_fin.isoformat() if n.fecha_fin else None,
                "intervalo": n.intervalo,
                "unidad_intervalo": n.unidad_intervalo,
                "estado": n.estado,
                "usuario_id": n.Usuario_id_usuario
            }
            for n in notificaciones
        ]), 200
    except Exception as e:
        print(f"Error al filtrar notificaciones: {e}")
        return jsonify({"error": "Error al obtener notificaciones"}), 500