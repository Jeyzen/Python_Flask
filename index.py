# Index.py
from flask import Flask
import logging
from src.routes import configure_routes
from src.models import db
import os
from flask_sslify import SSLify
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv(dotenv_path='src/.creed')
secret_key = os.getenv('JWT_SECRET_KEY')

# Configuración de logging
logging.basicConfig(filename='logs\log.txt', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s')

# Crear la aplicación Flask
app = Flask(__name__)
app.secret_key = secret_key

# Configura SSLify para forzar el uso de HTTPS
sslify = SSLify(app)

# Configuración de la aplicación y rutas
configure_routes(app)

# Inicializar la extensión SQLAlchemy dentro del contexto de la aplicación
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)