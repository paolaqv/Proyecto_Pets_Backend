from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Permitir CORS para todas las rutas y para el origen del frontend
    CORS(app, origins="http://localhost:5173")

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa los modelos para las migraciones
    from app.models import (Actividad, Mascota, Salud, Usuario, Especie, Notificacion, TipoActividad, TipoSalud)

    # Registra las rutas
    from app.routes import register_routes
    register_routes(app)

    return app
