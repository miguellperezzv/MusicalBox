from app.db import db, ma
from datetime import datetime

'''
id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())
'''


class Lanzamiento(db.Model):
    k_lanzamiento = db.Column(db.Numeric(12,0), primary_key=True)
    n_lanzamiento = db.Column(db.String(100), nullable = False )
    f_lanzamiento = db.Column(db.Date)
    i_lanzamiento = db.Columna(db.String(200))

class Artista(db.Model):
    k_artista = db.Column(db.Numeric(7,0), primary_key=True)
    n_artista = db.Column(db.String(50), nullable = False)
    pais_artista = db.Column(db.String(50))

class Lanzamiento_Artista(db.Model):
    k_artista = db.Column(db.Numeric(7,0), primary_key=True)
    k_lanzamiento = db.Column(db.Numeric(12,0), primary_key=True)

class Genero(db.Model):
    k_genero = db.Column(db.String(30), primary_key=True)

class Lanzamiento_Genero(db.Model):
    k_genero = db.Column(db.String(30), primary_key=True)
    k_lanzamiento = db.Column(db.Numeric(12,0), primary_key=True)
    subgenre = db.Column(db.Boolean)

class Producto(db.Model):
    k_producto = db.Column(db.Numeric(10,0), primary_key=True)
    k_lanzamiento = db.Column(db.Numeric(12,0))
    k_categoria = db.Column(db.String(30))
    n_producto = db.Column(db.String(100))
    p_producto = db.Column(db.Numeric(11,2), nullable = False )
    d_producto = db.Column(db.String(200))
    stock = db.Column(db.Numeric(5,0), nullable=False)
    i_producto = db.Column(db.String(200))
    f_producto = db.Column(db.DateTime, default= datetime.now())



class Item(db.Model):
    k_producto = db.Column(db.Numeric(10,0), primary_key=True)
    k_factura = db.Column(db.Numeric(10,0), primary_key=True)
    cant_item = db.Column(db.Numeric(3,0), nullable=False)
    p_item = db.Column(db.Numeric(11,2), nullable=False)

class Factura(db.Model):
    k_factura = db.Column(db.Numeric(10,0), primary_key=True)
    k_usuario = db.Column(db.Numeric(12,0), primary_key=True)
    f_compra = db.Column(db.DateTime, default=datetime.now())
    total = db.Column(db.Numeric(13,2), nullable=False)

class Usuario(db.Model):
    k_usuario = db.Column(db.Numeric(12,0), primary_key=True)
    k_rol = db.Column(db.String(20), nullable=False)
    n_usuario = db.Column(db.String(20), nullable=False)
    ape_usuario = db.Column(db.String(20), nullable=False)
    email_usario = db.Column(db.String(50), nullable=False)
    pwd_usuario = db.Column(db.String(100), nullable=False)
    dir_usuario = db.Column(db.String(200))
    lugar_usuario =db.Column(db.String(40))

class Rol(db.Model):
    k_rol = db.Column(db.String(20), primary_key=True)

class Categoria(db.Model):
    k_categoria = db.Column(db.String(30), primary_key=True)



