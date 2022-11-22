import mysql.connector

db = mysql.connector.connect(
    host = 'percona-db', user = 'root', password = 'root', port = '3306', database = 'test')
print("Conexion establecida")

cursor = db.cursor()
cursor.execute("Select * from test_table")
num = cursor.fetchall()
db.close()
print(num)
