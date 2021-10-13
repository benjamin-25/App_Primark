from flask import Flask, request
from flask import render_template
from flask import url_for
from flask import jsonify
from static.py.Usuarios import usuarios
from app import apps


app= Flask(__name__)

@app.route('/Home')

def Home():
    return render_template('Home_user.html')



@app.route('/perfil')

def perfil():
    return render_template('perfil.html')





if __name__ == '__main__':
    app.run( port= 5000, debug=True)