import mysql.connector
from datetime import datetime
from connection import connection
from Ogrenci import Ogrenci
from Ogretmen import Ogretmen
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from ogrenci where id = %s"
        value  = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Ogrenci.OgrenciYarat(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def deleteStudent(self,studentid):
        sql = "delete from ogrenci where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentsByClassId(self,classid):
        sql = "select * from ogrenci where classid = %s"
        value  = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Ogrenci.OgrenciYarat(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addorEditStudent(self,student: Ogrenci):
        pass

    def addStudent(self, student: Ogrenci):        
        sql = "INSERT INTO Ogrenci(OgrenciNo,Ad,Soyad,DogumTarihi,Cinsiyet,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.ogrencino,student.ad, student.soyad,student.dogumtarihi,student.cinsiyet,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def editStudent(self, student: Ogrenci):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.ogrencino,student.ad, student.soyad,student.dogumtarihi,student.cinsiyet,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err) 


    def editTeacher(self, teacher: Ogretmen):
        pass

    def __del__(self):
        self.connection.close()
        print('db silindi')