import flask import Flask, jsons
from flaskext.mysql import MySQL

@app.route('/')


@app.route('/empleados')
def empleados()
    #no se porque el delete
    sql = 'select * from empleados where is_delete = 0'
    cursor
