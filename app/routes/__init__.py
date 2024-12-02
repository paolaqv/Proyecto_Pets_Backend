from flask import Blueprint
from .mascota_routes import mascota_routes
from .usuario_routes import usuario_bp
from .especie_routes import especie_routes
from .actividad_routes import actividad_routes
from .salud_routes import salud_routes
from .notificacion_routes import notificacion_routes
# blueprints
def register_routes(app):
    app.register_blueprint(mascota_routes, url_prefix='/mascota')
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(especie_routes, url_prefix='/especie')  
    app.register_blueprint(actividad_routes, url_prefix='/actividad')
    app.register_blueprint(salud_routes, url_prefix='/salud')
    app.register_blueprint(notificacion_routes, url_prefix='/notificacion')

