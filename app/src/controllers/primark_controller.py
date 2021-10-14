from flask import render_template, redirect, url_for, request, abort
from controllers.forms import FormLogin
from static.py.Usuarios import usuarios
from controllers.forms import FormContacto



def index():
    return render_template('index.html')

def login():
    form=FormLogin()   
    return render_template('login.html',form=form)

def signin():
    return render_template('signin.html')

def favoritos():
    return render_template('favoritos.html')

def productos():
    return render_template('productos.html')

def compras():
    return render_template('compras.html')

def contactenos():
    form=FormContacto()   
    return render_template('contactenos.html', form=form)   

def evaluar():
    return render_template('evaluar.html')



def validarUsuario():
    
    form=FormLogin()
    if(form.validate_on_submit):
        correo=form.correo.data
        contraseña=form.contraseña.data
        
        users=None
        error=False
        nombre=None

        for users in usuarios:
            if(users['correo']==correo and users['contraseña']==contraseña):
                nombre=users['primer nombre']
                apellido=users['primer apellido']
                return render_template('index.html',nombre=nombre , apellido=apellido)
    error=True
    return render_template('login.html',error=error, form=form)
        
def contactForm():
    form=FormContacto()
    mess=request.form['textarea']
    return redirect('mailto:acurango@uninorte.edu.co?body='+str(mess))
