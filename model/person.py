# -*- coding: utf-8

"""
Created on '28/02/2017'
@author: Luis Rodriguez
Computer __author__ = 'Desarrollador'
"""

from core.conexion import Conexion
from helpers import helper_validacion as HV
from decimal import *
import psycopg2
from helpers.logger import Log

class mPerson():
    __tableName = 'person'
    __oConexion = None
    __logger = None

    def __init__(self):
        self.__oConexion = Conexion()
        self.__oConexion.connect()
        self.__logger = Log('Modelo Persona')

    def insert(self, arrData):

        """diccionarios"""
        msg = None
        isSuccess = None
        try:
            id = arrData.get('id')
            if(id==0):
                arrData['id'] = (self.__getLastID___() + 1) #id
            sql = 'INSERT INTO '+self.__tableName+' ("id","document", "surname", "name", "birthday", "isCapture") VALUES(%s, %s, %s, %s, %s, %s)'
            data = (arrData['id'], arrData['document'], arrData['surname'], arrData['name'], arrData['birthday'], arrData['isCapture'])
            self.__oConexion.execute(sql, data)
            self.__oConexion.commit()
            isSuccess = True
            msg = 'Registro Guardado!'
        except StandardError, exception:
            msg = str(exception)
            self.__logger.write(msg,self.__logger.ERROR)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess':isSuccess, 'message':msg,'data':None})

    def __getLastID___(self):
        try:
            sql = 'SELECT MAX(id) FROM '+self.__tableName
            cursor = self.__oConexion.execute(sql)
            res = cursor.fetchone()
            if(res[0]==None):
                id = 0
            else:
                id = res[0]
            self.__oConexion.commit()
        except:
            id = 0
            self.__oConexion.rollback()
        return (id)

    def getAllData(self, dni=None):
        msg = None
        isSuccess = None
        data = []
        try:
            if(dni==None):
                sql = "SELECT * FROM " + self.__tableName
            else:
                sql = "SELECT * FROM " + self.__tableName + " WHERE document='"+ str(dni) +"'"
            cursor = self.__oConexion.execute(sql)
            isSuccess = True
            data = []
            k = 0
            for row in cursor:
                data.append(k)
                data[k] = {'id': row[0], 'document': row[1],'surname': row[2], 'name': row[3], 'birthday': row[4], 'isCapture': row[5]}
                k = k + 1
            # get data
            """while (True):
                row = cursor.fetchone()
                if row == None:
                    break
                if(row[5]==1):
                    row = 'Si'
                elif(row[5]==0 or row[5]==None):
                    row = 'No'
                data.append(row)"""
            cursor.close()
            del cursor
        except (Exception, psycopg2.DatabaseError) as ex_c:
            msg = str(ex_c)
            self.__logger.write(msg,self.__logger.ERROR)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess':isSuccess, 'message':msg,'data':data})

    def getRows(self):
        msg = None
        isSuccess = None
        try:
            sql = 'SELECT * FROM '+self.__tableName
            cursor = self.__oConexion.execute(sql)
            list = cursor.fetchall()
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            list = None
            msg = str(exception)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess':isSuccess, 'message':msg,'data':list})

    def getRow(self):
        msg = None
        isSuccess = None
        try:
            sql = 'SELECT * FROM '+self.__tableName+' WHERE "id"=1'
            self.__oConexion.ejecutar(sql)
            data = self.__oConexion.vCursor.fetchone()
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            data = None
            msg = str(exception)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess':isSuccess, 'message':msg,'data':data})

    def execQuery(self):
        res = 1
        msg = None
        isSuccess = None
        try:
            sql = 'SELECT * FROM '+self.__tableName
            self.__oConexion.ejecutar(sql)
            lista = self.__oConexion.vCursor.fetchone();
            res = lista[0]#index 0 (id=1)
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            res = None
            msg = str(exception)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess':isSuccess, 'message':msg,'data':res})

    def close(self):
        self.__oConexion.close()

class ePerson():
    id          = None
    document    = None
    surname     = None
    name        = None
    birthday    = None
    def __init__(self):
        id          = 0
        document    = ''
        surname     = ''
        name        = ''
        birthday    = ''

