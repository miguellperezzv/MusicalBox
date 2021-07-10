from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField
from wtforms import DateField, SelectField
from datetime import date, datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class CreateUsuarioForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email_usuario = StringField('Email', validators=[DataRequired()])
    pwd_usuario = StringField('Contraseña', validators=[DataRequired()])
    