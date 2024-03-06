# Nama File: perawat.py
from db import DBConnection as mydb

class perawat:

    def __init__(self):
        self.__id = None
        self.__nip = None
        self.__nama = None
        self.__jk = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk)
        sql = "INSERT INTO freedb_databasenyaaku.perawat (nip, nama, jk) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk, id)
        sql = "UPDATE freedb_databasenyaaku.perawat SET nip = %s, nama = %s, jk = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateBynip(self, nip):
        self.conn = mydb()
        val = (self.__nama, self.__jk, nip)
        sql = "UPDATE freedb_databasenyaaku.perawat SET nama = %s, jk = %s WHERE nip = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM freedb_databasenyaaku.perawat WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteBynip(self, nip):
        self.conn = mydb()
        sql = "DELETE FROM freedb_databasenyaaku.perawat WHERE nip = %s"
        self.affected = self.conn.delete(sql, (nip,))
        self.conn.disconnect()
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM freedb_databasenyaaku.perawat WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        self.__nip = self.result[1]
        self.__nama = self.result[2]
        self.__jk = self.result[3]
        self.conn.disconnect()
        return self.result

    def getBynip(self, nip):
        a = str(nip)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM freedb_databasenyaaku.perawat WHERE nip = %s"
        self.result = self.conn.findOne(sql, (b,))
        if self.result is not None:
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama = ''
            self.__jk = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM freedb_databasenyaaku.perawat"
        self.result = self.conn.findAll(sql)
        return self.result

A = perawat()
nip = '4444'
A.deleteBynip(nip)
B = A.getAllData()
print(B)
