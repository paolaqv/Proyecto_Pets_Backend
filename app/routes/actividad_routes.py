# routes/actividad_routes.py
from flask import Blueprint, request, jsonify
from app.services.actividad_service import ActividadService
from datetime import datetime
import pytz


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
    


@actividad_routes.route('/lista', methods=['GET'])
def obtener_actividades():
    try:
        # Obtener todas las actividades desde el servicio
        actividades = ActividadService.obtener_todas1()
        
        if not actividades:
            return jsonify({"error": "No se encontraron actividades"}), 404

        # Transformar las actividades para incluir los nombres de mascota y tipo de actividad
        actividades_data = [
            {
                "id_actividad": actividad["id_actividad"],
                "fecha_hora": actividad["fecha_hora"],
                "descripcion": actividad["descripcion"],
                "mascota": actividad["mascota"],  # Accede correctamente
                "tipo_actividad": actividad["tipo_actividad"],  # Accede correctamente
                "estado": actividad["estado"]  # Incluye el estado
            }
            for actividad in actividades
        ]

        return jsonify(actividades_data), 200

    except Exception as e:
        # Registrar el error en consola para depuración
        print(f"Error al obtener actividades: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
    
# Ruta para obtener todas la actividades para el calendario
@actividad_routes.route('/actividades_calendario', methods=['GET'])
def obtener_actividades_calendario():
    try:
        # Configura la zona horaria
        zona_horaria = pytz.timezone('America/La_Paz')
        actividades = ActividadService.obtener_todas1()

        if not actividades:
            return jsonify([]), 200

        eventos_calendario = []
        for actividad in actividades:
            # Convertir fecha_hora a objeto datetime si es necesario
            if isinstance(actividad["fecha_hora"], str):
                fecha_hora = datetime.fromisoformat(actividad["fecha_hora"])
            else:
                fecha_hora = actividad["fecha_hora"]

            fecha_local = fecha_hora.astimezone(zona_horaria)  # Ajusta a zona local

            # Agregar evento al calendario
            eventos_calendario.append({
                "id": actividad["id_actividad"],
                "name": actividad["descripcion"],
                "date": fecha_local.strftime('%Y-%m-%dT%H:%M:%S'),  # En formato ISO sin zona horaria explícita
                "type": "event",
                "description": f"{actividad['tipo_actividad']} - {actividad['mascota']}"
            })

        return jsonify(eventos_calendario), 200

    except Exception as e:
        print(f"Error al obtener actividades para evo-calendar: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

@actividad_routes.route('/cancelar', methods=['POST'])
def cancelar_actividad():
    try:
        data = request.get_json()
        actividad_id = data.get('id')  # Asegúrate de que "id" existe en la solicitud

        # Llama al servicio para cancelar la actividad
        actividad = ActividadService.cancelar_actividad(actividad_id)
        if actividad:
            return jsonify({"message": "Actividad cancelada exitosamente"}), 200
        else:
            return jsonify({"error": "Actividad no encontrada"}), 404
    except Exception as e:
        print(f"Error al cancelar actividad: {e}")  # Imprime el error en consola
        return jsonify({"error": "Error interno del servidor"}), 500



