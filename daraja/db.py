import mysql.connector

data = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    passwd = '1618Teddy!',
)

cursor = data.cursor()

cursor.execute("CREATE DATABASE daraja_db")

print("All done!")