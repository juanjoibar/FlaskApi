from flask import Flask
from flask import render_template,request, url_for
from pymysql import cursors
from werkzeug.utils import redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='sistemas1121' 
mysql.init_app(app)


@app.route('/')


@app.route('/empleados')
def empleados()
    #no se porque el delete
    sql = 'select * from `sistemas1121`.`empleados` ;'
    conn = mysql.connect()

    cursor = conn.cursor()
    
    cursor.execute(sql)
    empleados = cursor.fetchall()

    conn.commit()




if __name__ == '__main__':
    app.run(debug=True)