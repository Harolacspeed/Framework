from flask import Flask,render_template,redirect,request,url_for
import mysql.connector
#creamos una instacia de la clase flask
app = Flask(__name__)
#configurar la conexion
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda2024"
)
cursor = db.cursor()
#definir ruta
@app.route('/')
def lista():#item
    cursor= db.cursor()
    cursor.execute('select * FROM personas')
    usuario = cursor.fetchall()

    return render_template('index.html',personas=usuario)

@app.route('/Registrar', methods=['GET','POST'])
def registrar_usuario():
    if request.method == 'POST':
       Nombres = request.form.get('NOMBRE')
       apellidos= request.form.get('APELLIDO')
       correos= request.form.get('CORREO')
       telefonos= request.form.get('TELEFONO')
       direcciones= request.form.get('DIRECION')
       usuarios= request.form.get('USUARIO')
       contrasenas= request.form.get('CONTRASENA')
#insertar datis a la tabla personas 
    
       cursor.execute("INSERT INTO personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,apellidos,correos,direcciones,telefonos,usuarios,contrasenas))
       db.commit()
#redirigir a la misma pagina cuando el metodo es post
       return redirect(url_for('registrar_usuario'))
#si es un metodo 
    return render_template('Registrar.html')
#definir rutas
#para ejecutar la aplicacion 
if __name__== '__main__':
    app.add_url_rule('/',view_func=lista)
    app.run(debug=True,port=5005)
    