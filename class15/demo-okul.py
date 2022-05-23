# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. (connection.py)

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")

""" 
*** Tek bir kayıt ekleme
ahmet = Student("202","ahmet","yılmaz",datetime(2005, 5, 17),"E")
ahmet.saveStudent()
"""

""" 
*** Çoklu kayıt ekleme
ogrenciler = [
    ("301","Servet","Kartal",datetime(2005, 5, 17),"E"),
    ("302","Ali","Kartal",datetime(2005, 6, 17),"E"),
    ("303","Merve","Kartal",datetime(2005, 7, 7),"K"),
    ("304","Melis","Kartal",datetime(2005, 9, 23),"K"),
    ("305","Metin","Kartal",datetime(2004, 7, 27),"E"),
    ("306","Ali","Metin",datetime(2003, 8, 25),"E")
]
Student.saveStudents(ogrenciler)
"""

# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

import mysql.connector
from datetime import datetime
from connection import connection

class Ogrenci:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id,ogrencino,ad,soyad,dogumtarihi,cinsiyet):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.ogrencino = ogrencino
        self.ad = ad
        self.soyad = soyad
        self.dogumtarihi = dogumtarihi
        self.cinsiyet = cinsiyet

    def saveStudent(self):
        sql = "INSERT INTO Ogrenci(OgrenciNo,Ad,Soyad,DogumTarihi,Cinsiyet) VALUES (%s,%s,%s,%s,%s)"
        value = (self.ogrencino,self.ad, self.soyad,self.dogumtarihi,self.cinsiyet)
        Ogrenci.mycursor.execute(sql,value)

        try:
            Ogrenci.connection.commit()
            print(f'{Ogrenci.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Ogrenci.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Ogrenci(OgrenciNo,Ad,Soyad,DogumTarihi,Cinsiyet) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Ogrenci.mycursor.executemany(sql,values)

        try:
            Ogrenci.connection.commit()
            print(f'{Ogrenci.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Ogrenci.connection.close()

    @staticmethod
    def StudentInfo():
        # sql = "select * from ogrenci"
        # sql = "select * from ogrenci LIMIT 3"
        # sql = "select ogrencino,ad,soyad from ogrenci"
        # sql = "select ad,soyad from ogrenci where cinsiyet='K'"
        # sql = "select * from ogrenci where YEAR(dogumtarihi) = 2003"
        # sql = "select * from ogrenci where YEAR(dogumtarihi) = 2005 and ad = 'Ali'"
        # sql = "select * from ogrenci where ad like '%an%' or soyad like '%an%'"
        # sql = "select COUNT(id) from ogrenci where cinsiyet='E'"
        # sql = "select ad,soyad from ogrenci where cinsiyet='K' order by ad,soyad"

        Ogrenci.mycursor.execute(sql)

        try:
            results = Ogrenci.mycursor.fetchall()
            for result in results:
                print(f'{result}')

        except mysql.connector.Error as err:
            print('hata', err)
        finally:
            Ogrenci.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = "select * from ogrenci where id=%s"
        value = (id,)

        Ogrenci.mycursor.execute(sql,value)

        try:
            obj = Ogrenci.mycursor.fetchone()
            return Ogrenci(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Error', err)        
    
    def updateStudent(self):
        sql = "update ogrenci set ogrencino=%s,ad=%s,soyad=%s,dogumtarihi=%s,cinsiyet=%s where id=%s"
        values = (self.ogrencino,self.ad,self.soyad,self.dogumtarihi,self.cinsiyet,self.id)
        Ogrenci.mycursor.execute(sql,values)

        try:
            Ogrenci.connection.commit()
            print(f'{Ogrenci.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    @staticmethod
    def updateStudents(liste):
        sql = "update ogrenci set ogrencino=%s,ad=%s,soyad=%s,dogumtarihi=%s,cinsiyet=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Ogrenci.mycursor.executemany(sql,values)

        try:
            Ogrenci.connection.commit()
            print(f'{Ogrenci.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def getStudentsGender(cinsiyet):
        sql = "select * from ogrenci where cinsiyet=%s"
        value = (cinsiyet,)

        Ogrenci.mycursor.execute(sql,value)

        try:
            return Ogrenci.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)    
        

# student = Student.getStudentById(8)

# student.name = 'Melis Erva'
# student.surname = 'Kartal'

# student.updateStudent()


students = Ogrenci.getStudentsGender('E')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    liste.append(std)

Ogrenci.updateStudents(liste)