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
import model.inplanet


class eInplanet(object):
    def __init__(self):
        self._id = 0
        self._ruc = ''
        self._razonSocial = ''
        self._dirMatriz = ''

    @property
    def id(self):
        print "Getting: %i" % self._id
        return self._id

    @id.setter
    def id(self, value):
        print "Setting: %i" % value
        self._id = value

    @id.deleter
    def id(self):
        print ">Deleting: %i" % self._id
        del self._id

    @property
    def ruc(self):
        print "Getting: %s" % self._ruc
        return self._ruc

    @ruc.setter
    def ruc(self, value):
        print "Setting: %s" % value
        self._ruc = value

    @ruc.deleter
    def ruc(self):
        print ">Deleting: %s" % self._ruc
        del self._ruc



class mInplanet():
    __tableName = 'inplanet'
    __oConexion = None
    __logger = None
    eInplanet = eInplanet()

    def __init__(self):
        self.__oConexion = Conexion()
        self.__oConexion.connect()
        self.__logger = Log('Modelo Inplanet')

    def __load__(self, value, by='id', except_value=None, except_by='id'):
        msg = None
        isSuccess = None
        data = None
        try:
            sql = "SELECT * FROM " + self.__tableName + " WHERE " + by + "='" + str(value) + "'"
            if not except_value == None:
                sql = sql + "and " + except_by + " <> " + str(except_value)
            cursor = self.__oConexion.execute(sql)
            row = cursor.fetchone()
            if (not row == None):
                data = {'id': row[0], 'ruc': row[1], 'razonSocial': row[2], 'dirMatriz': row[3]}
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            data = None
            msg = str(exception)
            self.__logger.write(msg, self.__logger.ERROR)
            self.__oConexion.rollback()
            isSuccess = False
        oBus = {'isSuccess': isSuccess, 'message': msg, 'data': data}
        return oBus

    def load(self, value, by='id', except_value=None, except_by='id'):

        data = self.__load__(value, by, except_value, except_by)

        return data

    def insert(self, arrData):
        try:
            id = arrData.get('id')
            if (id == 0):
                arrData['id'] = (self.__getLastID___() + 1)  # id
            sql = 'INSERT INTO ' + self.__tableName + ' ("id", "ruc", "razonSocial", "dirMatriz") VALUES(%s, %s, %s, %s)'
            data = (arrData['id'], arrData['ruc'], arrData['razonSocial'], arrData['dirMatriz'])
            self.__oConexion.execute(sql, data)
            self.__oConexion.commit()
            isSuccess = True
            msg = 'Registro Guardado!'
        except StandardError, exception:
            msg = str(exception)
            self.__logger.write(msg, self.__logger.ERROR)
            self.__oConexion.rollback()
            isSuccess = False
        oBus = {'isSuccess': isSuccess, 'message': msg, 'data': None}
        return (oBus)

    def __getLastID___(self):
        try:
            sql = 'SELECT MAX(id) FROM ' + self.__tableName
            cursor = self.__oConexion.execute(sql)
            res = cursor.fetchone()
            if (res[0] == None):
                id = 0
            else:
                id = res[0]
            self.__oConexion.commit()
        except:
            id = 0
            self.__oConexion.rollback()
        return (id)

    def getAllData(self, ruc=None):
        msg = None
        isSuccess = None
        data = []
        try:
            if (ruc == None):
                sql = "SELECT * FROM " + self.__tableName
            else:
                sql = "SELECT * FROM " + self.__tableName + " WHERE ruc='" + str(ruc) + "'"
            cursor = self.__oConexion.execute(sql)
            isSuccess = True
            data = []
            k = 0
            for row in cursor:
                data.append(k)
                data[k] = {'id': row[0], 'ruc': row[1], 'razonSocial': row[2], 'dirMatriz': row[3]}
                k = k + 1
            # get data
            cursor.close()
            del cursor
        except (Exception, psycopg2.DatabaseError) as ex_c:
            msg = str(ex_c)
            self.__logger.write(msg, self.__logger.ERROR)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess': isSuccess, 'message': msg, 'data': data})

    def getRows(self):
        msg = None
        isSuccess = None
        try:
            sql = 'SELECT * FROM ' + self.__tableName
            cursor = self.__oConexion.execute(sql)
            list = cursor.fetchall()
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            list = None
            msg = str(exception)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess': isSuccess, 'message': msg, 'data': list})

    def getRow(self):
        msg = None
        isSuccess = None
        try:
            sql = 'SELECT * FROM ' + self.__tableName + ' WHERE "id"=1'
            self.__oConexion.ejecutar(sql)
            data = self.__oConexion.vCursor.fetchone()
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            data = None
            msg = str(exception)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess': isSuccess, 'message': msg, 'data': data})

    def execQuery(self):
        res = 1
        msg = None
        isSuccess = None
        try:
            sql = 'SELECT * FROM ' + self.__tableName
            self.__oConexion.ejecutar(sql)
            lista = self.__oConexion.vCursor.fetchone();
            res = lista[0]  # index 0 (id=1)
            self.__oConexion.commit()
            isSuccess = True
        except StandardError, exception:
            res = None
            msg = str(exception)
            self.__oConexion.rollback()
            isSuccess = False
        return ({'isSuccess': isSuccess, 'message': msg, 'data': res})

    def close(self):
        self.__oConexion.close()


class ePerson():
    id = None
    document = None
    surname = None
    name = None
    birthday = None

    def __init__(self):
        id = 0
        document = ''
        surname = ''
        name = ''
        birthday = ''

    def __set__(self, instance, value):
        pass


