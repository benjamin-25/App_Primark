from contextlib import nullcontext
from flask import render_template, redirect, url_for, request, flash
from controllers.forms import FormLogin, FormSignin
from static.py.Usuarios import usuarios
from static.py.newusuario import newusuarios
from flask import session,redirect
from mydatabase import connection, close_db
from werkzeug.security import check_password_hash, generate_password_hash
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
        if 'submit-button' in session:
            return render_template('compras.html')

def individual():
    if request.method=='POST':
        submit= request.form['submit-button']
        session['submit-button']=submit
        return redirect(url_for('compras'))
    return render_template('individual.html')


def contactenos():
    if 'user' in session:
        return render_template('contactenos.html',nombre=session['user'])
    else:
        return render_template('contactenos.html')

# hola
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

        sql= 'SELECT * FROM Personas WHERE CorreoElectronico ="{0}"'.format(correo)
        try:
            CursorObj= con.cursor()
            CursorObj.execute(sql)
            resul = CursorObj.fetchall()
            con.commit()
            close_db()

        except Error as err:
                print(err)
        
        if len(resul) == 0:
            error2=True
            return render_template('login.html',error=error2, form=form)
        
        else:
            
            pwd = resul[0][10]
            if check_password_hash(pwd,contraseña):

                estado=session['user']=resul[0][2]
                return render_template('index.html',nombre=estado)

            else:
                flash('Error, Usuario o clave invalidas','error')
                return render_template('login.html',form=form)
    
    
    error=True
    return render_template('login.html',error=error, form=form)


def registrarUsuario():

    formSig=FormSignin()

    if(formSig.validate_on_submit()):
        tipo=formSig.tipo.data
        documento=formSig.documento.data
        primer_nombre=formSig.primer_nombre.data
        segundo_nombre=formSig.segundo_nombre.data
        primer_apellido=formSig.primer_apellido.data
        segundo_apellido=formSig.segundo_apellido.data
        fecha_nacimiento=formSig.fecha_nacimiento.data
        correo=formSig.correo.data
        contraseña=formSig.contraseña.data
        
        registrado=False
        TipoUser='Null'
        Permiso='Null'
        
        pwd = generate_password_hash(contraseña)
        con=connection()

        sql1= 'SELECT * FROM Personas WHERE CorreoElectronico ="{0}"'.format(correo)
        try:
            CursorObj= con.cursor()
            CursorObj.execute(sql1)
            resul = CursorObj.fetchall()
            con.commit()
            close_db()

        except Error as err:
                print(err)

        if resul!=0:
            error2=True
            return render_template('signin.html',error=error2, form=formSig)
        
        else:
            sql= 'INSERT into Personas (TipoIdentificacion,NumeroIdentificacion,PrimerNombre,SegundoNombre,PrimerApellido,SegundoApellido,FechaNacimiento,TipoUsuario,Permisos,CorreoElectronico,Contraseña ) values (?,?,?,?,?,?,?,?,?,?,?)'
            

            try:

                CursorObj=con.cursor()
                resultado=CursorObj.execute(sql,[tipo,documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,TipoUser,Permiso,correo,pwd]).rowcount
                con.commit()
                close_db()
                print(resultado)
            except Error as err:
                print(err)
                

            if resultado!=0:
                flash('Estupendo, Registrado Exitosamente!!')
                return redirect(url_for('signin'))

            else:

                error=True
                return render_template('signin.html',error=error, form=formSig)

    error=True
    return render_template('signin.html',error=error, form=formSig)

def productosfemeninos():
    con=connection()
    try:
        cursor=con.cursor()
        query="SELECT NombreProducto FROM Productos WHERE Categoria='F' "
        LPF=cursor.execute(query).fetchall()
    except Error as err:
        print(err)

    try:
        cursor=con.cursor()
        query="SELECT Precio FROM Productos WHERE Categoria='F' "
        LPrF=cursor.execute(query).fetchall()
    except Error as err:
        print(err)
    return render_template('productosfemeninos.html', LPF=LPF, LPrF=LPrF)

