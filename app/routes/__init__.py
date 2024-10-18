from flask import Blueprint
from .mascota_routes import mascota_routes
from .usuario_routes import usuario_bp

# blueprints
def register_routes(app):
    app.register_blueprint(mascota_routes)
    app.register_blueprint(usuario_bp, url_prefix='/usuario') 