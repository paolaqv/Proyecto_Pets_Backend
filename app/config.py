import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:root@localhost/pets') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'marceline25'
