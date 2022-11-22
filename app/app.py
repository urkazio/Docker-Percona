from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import datetime

app = Flask(__name__)
db = mysql.connector.connect(host = 'perconadb', user = 'root', password = 'root', port = 3306)

def test_table() -> List[Dict]:

    cnx = mysql.connector.connect(user='root', database='employees')
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name, hire_date FROM employees "
            "WHERE hire_date BETWEEN %s AND %s")

    hire_start = datetime.date(1999, 1, 1)
    hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query, (hire_start, hire_end))

    cursor.close()
    cnx.close()

    return cursor


@app.route('/')
def index() -> str:
    return json.dumps({'test_table': test_table()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')