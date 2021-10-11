from flask import Flask
from flask import render_template
from flask import url_for


app= Flask(__name__)


@app.route('/')

def index():
    return render_template('Index.html')

@app.route('/login')

def login():
    return render_template('Login.html')

@app.route('/signin')

def signin():
    return render_template('Signin.html')

@app.route('/favoritos')

def favoritos():
    return render_template('Favoritos.html')

@app.route('/productos')

def Productos():
    return render_template('Productos.html')

@app.route('/compras')

def compras():
    return render_template('Compras.html')


@app.route('/contactenos')

def contactenos():
    return render_template('Contactenos.html')

@app.route('/evaluar')

def evaluar():
    return render_template('Evaluar.html')



if __name__ == '__main__':
    app.run( port= 5000, debug=True)
    
