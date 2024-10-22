import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres:seiya26@localhost/pets') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'seiya26'
