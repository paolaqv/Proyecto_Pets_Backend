import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:marceline25@localhost/pets') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'seiya26'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Ruta absoluta de la carpeta de uploads
