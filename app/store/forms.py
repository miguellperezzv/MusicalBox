
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SelectField, PasswordField
from wtforms.fields.html5 import DateField
from datetime import date, datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class CreateUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email_usuario = StringField('Email', validators=[DataRequired()])
    pwd_usuario = PasswordField('Contraseña', validators=[DataRequired(message="Ingresa una contraseña.")])

class LoginUsuarioForm(FlaskForm):
    email_usuario =  StringField('Email', validators=[DataRequired()])
    pwd_usuario =  StringField('Contraseña', validators=[DataRequired()])

class newArtistForm(FlaskForm):
    n_artista = StringField('Nombre del Artista', validators=[DataRequired()])

class  newReleaseForm(FlaskForm):
    n_lanzamiento = StringField("Nombre del lanzamiento", validators=[DataRequired()])
    i_lanzamiento = StringField("Imagen del lanzamiento", validators=[DataRequired()])
    k_artista  = StringField("Artista",validators=[DataRequired()], id="artista")
    f_lanzamiento = DateField("Fecha de Lanzamiento", default=date.today)

        

    