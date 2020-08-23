from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import sys


app = Flask(__name__)

## c:\users\usuario1\anaconda3\lib\site-packages
## instalamos pip install flask_mysqldb
## A la variable mysql le asiganamos la configuración de la base de datos
## CREACIÓN DE BASE DE DATOS: 
## 1. Creamos la base de datos con nombre flaskcontacts y utf8_unicode_ci
## 2. Creamos la primera tabla, nombre contacts
## 3. Creamos la columna de la tabla, indicamos el tipo de variable. 
## Para el id seleccionamos el tipo indice primario y Opción A.I autoincremenetal.
## El usuario por defecto es root y la contrasea es '' 

## Conexión con mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

## Settings. Para solucionar error: The session is unavailable because no secret key was set. 
app.secret_key = 'mysecretkey'

## render_template ejecuta el código que esta en index.html
## Para que funcione hay que crear un acarpeta especificamente con el nombre templates en la misma 
## ubicación del archivo de flask
@app.route('/', methods = ['GET'])
def index():
    ## Obtener los datos de la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    
    ## Enviar dato al backend
    return render_template('index.html', contactos = data)
#fed

@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if (request.method == 'POST'):
        ## Obtención de los datos del Frint
        fullnameReceived = request.form['fullname']
        phoneReceived = request.form['phone']
        emailReceived = request.form['email']

        ## Añadir usuario a la base de datos, tabla contacts con atributos de tabla fullname, phone, email 
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',(fullnameReceived, phoneReceived, emailReceived))
        mysql.connection.commit()

        ## Mostrar mensaje en pantalla en HTML
        flash('Contact added successfully')
        
        ## Redirigir
        print(fullnameReceived, phoneReceived, emailReceived)
        return redirect(url_for('index'))
    #fi
#fed


@app.route('/edit/<int:id>')
def edit_contact(id):
    ## Editar el dato
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s',[id])
    data = cur.fetchall() ## En este caso se obtiene el dato que cumpla la condición de arriba
    print(data)
    return render_template('edit-contact.html', contact = data[0])
#fed


@app.route('/update/<id>',methods=['POST'])
def update_contact(id):
    if (request.method == 'POST'):
        ## Recibir los archivos del form
        fullnameReceived = request.form['fullname']
        phoneReceived = request.form['phone']
        emailReceived = request.form['email']

        ## Editar en la base de datos
        cur = mysql.connection.cursor()
        cur.execute('UPDATE contacts SET fullname = %s, email = %s, phone = %s WHERE id = %s',(fullnameReceived, phoneReceived, emailReceived,id))
        mysql.connection.commit()

        ## Añadir mensaje y redirigir al inicio
        flash('Contact updated succesfully')
        return redirect(url_for('index'))
    #fi
#fed

@app.route('/delete/<string:id>')
def delete_contact(id):
    ## ELiminar de mysql
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {}'.format(id)) 
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))
#fed

if __name__ == "__main__":
    app.run(port = 3000)
#fi