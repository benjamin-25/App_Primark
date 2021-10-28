import sqlite3
from sqlite3 import Error


def connection():

    try:
        db = sqlite3.connect('mydatabase.db')
        return db

    except Error:
        print(Error)


def close_db():
    
    con = connection()
    con.close()



def consultaPersona(correo):

    
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
    
    return resul


def crearPersona(tipo,documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,TipoUser,Permiso,correo,pwd):

    con=connection()
    
    sql= 'INSERT into Personas (TipoIdentificacion,NumeroIdentificacion,PrimerNombre,SegundoNombre,PrimerApellido,SegundoApellido,FechaNacimiento,TipoUsuario,Permisos,CorreoElectronico,Contraseña ) values (?,?,?,?,?,?,?,?,?,?,?)'
            
    try:

        CursorObj=con.cursor()
        resultado=CursorObj.execute(sql,[tipo,documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,TipoUser,Permiso,correo,pwd]).rowcount
        con.commit()
        close_db()
        

    except Error as err:
        print(err)

    return resultado