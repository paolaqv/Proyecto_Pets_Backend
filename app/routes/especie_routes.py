from flask import Blueprint, jsonify
from app.services.especie_service import EspecieService

especie_routes = Blueprint('especie_routes', __name__)

@especie_routes.route('/get', methods=['GET'])
def obtener_especies():
    especies = EspecieService.obtener_todas_especies()

    # Formatear las especies para enviarlas como respuesta JSON
    especies_data = [
        {
            "id_especie": especie.id_especie,
            "especie": especie.especie
        }
        for especie in especies
    ]
    
    return jsonify(especies_data), 200


