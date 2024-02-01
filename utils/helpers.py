from datetime import datetime
from src.models import MxArt, MxFac, MxFor


def obtener_facturas(fecha, db):
    try:
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        facturas = MxFac.query.filter_by(fecha=fecha).all()

        factura_dict = {}

        for factura in facturas:
            numero_factura = numero_factura = f"{factura.prefijo:04d}-{factura.numero:08d}"
            if numero_factura not in factura_dict:
                factura_dict[numero_factura] = {
                    "factura": {
                        "numero": numero_factura,
                        "fecha": factura.fecha.strftime('%d/%m/%Y'),
                        "total": factura.total,
                        "cabecera": {
                            "fecha": str(factura.fecha),
                            "hora": datetime.strptime(factura.hora_fis, '%H%M%S').strftime('%H:%M:%S'),
                            "turno": factura.turno,
                            "prefijo": factura.prefijo,
                            "numero": factura.numero,
                            "cod_cpb": factura.cod_cpb,
                            "cod_dto": factura.cod_dto,
                            "imp_dto": factura.imp_dto,
                            "neto1": factura.neto1,
                            "tasa1": factura.tasa1,
                            "iva1": factura.iva1,
                            "total": factura.total,
                        },
                        "items": [],
                        "cobro": [],
                    }
                }

            factura_info = factura_dict[numero_factura]["factura"]

            # Agregar información de item
            for item in factura.items:
                if item.cod_art != 0:
                    factura_info["items"].append({
                        "nombre_art": get_articulo_nombre(item.cod_art, db),
                        "cantidad": item.cantidad,
                        "cod_art": item.cod_art,
                        "precio": item.precio,
                    })

            # Agregar información de cobro
            for cobro in factura.cobros:
                factura_info["cobro"].append({
                    "nombre_cobro": get_cobro_nombre(cobro.cod_for, db),
                    "cod_for": cobro.cod_for,
                    "importe": cobro.importe,
                })

        data = {
            "fechas": {"fecha": fecha.strftime('%Y-%m-%d')},
            "cantidad": len(factura_dict),
            "facturas": list(factura_dict.values())
        }
        return data

    except Exception as e:
        return {
            "resultId": "1200",
            "resultCode": "ERROR",
            "resultDescription": f"Error: {e}",
            "content": None
        }

# # Función para obtener el nombre del artículo
def get_articulo_nombre(cod_art, db):
    nombre = db.session.query(MxArt.nombre).filter_by(codigo=cod_art).scalar()
    return nombre if nombre else None

# # Función para obtener el nombre del artículo
def get_cobro_nombre(cod_for, db):
    nombre = db.session.query(MxFor.nombre).filter_by(codigo=cod_for).scalar()
    return nombre if nombre else None