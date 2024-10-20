from flask import Blueprint
from .mascota_routes import mascota_routes
from .usuario_routes import usuario_bp
from .especie_routes import especie_routes
# blueprints
def register_routes(app):
    app.register_blueprint(mascota_routes, url_prefix='/mascota')
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(especie_routes, url_prefix='/especie')  
