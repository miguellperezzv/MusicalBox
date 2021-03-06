from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, SelectField, PasswordField, IntegerField, FileField
from wtforms.fields.html5 import DateField
from datetime import date, datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.widgets import html5 as h5widgets
import pycountry
from store.models import get_all_genres

class CreateUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Ingresa un nombre")])
    lastname = StringField('Apellido', validators= [DataRequired(message = "Ingresa un apellido")])
    email_usuario = StringField('Email', validators=[DataRequired(message = "Ingresa un e-mail válido")])
    pwd_usuario = PasswordField('Contraseña', validators=[DataRequired(message="Ingresa una contraseña.")])

class LoginUsuarioForm(FlaskForm):
    email_usuario =  StringField('Email', validators=[DataRequired()])
    pwd_usuario =  PasswordField('Contraseña', validators=[DataRequired()])

class EditUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Ingresa un nombre")])
    lastname = StringField('Apellido', validators= [DataRequired(message = "Ingresa un apellido")])
    email_usuario = StringField('Email', validators=[DataRequired(message = "Ingresa un e-mail válido")])
    pwd_usuario = PasswordField('Contraseña', validators=[DataRequired(message="Ingresa una contraseña.")])
    address = StringField('Dirección', validators=[DataRequired(message="Dirección a donde te enviaremos tus productos")])
    city = StringField('Municipio/Ciudad', id="city", validators=[DataRequired(message="Lugar a donde te enviaremos tus productos")])
    

class GenreSelectField(SelectField):
    def __init__(self, *args, **kwargs):
        super(GenreSelectField, self).__init__(*args, **kwargs)
        #self.choices = [(country.alpha_2, country.name) for country in pycountry.countries]
        genres = get_all_genres()
        genres.append({'k_genero' : 'N/A'})
        print( genres)
        self.choices = [(genre['k_genero']) for genre in genres]
    

class  newReleaseForm(FlaskForm):


    
    #es una mouskerramienta que nos ayudará en la parte de edición del lanzamiento ;)
    #ya que ejemplifico mismo formulario en la vista de edición y quiero evitar conflictos con el otro stringfield
    n_lanzamiento_edit =  StringField("Nombre del lanzamiento [EDICIÓN]", id="lanzamiento", validators=[DataRequired()])
    
    
    n_lanzamiento = StringField("Nombre del lanzamiento", id="lanzamiento", validators=[DataRequired()])
    i_lanzamiento = StringField("Imagen del lanzamiento", validators=[DataRequired()])
    k_artista  = StringField("Artista",validators=[DataRequired()], id="artista")
    f_lanzamiento = DateField("Fecha de Lanzamiento", default=date.today)
    k_genero = GenreSelectField("Genero", id="k_genero")
    

    

class newProductForm(FlaskForm):

    #es una mouskerramienta que nos ayudará en la parte de edición del lanzamiento ;)
    #ya que ejemplifico mismo formulario en la vista de edición y quiero evitar conflictos con el otro stringfield
    n_producto_edit =  StringField("Nombre del lanzamiento [EDICIÓN]", id="lanzamiento", validators=[])
    
    n_lanzamiento = StringField("Lanzamiento asociado", id="lanzamiento", render_kw={"placeholder": "Lanzamiento al que se registra el producto"})
    n_producto = StringField("Nombre del producto", id="producto" , render_kw={"placeholder": "Opcional. Amplía el nombre (ej: +VinylBox Set)"})
    p_producto = IntegerField("Precio", widget=h5widgets.NumberInput(min=0, max=1000000, step=50), validators=[NumberRange(min=0, max=10000), DataRequired()])
    d_producto = StringField("Descripción", render_kw={"placeholder": "Opcional. Información adicional"})
    stock = IntegerField("Stock", widget=h5widgets.NumberInput(min=0, max=1000), validators=[DataRequired()])
    i_producto = FileField("Imagen del producto")
    k_category = SelectField("Categoria", id="category", choices=[])

    def __init__(self, categories_choices: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if categories_choices:
            self.k_category.choices = categories_choices


class CountrySelectField(SelectField):
    def __init__(self, *args, **kwargs):
        super(CountrySelectField, self).__init__(*args, **kwargs)
        #self.choices = [(country.alpha_2, country.name) for country in pycountry.countries]
        self.choices = [(country.name) for country in pycountry.countries]

class newCat_Genre_Artist(FlaskForm):
    genre = StringField("Nuevo Género")
    category = StringField("Nueva Categoría")
    n_artist = StringField('Nombre del Artista', validators=[DataRequired()])
    country = CountrySelectField("Pais de origen" )

class newAdmin(FlaskForm):
    email = StringField("Ingresa el email del nuevo usuario ADMINISTRADOR")
    pwd = PasswordField("Ingresa tu contraseña")

class editReleaseForm(FlaskForm):
    
    n_lanzamiento = StringField("Lanzamiento asociado", id="lanzamiento", render_kw={"placeholder": "Lanzamiento al que se registra el producto"})

