from flask import Blueprint
from .mascota_routes import mascota_routes

# blueprints
def register_routes(app):
    app.register_blueprint(mascota_routes)
