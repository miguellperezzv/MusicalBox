#from app.db import db, ma
from db import db, ma
from datetime import datetime



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
    email_usuario = db.Column(db.String(50), unique=True, nullable=False)
    pwd_usuario = db.Column(db.String(100), nullable=False)
    dir_usuario = db.Column(db.String(200))
    lugar_usuario =db.Column(db.String(40))
    #atributo de la relacion
    rol = db.relationship("Rol")

class Rol(db.Model):
    k_rol = db.Column(db.String(20), primary_key=True)

class Categoria(db.Model):
    k_categoria = db.Column(db.String(30), primary_key=True)



#ESQUEMAS schema
class LanzamientoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lanzamiento
        fields = ["k_lanzamiento", "n_lanzamiento", "f_lanzamiento", "i_lanzamiento"]

class ArtistaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artista
        fields = ["k_artista", "n_artista", "pais_artista"]

class Lanzamiento_ArtistaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lanzamiento_Artista
        fields = ["k_artista", "k_lanzamiento"]

class GeneroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genero
        fields = ["k_genero"]

class Lanzamiento_GeneroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lanzamiento_Genero
        fields = ["k_lanzamiento", "k_genero", "subgenre"]

class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        fields = ["k_lanzamiento", "k_categoria", "n_producto", "p_producto", "d_producto", 'stock', 'i_producto', 'f_producto']

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        fields = ["k_factura", "cant_item", "p_item"]

class FacturaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Factura
        fields = ["k_factura", "k_usuario", "f_compra", "total"]

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        fields = ["k_usuario", "k_rol", "n_usuario","ape_usuario", "email_usuario", "pwd_usuario", "dir_usuario", "lugar_usuario"]

class RolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        fields = ["k_rol"]

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        fields = ["k_categoria"]


#mis consultas 
def create_new_user(n_usuario, ape_usuario, email, password):
    print(email)
    print(password)

    k_usuario = "U"+str(len(get_all_users())+1)
    user = Usuario(k_usuario=k_usuario, k_rol='USER' ,n_usuario =n_usuario,ape_usuario=ape_usuario, email_usuario=email, pwd_usuario=password )
    db.session.add(user)

    if db.session.commit():
        return user
    return None 

def create_new_artist(n_artista):
    print(n_artista)
    k_artista = "A"+str(len(get_all_artists())+1)
    artista = Artista(k_artista=k_artista, n_artista=n_artista)
    db.session.add(artista)

    if db.session.commit():
        return artista
    return None 

def get_all_products():
    products_qs = Producto.query.all()
    product_schema = ProductoSchema()
    products=[product_schema.dump(product) for product in products_qs]
    return products

def get_all_users():
    users_qs = Usuario.query.all()
    users_schema = UsuarioSchema()
    users=[users_schema.dump(user) for user in users_qs]
    return users

def get_all_artists():
    artist_qs = Artista.query.all()
    artist_schema = ArtistaSchema()
    artists=[artist_schema.dump(artista) for artista in artist_qs]
    return artists

def get_user_by_email(email):
    usuario_qs = Usuario.query.filter_by(email_usuario = email).first()
    usuario_schema = UsuarioSchema()
    u = usuario_schema.dump(usuario_qs)
    return u