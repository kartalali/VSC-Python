import mysql.connector

def insertMember(name, surname, age, description):
    connection = mysql.connector.connect(host="127.0.0.1", user = "root", password="Ak200940.", database="family")
    cursor = connection.cursor()

    sql = "INSERT INTO Memberoffamily(name,surname,age,description) VALUES (%s,%s,%s,%s)" 
    values = (name,surname,age,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertMembers(list):
    connection = mysql.connector.connect(host="127.0.0.1", user = "root", password="Ak200940.", database="family")
    cursor = connection.cursor()

    sql = "INSERT INTO Memberoffamily(name,surname,age,description) VALUES (%s,%s,%s,%s)" 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getMembers():
    connection = mysql.connector.connect(host="127.0.0.1", user = "root", password="Ak200940.", database="family")
    cursor = connection.cursor()

    # cursor.execute('Select * From Memberoffamily')
    cursor.execute('Select name,age From Memberoffamily')

    # result = cursor.fetchall()    
    result = cursor.fetchone()
    
    print(f'name: {result[0]} age: {result[1]}')

    # for member in result:
    #     # print(f'name: {member[1]} age: {member[2]}')
    #     print(f'name: {member[0]} age: {member[1]}')

getMembers()