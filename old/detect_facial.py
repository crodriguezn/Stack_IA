# -*- coding: utf-8 

"""
Created on '15/01/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

import cv2
from classForms import classFormDetectarFaceSave as cfDFS
from PyQt4 import QtCore, QtGui, uic
import sys


# Cargar nuestro archivo .ui
form_class = uic.loadUiType("./forms/mwDetectarFaceSave.ui")[0]

app = QtGui.QApplication(sys.argv)
MyWindow = cfDFS.DetectarFaceSave(None)
MyWindow.show()
app.exec_()