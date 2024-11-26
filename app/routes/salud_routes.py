from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.models import Salud, Mascota, TipoSalud
from app import db
import os

salud_routes = Blueprint('salud_routes', __name__)

# Extensiones permitidas para los archivos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@salud_routes.route('/registrar', methods=['POST'])
def registrar_salud():
    try:
        # Verificar datos recibidos
        print("Datos recibidos (request.form):", request.form)
        print("Archivo recibido:", request.files.get('archivo'))

        # Obtener datos del formulario
        data = request.form

        # Validar los campos requeridos
        required_fields = ['fecha', 'observacion', 'Mascota_id_mascota', 'tipo_salud_id_tipoSalud']
        for field in required_fields:
            if field not in data or not data[field]:
                print(f"Campo faltante o vacío: {field}")
                return jsonify({"error": f"El campo {field} es obligatorio"}), 400

        # Verificar archivo opcional
        file = request.files.get('archivo')
        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config.get('UPLOAD_FOLDER')
            upload_path = os.path.join(upload_folder, filename)
            file.save(upload_path)

        # Crear un nuevo registro de salud
        nuevo_salud = Salud(
            fecha=data['fecha'],
            observacion=data['observacion'],
            archivo=filename if filename else '',
            Mascota_id_mascota=data['Mascota_id_mascota'],
            tipo_salud_id_tipoSalud=data['tipo_salud_id_tipoSalud']
        )
        print("Nuevo registro de salud creado:", nuevo_salud)

        # Guardar en la base de datos
        db.session.add(nuevo_salud)
        print("Registro agregado a la sesión.")
        db.session.commit()
        print("Cambios confirmados en la base de datos.")

        return jsonify({"message": "Registro de salud creado exitosamente"}), 201

    except Exception as e:
        db.session.rollback()
        print("Error interno:", str(e))
        return jsonify({"error": f"Error interno: {str(e)}"}), 500


# Obtener los registros de salud de un usuario
@salud_routes.route('/mis-registros', methods=['GET'])
def obtener_registros_salud():
    usuario_id = request.args.get('Usuario_id_usuario')

    if not usuario_id:
        return jsonify({"error": "El ID del usuario es obligatorio"}), 400

    try:
        registros = db.session.query(Salud).join(Mascota).filter(Mascota.Usuario_id_usuario == usuario_id).all()
        registros_data = [
            {
                "id_salud": registro.id_salud,
                "fecha": registro.fecha.strftime('%Y-%m-%d'),
                "observacion": registro.observacion,
                "archivo": registro.archivo,
                "mascota": registro.mascota.nombre,
                "tipo": registro.tipo_salud.tipo
            }
            for registro in registros
        ]
        return jsonify(registros_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener las categorías de tipo_salud
@salud_routes.route('/categorias', methods=['GET'])
def obtener_categorias_salud():
    try:
        tipos = TipoSalud.query.all()
        tipos_data = [{"id": tipo.id_tipoSalud, "tipo": tipo.tipo} for tipo in tipos]
        print("Categorías cargadas:", tipos_data)  # Depuración
        return jsonify(tipos_data), 200
    except Exception as e:
        print("Error al cargar categorías:", str(e))  # Depuración
        return jsonify({"error": str(e)}), 500



