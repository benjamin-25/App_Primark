from email import message
from sqlite3 import DatabaseError
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


class FormLogin(FlaskForm):
    correo = StringField('correo',validators=[DataRequired(message='Favor ingresar un Correo')])
    contraseña = PasswordField('contraseña',validators=[DataRequired(message='Favor digitar una contraseña')])
    enviar = SubmitField('Iniciar Sesion')