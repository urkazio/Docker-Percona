from flask import Flask, render_template
import mysql.connector
from app import app
from flask import jsonify, request

app = Flask(__name__)



def DBselectNumRows():
    db = mysql.connector.connect(
        host = 'db', user = 'root', password = 'root', port = 3306, database = 'test')
    print("Conexion establecida")

    cursor = db.cursor()
    cursor.execute('Select * from test_table')
    num = cursor.fetchall()
    db.close()
    return num

@app.route('/')
def hello():
    return render_template('index.html', numrows=DBselectNumRows())
