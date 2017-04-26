# -*- coding: utf-8 -*-
"""
Created on '15/01/2017'
@author: Luis Rodriguez
Computer __author__ = 'Desarrollador'
"""

#parametros para la conexion

class DataBase:
    DBdatabase              = 'ia_facial'
    DBuser                  = 'postgres'
    DBpassword              = 'postgres0'
    DBhost                  = 'localhost'
    DBport                  = 5432
    DBconnection_factory    = None
    DBcursor_factory        = None
    DBasync                 = False