import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:admin@localhost/pets') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '159753rpwn'
