from flask import Flask, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

DEFAULT_CATEGORIES = [
    {"id_tipoSalud": 1, "tipo": "Vacunas"},
    {"id_tipoSalud": 2, "tipo": "Exámenes Médicos"},
    {"id_tipoSalud": 3, "tipo": "Tratamientos"},
    {"id_tipoSalud": 4, "tipo": "Cirugías"}
]

def create_app():
    app = Flask(__name__)

    # Configuración de la app
    CORS(app, origins="http://localhost:5173", methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'], allow_headers=["Content-Type", "Authorization"])
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Importar modelos y registrar rutas
    from app.models import (Actividad, Mascota, Salud, Usuario, Especie, Notificacion, TipoActividad, TipoSalud)
    from app.routes import register_routes

    with app.app_context():
        initialize_tipo_salud()

    register_routes(app)
    from app.services.scheduler import iniciar_scheduler
    iniciar_scheduler()

    # Ruta para servir archivos
    @app.route('/uploads/<path:filename>')
    def download_file(filename):
        uploads_dir = os.path.join(os.getcwd(), 'uploads')  # Ruta absoluta
        file_path = os.path.join(uploads_dir, filename)

        # Verifica si el archivo existe
        if not os.path.isfile(file_path):
            return f"Archivo {filename} no encontrado en {uploads_dir}.", 404

        try:
            # Enviar el archivo
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            print(f"Error al enviar el archivo {filename}: {e}")
            return f"Error al intentar descargar el archivo {filename}.", 500

    return app

def initialize_tipo_salud():
    from app.models import TipoSalud
    existing_categories = TipoSalud.query.all()
    existing_types = {category.tipo for category in existing_categories}

    new_categories = [
        TipoSalud(**category)
        for category in DEFAULT_CATEGORIES
        if category["tipo"] not in existing_types
    ]

    if new_categories:
        db.session.add_all(new_categories)
        db.session.commit()
        print(f"Categorías predeterminadas añadidas: {[c.tipo for c in new_categories]}")
    else:
        print("Categorías ya configuradas.")

