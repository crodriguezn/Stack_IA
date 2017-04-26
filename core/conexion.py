# -*- coding: utf-8 -*-
"""
Created on '15/01/2017'
@author: Luis Rodriguez
Computer __author__ = 'Desarrollador'
"""
import sys
from config import database as DB
import psycopg2


class Conexion(DB.DataBase):

    def __init__(self):
        self.__oDB = DB.DataBase
        self.__database           = self.__oDB.DBdatabase
        self.__user               = self.__oDB.DBuser;
        self.__password           = self.__oDB.DBpassword
        self.__host               = self.__oDB.DBhost
        self.__port               = self.__oDB.DBport
        self.__connection_factory = self.__oDB.DBconnection_factory
        self.__cursor_factory     = self.__oDB.DBcursor_factory
        self.__async              = self.__oDB.DBasync


    def connect(self):
        """try:
            self.vConnection = psycopg2.connect(database = self.__database, user = self.__user, password = self.__password, host = self.__host, port = self.__port, connection_factory = self.__connection_factory, async = self.__async)
            self.vCursor = self.vConnection.cursor()
        except StandardError, exception:
            msg = str(exception)
            __logger__         = logger.Log('BASE DE DATOS',logger.Log.DEBUG)
            __logger__.write(msg, __logger__.DEBUG)
            sys.exit()"""
        self.__db = psycopg2.connect(database = self.__database, user = self.__user, password = self.__password, host = self.__host, port = self.__port, connection_factory = self.__connection_factory, async = self.__async)

    def execute(self, command, data = None):
        cursor = self.__db.cursor()
        cursor.execute(command, data)
        return cursor;

    def cursor(self):
        pass

    def commit(self):
        self.__db.commit()

    def rollback(self):
        self.__db.rollback()

    def close(self):
        self.__db.close()

