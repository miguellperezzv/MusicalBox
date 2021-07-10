from db import db, ma
from datetime import datetime

'''
id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())
'''



class Lanzamiento(db.Model):
    k_lanzamiento = db.Column(db.String(10), primary_key=True)
    n_lanzamiento = db.Column(db.String(100), nullable = False )
    f_lanzamiento = db.Column(db.Date)
    i_lanzamiento = db.Column(db.String(200))


class Artista(db.Model):
    k_artista = db.Column(db.String(10), primary_key=True)
    n_artista = db.Column(db.String(50), nullable = False)
    pais_artista = db.Column(db.String(50))

class Lanzamiento_Artista(db.Model):
    k_artista = db.Column(db.String(10), db.ForeignKey("artista.k_artista"), primary_key=True)
    k_lanzamiento = db.Column(db.String(10), db.ForeignKey("lanzamiento.k_lanzamiento") ,primary_key=True)
    #atributos de la relacion
    lanzamiento = db.relationship("Lanzamiento")
    artista = db.relationship("Artista")

class Genero(db.Model):
    k_genero = db.Column(db.String(30), primary_key=True)

class Lanzamiento_Genero(db.Model):
    k_genero = db.Column(db.String(30), db.ForeignKey("genero.k_genero"),primary_key=True)
    k_lanzamiento = db.Column(db.String(10), db.ForeignKey("lanzamiento.k_lanzamiento"), primary_key=True)
    subgenre = db.Column(db.Boolean)
    #atributos de la relacion
    genero = db.relationship("Genero")
    lanzamiento = db.relationship("Lanzamiento")

class Producto(db.Model):
    k_producto = db.Column(db.String(10), primary_key=True)
    k_lanzamiento = db.Column(db.String(10), db.ForeignKey("lanzamiento.k_lanzamiento"))
    k_categoria = db.Column(db.String(30), db.ForeignKey("categoria.k_categoria"))
    n_producto = db.Column(db.String(100))
    p_producto = db.Column(db.Numeric(11,2), nullable = False )
    d_producto = db.Column(db.String(200))
    stock = db.Column(db.Numeric(5,0), nullable=False)
    i_producto = db.Column(db.String(200))
    f_producto = db.Column(db.DateTime, default= datetime.now())
    #atributos de la relacion
    lanzamiento = db.relationship("Lanzamiento")
    categoria = db.relationship("Categoria")


class Item(db.Model):
    k_producto = db.Column(db.String(10), db.ForeignKey("producto.k_producto"), primary_key=True)
    k_factura = db.Column(db.Numeric(10,0),db.ForeignKey("factura.k_factura"), primary_key=True)
    cant_item = db.Column(db.Numeric(3,0), nullable=False)
    p_item = db.Column(db.Numeric(11,2), nullable=False)
    #atributos de la relacion
    producto = db.relationship("Producto")
    factura = db.relationship("Factura")

class Factura(db.Model):
    k_factura = db.Column(db.Numeric(10,0), primary_key=True)
    k_usuario = db.Column(db.String(10), db.ForeignKey("usuario.k_usuario") , primary_key=True)
    f_compra = db.Column(db.DateTime, default=datetime.now())
    total = db.Column(db.Numeric(13,2), nullable=False)
    #atributos de la relacion
    usuario = db.relationship("Usuario")

class Usuario(db.Model):
    k_usuario = db.Column(db.String(10), primary_key=True)
    k_rol = db.Column(db.String(20), db.ForeignKey('rol.k_rol'))
    n_usuario = db.Column(db.String(20), nullable=False)
    ape_usuario = db.Column(db.String(20), nullable=False)
    email_usuario = db.Column(db.String(50), nullable=False)
    pwd_usuario = db.Column(db.String(100), nullable=False)
    dir_usuario = db.Column(db.String(200))
    lugar_usuario =db.Column(db.String(40))
    #atributo de la relacion
    rol = db.relationship("Rol")

class Rol(db.Model):
    k_rol = db.Column(db.String(20), primary_key=True)

class Categoria(db.Model):
    k_categoria = db.Column(db.String(30), primary_key=True)



def create_new_user(k_usuario, k_rol, n_usuario, ape_usuario, email, password):
    print(email)
    print(password)
    user = Usuario(k_usuario=k_usuario, k_rol=k_rol ,n_usuario =n_usuario,ape_usuario=ape_usuario, email_usuario=email, pwd_usuario=password )
    db.session.add(user)

    if db.session.commit():
        return user
    return None 