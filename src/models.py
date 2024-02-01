from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class MxFac(db.Model):
    __tablename__ = 'mxfac'
    __bind_key__ = None

    numero = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora_fis = db.Column(db.String)
    turno = db.Column(db.Integer)
    prefijo = db.Column(db.Integer)
    cod_cpb = db.Column(db.String)
    cod_dto = db.Column(db.String)
    imp_dto = db.Column(db.Float)
    neto1 = db.Column(db.Float)
    tasa1 = db.Column(db.Float)
    iva1 = db.Column(db.Float)
    total = db.Column(db.Float)
    total = db.Column(db.Float)
    prefijo = db.Column(db.Integer)
    items = relationship('MxIte', backref='mxfac', lazy=True)
    cobros = relationship('MxCtc', backref='mxfac', lazy=True)

# Definición del modelo para tabla mxart
class MxArt(db.Model):
    __tablename__ = 'mxart'
    __bind_key__ = None

    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

# Definición del modelo para tabla mxfor
class MxFor(db.Model):
    __tablename__ = 'mxfor'
    __bind_key__ = None

    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

# Definición del modelo para la tabla mxite
class MxIte(db.Model):
    __tablename__ = 'mxite'
    __bind_key__ = None

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, db.ForeignKey('mxfac.numero'))
    cod_art = db.Column(db.Integer)
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Float)

# Definición del modelo para la tabla mxctc
class MxCtc(db.Model):
    __tablename__ = 'mxctc'
    __bind_key__ = None

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, db.ForeignKey('mxfac.numero'))
    cod_for = db.Column(db.String)
    importe = db.Column(db.Float)
