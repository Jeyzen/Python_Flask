# routes.py
from flask import request, Response
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from src.models import db
from utils.helpers import obtener_facturas
from src.authenticator import authenticate, generate_access_token
import json

def configure_routes(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user@IP:PORT/DATABASE' #change  content for your own values db
    app.config['SQLALCHEMY_BINDS'] = {}
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    SUCURSALES = {
        'cod_suc': {'nombre_base_datos': 'database name', 'ip_base_remota': 'ip address', 'puerto_base_remota': 'port number'},  #same for this
        # Agrega más sucursales según sea necesario
    }
    app.config['SQLALCHEMY_BINDS'] = {}
    for cod_suc, sucursal_info in SUCURSALES.items():
        db_ip = sucursal_info['ip_base_remota']
        db_port = sucursal_info['puerto_base_remota']
        db_name = sucursal_info['nombre_base_datos']
        db_uri = f"mysql+pymysql://user@{db_ip}:{db_port}/{db_name}"
        app.config['SQLALCHEMY_BINDS'][cod_suc] = db_uri

    # Configurar objeto JWT
    jwt = JWTManager(app)
    jwt.identity_callback = generate_access_token

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        if not data or 'USERNAME' not in data or 'PASSWORD' not in data or 'COD_SUC' not in data:
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "ERROR",
                "resultDescription": "Credenciales incorrectas",
                "content": None
            }), status=401, mimetype='application/json')

        username = data['USERNAME']
        password = data['PASSWORD']
        cod_suc = data['COD_SUC']

        if cod_suc in SUCURSALES:
            app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://user@{SUCURSALES[cod_suc]['ip_base_remota']}:{SUCURSALES[cod_suc]['puerto_base_remota']}/{SUCURSALES[cod_suc]['nombre_base_datos']}"
        else:
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "ERROR",
                "resultDescription": "Código de sucursal no autorizado",
                "content": None
            }), status=401, mimetype='application/json')

        # Ajusta la llamada a authenticate para pasar solo dos argumentos
        identity = authenticate(username, password)
        if identity:
            access_token = generate_access_token(identity)
            #print(access_token)
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "SUCCESS",
                "resultDescription": "Inicio de sesión exitoso",
                "content": {"access_token": access_token}
            }), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "ERROR",
                "resultDescription": "Credenciales incorrectas",
                "content": None
            }), status=401, mimetype='application/json')

    @app.route('/facturas/', methods=['GET'])
    @jwt_required()
    def obtener_facturas_endpoint():
        fecha = request.args.get('fecha')

        if not fecha:
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "ERROR",
                "resultDescription": "Parámetro 'fecha' requerido",
                "content": None
            }), status=400, mimetype='application/json')

        # Obtén el código de sucursal directamente desde el token
        current_user = get_jwt_identity()
        cod_suc = current_user.get('cod_suc')

        if cod_suc is None:
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "ERROR",
                "resultDescription": "Código de sucursal no presente en el token",
                "content": None
            }), status=401, mimetype='application/json')

        # Verifica si el código de sucursal está en la lista de sucursales
        if cod_suc not in SUCURSALES:
            return Response(json.dumps({
                "resultId": "1200",
                "resultCode": "ERROR",
                "resultDescription": "Código de sucursal no autorizado",
                "content": None
            }), status=401, mimetype='application/json')

        # Establece la base de datos correspondiente según el código de sucursal
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_BINDS'][cod_suc]

        # Realiza la operación de obtener_facturas utilizando la base de datos configurada
        result = obtener_facturas(fecha, db)

        response = Response(json.dumps({
            "resultId": "1200",
            "resultCode": "SUCCESS",
            "resultDescription": "Operación exitosa",
            "content": result if result else None
        }, sort_keys=False), status=200, mimetype='application/json')

        return response