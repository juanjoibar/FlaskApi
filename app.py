from flask import Flask
from flask import render_template,request, url_for
from pymysql import cursors
from werkzeug.utils import append_slash_redirect, redirect
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistemas1121' 
mysql.init_app(app)


@app.route('/')
def idex():
    return '<h2>Esto es una API</h2> \
    <p><a href="/empleados">/empleados</a></p>'

@app.route('/empleados')
def empleados():
    #no se porque el delete
    sql = 'select * from `sistemas1121`.`empleados` ;'
    conn = mysql.connect()

    cursor = conn.cursor()
    
    cursor.execute(sql)
    empleados = cursor.fetchall()

    conn.commit()


@app.route('/empleado')
def empleado():
    #no se porque el delete
    sql = 'select * from `sistemas1121`.`empleados` ;'
    conn = mysql.connect()

    cursor = conn.cursor()
    
    cursor.execute(sql)
    empleados = cursor.fetchall()

    conn.commit()




if __name__ == '__main__':
    app.run(debug=True)