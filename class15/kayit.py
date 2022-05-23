import mysql.connector
from datetime import datetime

def ekleOgrenci(list):

    connection = mysql.connector.connect(
        host="127.0.0.1",  
        user="root",
        password="Ak200940.",
        database="okuldb"
    )

    mycursor = connection.cursor()
    sql = "INSERT INTO Ogrenci (ogrencino,ad,soyad,dogumtarihi,cinsiyet) VALUES (%s,%s,%s,%s,%s)"
    values = list

    mycursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{mycursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {mycursor.lastrowid}')
    except mysql.connector.Error as err:
        print("hata: ", err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')
    
list = []
while True:
    ogrencino = int(input("Öğrenci No: "))
    ad = input("Öğrenci Adı: ")
    soyad = input("Öğrenci Soyadı: ")
    dogumtarihi = input("Öğrenci Doğum tarihi (YYYY,AA,GG olarak giriniz): ")
    cinsiyet = input ("Öğrenci Cinsiyeti (K/E): ")

    list.append((ogrencino, ad, soyad, dogumtarihi, cinsiyet))

    result = input("Devam etmek istiyor musunuz? (e/h)")
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor...')
        ekleOgrenci(list)
        break


