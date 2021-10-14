from email import message
from sqlite3 import DatabaseError
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,DateField 
from wtforms.validators import DataRequired


class FormLogin(FlaskForm):
    correo = StringField('correo',validators=[DataRequired(message='Favor ingresar un Correo')])
    contraseña = PasswordField('contraseña',validators=[DataRequired(message='Favor digitar una contraseña')])
    enviar = SubmitField('Iniciar Sesion')


class FormSignin(FlaskForm):
    tipo = SelectField('Tipo Documento',choices=[('null', ''),('CC', 'Cedula de Ciudadania'), ('TI', 'Tarjeta de Identidad')],validators=[DataRequired(message='Favor seleccione una opcion')])
    documento = StringField('Documento',validators=[DataRequired(message='Favor ingresar un Documento')])
    primer_nombre = StringField('Primer Nombre',validators=[DataRequired(message='Favor ingresar Nombre')])
    segundo_nombre = StringField('Segundo Nombre',validators=[DataRequired(message='Favor ingresar Nombre')])
    primer_apellido = StringField('Primer Apellido',validators=[DataRequired(message='Favor ingresar Apellido')])
    segundo_apellido = StringField('Segundo Apellido',validators=[DataRequired(message='Favor ingresar Apellido')])
    fecha_nacimiento= DateField('Fecha de Nacimiento',validators=[DataRequired(message='Favor ingresar la fecha')])
    correo = StringField('correo',validators=[DataRequired(message='Favor ingresar un Correo')])
    contraseña = PasswordField('contraseña',validators=[DataRequired(message='Favor digitar una contraseña')])
    enviar = SubmitField('Registrate')
