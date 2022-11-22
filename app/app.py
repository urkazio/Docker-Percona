from flask import Flask
import mysql.connector
import time
import os

app = Flask(__name__)
db = mysql.connector.connect(
        host = 'percona-db', user = 'root', password = 'root', port = 3306, database = 'test')


def get_count():
    retries = 5
    while True:
        try:
            cursor = db.cursor()
            cursor.execute("Select * from test_table")
            num = cursor.fetchall()
            db.close()
            print(num)

            return num
        except db.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_count()
    return 'Eyyyy!!!!!!! Has venido {} veces. Estamos por los helaos no te coles\n'.format(count)