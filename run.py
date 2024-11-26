import os
from app import create_app

app = create_app()

# Configurar la carpeta de subida
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == "__main__":
    app.run(debug=True)
