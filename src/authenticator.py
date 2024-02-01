# authenticator.py
import os
from flask import request
from dotenv import load_dotenv
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity

load_dotenv(dotenv_path='src/.creed')

def authenticate(username, password):
    # Obtiene las credenciales del archivo .creed
    stored_username = os.getenv('USERNAME')
    stored_password = os.getenv('PASSWORD')

    # Obtiene el valor de 'cod_suc' directamente del cuerpo de la solicitud
    cod_suc = request.json.get('COD_SUC', None)

    # Verifica las credenciales del usuario y la existencia de 'cod_suc'
    if username == stored_username and password == stored_password and cod_suc:
        # Incluye 'cod_suc' en la identidad
        return {'user_id': 1, 'cod_suc': cod_suc}
    return None


def identity_callback(identity):
    # Utiliza identity.get directamente para obtener 'cod_suc'
    cod_suc = identity.get('cod_suc', None)
    
    # Return a dictionary with the user_id and cod_suc
    return {
        'user_id': get_jwt_identity(),
        'cod_suc': cod_suc
    }

# identity_callback ahora es una función de configuración de JWT
def configure_jwt(app):
    jwt = JWTManager(app)
    jwt.identity_callback = identity_callback

# Función para obtener el identity
def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}

def generate_access_token(identity):
    # Genera un token de acceso estándar
    access_token = create_access_token(identity=identity, expires_delta=timedelta(hours=1), additional_claims={'cod_suc': identity.get('cod_suc')})
    return access_token