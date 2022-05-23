import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Ak200940.",
    database = "okuldb"
)

mycursor = connection.cursor()

mycursor.execute("Show Databases")

for i in mycursor:
    print(i)