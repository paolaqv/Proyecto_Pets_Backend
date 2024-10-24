from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    
    

#base de datos
    from app.models import (Actividad, Mascota, Salud, Usuario, Especie, Notificacion, TipoActividad, TipoSalud)

#rutas
    from app.routes import register_routes
    register_routes(app)

    return app

