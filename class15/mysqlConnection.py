import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  
    user="root",
    password="Ak200940.",
    database="family"
)

mycursor = mydb.cursor()


