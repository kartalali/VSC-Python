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


def insertMember(list):
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



list = []
while True:
    name = input('kişi adı: ')
    surname = input('kişi soyadı: ')
    age = int(input('kişi yaşı: '))
    description = input('kişi açıklaması: ')

    list.append((name, surname, age, description))

    result = input('devam etmek istiyor musunuz? (e/h)')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        print(list)
        insertMember(list)
        break


