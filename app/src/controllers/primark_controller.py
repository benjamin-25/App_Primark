from unittest import result
from flask import render_template, redirect, url_for, request, abort
from controllers.forms import FormLogin, FormSignin
from static.py.Usuarios import usuarios
from static.py.newusuario import newusuarios
from flask import session,redirect
from database.db_primark import connection, close_db
import sqlite3
from sqlite3 import Error



def index():
    if 'user' in session:
        return render_template('index.html',nombre=session['user'])
    else:
        return render_template('index.html')

def login():
    form=FormLogin()   
    return render_template('login.html',form=form)

def signin():
    formSig=FormSignin()
    return render_template('signin.html',form=formSig)

def favoritos():
    if 'user' in session:
        return render_template('favoritos.html',nombre=session['user'])
    else:
        return render_template('favoritos.html')

def productos():
    if 'user' in session:
        return render_template('productos.html',nombre=session['user'])
    else:
        return render_template('productos.html')

def compras():
    if 'user' in session:
        return render_template('compras.html',nombre=session['user'])
    else:
        return render_template('compras.html')

def contactenos():
    if 'user' in session:
        return render_template('contactenos.html',nombre=session['user'])
    else:
        return render_template('contactenos.html')

def evaluar():
    if 'user' in session:
        return render_template('evaluar.html',nombre=session['user'])
    else:
        return render_template('evaluar.html')


def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('index'))

def validarUsuario():
    
    form=FormLogin()
    if(form.validate_on_submit()):
        correo=form.correo.data
        contraseña=form.contraseña.data
        
        users=None
        error=False
        nombre=None
        resul=None
        con=connection()

        sql= 'SELECT * FROM usuarios WHERE Correo ="{0}" AND Contraseña="{1}"'.format(correo,contraseña)
        try:
            CursorObj= con.cursor()
            CursorObj.execute(sql)
            resul = CursorObj.fetchall()
        
        except Error as err:
                print(err)
        
        
        if resul is None:
            
            error2=True
            return render_template('login.html',error=error2, form=form)
        else:
            print(resul['correo'])
            return render_template('index.html',nombre=resul['correo'])
        '''
        for users in usuarios:
            if(users['correo']==correo and users['contraseña']==contraseña):
                nombre=users['primer nombre']
                apellido=users['primer apellido']
                estado=session['user']=nombre
                return render_template('index.html',nombre=estado)
        '''
    error=True
    return render_template('login.html',error=error, form=form)


def registrarUsuario():
    form=FormSignin()
    if(form.validate_on_submit()):
        tipo=form.tipo.data
        documento=form.documento.data
        primer_nombre=form.primer_nombre.data
        segundo_nombre=form.segundo_nombre.data
        primer_apellido=form.primer_apellido.data
        segundo_apellido=form.segundo_apellido.data
        fecha_nacimiento=form.fecha_nacimiento.data
        correo=form.correo.data
        contraseña=form.contraseña.data
        
        registrado=False
        
        newusuarios=dict(tipo=tipo,
                    documento=documento,
                    primer_nombre=primer_nombre,
                    segundo_nombre=segundo_nombre,
                    primer_apellido=primer_apellido,
                    segundo_apellido=segundo_apellido,
                    fecha_nacimiento=fecha_nacimiento,
                    correo=correo,
                    contraseña=contraseña)
        
        if newusuarios.get('documento')==documento:
            registrado=True
            return render_template('signin.html',status=registrado, form=form)
    error=True
    return render_template('signin.html',error=error, form=form)
        