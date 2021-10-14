from email import message
from sqlite3 import DatabaseError
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


class FormLogin(FlaskForm):
    correo = StringField('correo',validators=[DataRequired(message='Favor ingresar un Correo')])
    contraseña = PasswordField('contraseña',validators=[DataRequired(message='Favor digitar una contraseña')])
    enviar = SubmitField('Iniciar Sesion')

class FormContacto(FlaskForm):
    nombre = StringField('nombre',validators=[DataRequired(message='Par favor deja tu nombre')])
    correo = StringField('correo',validators=[DataRequired(message='Favor ingresa un Correo de contacto')])
    textoMensaje = StringField('textoMensaje',validators=[DataRequired(message='Tus comentarios van aquí')])
    enviar = SubmitField('Enviar')