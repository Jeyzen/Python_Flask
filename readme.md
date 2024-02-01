# Endpoint API Flask
Este proyecto es una API desarrollada en Flask para un sistema de facturación, que permite la autenticación de usuarios, así como la recuperación de información sobre facturas por día retornado por un endpoint en formato json. Este proyecto fue creado por Yulian Planas bajo la necesidad de un sistema de facturación para integraciones de aplicaciones destinadas a las necesidades de una PYME.

## Dependencias Principales

1. **Flask**
2. **Flask-JWT-Extended**
3. **Flask-SQLAlchemy**
4. **python-dotenv**

## Funcionalidades Principales

1. **Autenticación**: La aplicación utiliza JWT para gestionar la autenticación de usuarios.
2. **Conexión a Bases de Datos**: Configuración de múltiples bases de datos según sucursales.
3. **Obtención de Facturas**: Endpoint para obtener facturas según una fecha dada.

## Verificaciones de Seguridad Implementadas

1. **Validación de Credenciales**: Verifica que las credenciales proporcionadas en el inicio de sesión sean correctas.
2. **Token JWT Expirado**: Controla la expiración del token JWT para mantener la seguridad de la sesión.
3. **Control de Acceso a Sucursales**: Asegura que los usuarios solo puedan acceder a las sucursales autorizadas.

## Registro de Conexiones
 
- Se implementó un registro de conexiones en el endpoint `/login`, almacenando intentos de inicio de sesión en el archivo `log.txt` con información de hora y dirección IP.
- Se implementó una librería `sslify` para la redirección automáticamente todas las solicitudes HTTP a HTTPS.



## DISCLAIMER
### English
This project is a guide created by Yulian Planas for application integrations designed to meet the needs of small and medium-sized enterprises (PYME). The use or modification of this project without the express authorization of Yulian Planas is prohibited.

### License Agreement

The use of this project is subject to the following license:

1. **Personal Use:** You may use this project for your own needs and personal learning.

2. **Commercial Use:** If you wish to use this project for commercial purposes, you must obtain prior authorization from Yulian Planas.

3. **Distribution:** You may not distribute this project without the written consent of Yulian Planas.

4. **Liability:** Yulian Planas is not responsible for any damage or consequences arising from the use or misuse of this project.

Any questions or requests for authorization can be directed to [Yulianplanas@gmail.com].

Thank you for respecting the terms of use.# FlaskAPI

### Spanish

### Licencia de Uso

El uso de este proyecto está sujeto a la siguiente licencia:

1. **Uso Personal:** Puedes utilizar este proyecto para tus propias necesidades y aprendizaje personal.

2. **Uso Comercial:** Si deseas utilizar este proyecto con fines comerciales, debes obtener la autorización previa de Yulian Planas.

4. **Distribución:** No puedes distribuir este proyecto sin el consentimiento por escrito de Yulian Planas.

5. **Responsabilidad:** Yulian Planas no se hace responsable de cualquier daño o consecuencia derivada del uso o mal uso de este proyecto.

Cualquier pregunta o solicitud de autorización puede dirigirse a [Yulianplanas@gmail.com].