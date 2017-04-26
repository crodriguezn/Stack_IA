# -*- coding: utf-8 

"""
Created on '03/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from core.conexion import Conexion
from principal import *
import sys
import psycopg2
from helpers.logger import Log


# main ----------------------------------------
def main():
    app = QApplication(sys.argv)
    w = WPrincipal()
    db = Conexion();
    try:
        db.connect()
        db.close()
    except (Exception, psycopg2.DatabaseError) as ex_c:
        w.showMessage(str(ex_c), ERROR)
        msg = str(ex_c)
        logger = Log('BASE DE DATOS', Log.DEBUG)
        logger.write(msg, Log.DEBUG)
        sys.exit(0)
    w.show()
    sys.exit(app.exec_())


# end main

# execute main
if __name__ == '__main__':
    main()
