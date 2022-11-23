from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import os


app = Flask(__name__)

def favorite_colors() -> List[Dict]:
   
    db = mysql.connector.connect(
                        host = 'db', user = 'root', password = 'root', port = 3306, database = 'test')
    print("Conexion establecida")
    cursor = db.cursor()
    cursor.execute("Select * from test_table")
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    db.close()
    return results
    

@app.route('/')
def hello():
    return json.dumps({'favorite_colors': favorite_colors()})