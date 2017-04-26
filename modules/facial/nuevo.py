# -*- coding: utf-8

"""
Created on '27/02/2017'
@author: Luis Rodriguez
Computer __author__ = 'Desarrollador'
"""

import sys
import os
import re
import cv2

from principal import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.uic import *
from helpers import helper_validacion as HV
from model.person import mPerson
from pyw.frmEntrenarNuevo import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

# Cargar nuestro archivo .ui
frmEntrenarNuevo = loadUiType("./uicForms/frmEntrenarNuevo.ui")[0]
frmEntrenarNuevoPYW = Ui_MWEntrenarNuevo

class WNuevo(QMainWindow, frmEntrenarNuevo):
    def __init__(self, parent=None):
        super(WNuevo, self).__init__(parent)
        self.setupUi(self)
        self.__initUI()

    def __initUI(self):

        # ícono ventana
        self.setWindowIcon(QIcon(os.path.join('images/icons/', 'plainicon.com-46169-8af1-256px.png')))
        self.txtNIP.textChanged.connect(self.validarNIP)
        self.txtApellido.textChanged.connect(self.validarApellido)
        self.txtNombre.textChanged.connect(self.validarNombre)
        self.birthday.setDate(QDate.currentDate())
        self.setTabOrder(self.txtNIP, self.txtApellido)
        self.setTabOrder(self.txtApellido, self.txtNombre)
        self.setTabOrder(self.txtNombre, self.btnGuardar)
        self.setTabOrder(self.btnGuardar, self.btnCancelar)
        self.txtNIP.setFocus()
        self.txtNIP.setStyleSheet("border: 1px solid gray;")
        self.txtApellido.setStyleSheet("border: 1px solid gray;")
        self.txtNombre.setStyleSheet("border: 1px solid gray;")

        self.setWindowTitle(_fromUtf8('Nuevo Datos de Entrenamiento Facial'))
        self.setFixedSize(self.size())
        self.center()

        self.btnCancelar.clicked.connect(self.cerrar)
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnGuardar.setStatusTip(_fromUtf8('Guardar Información'))
        self.btnCancelar.setStatusTip(_fromUtf8('Cerrar la ventana'))

        #barra de estado
        self.statusBar().showMessage('Captura')
        self.barra_de_estado = self.statusBar()
        self.etiqueta_palabras = QLabel(_fromUtf8('Administrador | Copyright © 2017 by Luis Rodriguez'))
        self.barra_de_estado.addPermanentWidget(self.etiqueta_palabras)  # mensaje permanente
        #self.initConsultarData()



    #Evento para cuando la ventana se muestra
    def showEvent(self, event):
        #self.barra_de_estado.setText("¡¡¡Bienvenido!!!")
        #self.setup_camera()
        pass

    def hideEvent(self, event):
        #self.barra_de_estado.setText("¡¡¡Bienvenido!!!")
        #self.quitCapture()
        pass

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(((screen.width()/2)-(self.frameSize().width()/2)),((screen.height()/2)-(self.frameSize().height()/2)))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, _fromUtf8('Solicitud de cierre'),_fromUtf8("¿Está seguro que desea cerrar?"), QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.initLimpiar()
            event.accept()
        else:
            event.ignore()

    def cerrar(self, isBan=False):
        if(not isBan):
            self.close()
        else:
            self.hide()


    def initLimpiar(self):
        self.txtNIP.clear()
        self.txtApellido.clear()
        self.txtNombre.clear()
        self.birthday.clear()
        self.lblTxtErrors.clear()
        self.txtNIP.setStyleSheet("border: 1px solid silver;")
        self.txtApellido.setStyleSheet("border: 1px solid silver;")
        self.txtNombre.setStyleSheet("border: 1px solid silver;")

    def validarNIP(self):
        NIP = self.txtNIP.text()
        validar = re.match('^[a-zA-Z0-9]+$', NIP, re.I)
        objValidacion = HV.HelperValicacion()
        if(objValidacion.isEmpty(NIP)):
            self.txtNIP.setStyleSheet("border: 2px solid #F8C471;")
            self.lblTxtErrors.setText(_fromUtf8('Error: No se permite Cédula/NIP en blanco'))
            self.lblTxtErrors.setStyleSheet("color: #F8C471;")
            self.txtNIP.setFocus()
            return False
        elif not validar:
            self.txtNIP.setStyleSheet("border: 2px solid #E74C3C;")
            self.lblTxtErrors.setText(_fromUtf8('Error: Solo se permite números y letras'))
            self.lblTxtErrors.setStyleSheet("color: #E74C3C;")
            self.txtNIP.setFocus()
            return False
        else:
            self.txtNIP.setStyleSheet("border: 2px solid #58D68D;")
            self.lblTxtErrors.clear()
            return True

    def validarApellido(self):
        apellido = self.txtApellido.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', apellido, re.I)
        objValidacion = HV.HelperValicacion()
        if(objValidacion.isEmpty(apellido)):
            self.txtApellido.setStyleSheet("border: 2px solid #F8C471;")
            self.lblTxtErrors.setText(_fromUtf8('Error: No se permite Apellidos en blanco'))
            self.lblTxtErrors.setStyleSheet("color: #F8C471;")
            self.txtApellido.setFocus()
            return False
        elif not validar:
            self.txtApellido.setStyleSheet("border: 2px solid #E74C3C;")
            self.lblTxtErrors.setText(_fromUtf8('Error: Solo se permite letras'))
            self.lblTxtErrors.setStyleSheet("color: #E74C3C;")
            self.txtApellido.setFocus()
            return False
        else:
            self.txtApellido.setStyleSheet("border: 2px solid #58D68D;")
            self.lblTxtErrors.clear()
            return True

    def validarNombre(self):
        nombre = self.txtNombre.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        objValidacion = HV.HelperValicacion()
        if(objValidacion.isEmpty(nombre)):
            self.txtNombre.setStyleSheet("border: 2px solid #F8C471;")
            self.lblTxtErrors.setText(_fromUtf8('Error: No se permite Nombres en blanco'))
            self.lblTxtErrors.setStyleSheet("color: #F8C471;")
            self.txtNombre.setFocus()
            return False
        elif not validar:
            self.txtNombre.setStyleSheet("border: 2px solid #E74C3C;")
            self.lblTxtErrors.setText(_fromUtf8('Error: Solo se permite letras'))
            self.lblTxtErrors.setStyleSheet("color: #E74C3C;")
            self.txtNombre.setFocus()
            return False
        else:
            self.txtNombre.setStyleSheet("border: 2px solid #58D68D;")
            self.lblTxtErrors.clear()
            return True

    def validarFRM(self):
        if not (self.validarNIP() and self.validarApellido() and self.validarNombre()):
            QMessageBox.warning(self, "Error", _fromUtf8('Información ingresada incorrecta'), QMessageBox.Ok);
            return False
        else:
            return True

    def guardar(self):
        self.__nip__         = str(self.txtNIP.text())
        apellido    = str(self.txtApellido.text())
        nombre      = str(self.txtNombre.text())
        birthday    = str(self.birthday.text())
        isCapture   = 0
        oPerson = mPerson()
        arrData = {'id':0, 'document':self.__nip__,'surname':apellido,'name':nombre,'birthday':birthday, 'isCapture':isCapture}
        rSG = QMessageBox.question(self, _fromUtf8('Solicitud de Guardar'),_fromUtf8("¿Está seguro que desea guardar?"), QMessageBox.Yes, QMessageBox.No)
        if rSG == QMessageBox.Yes and (self.validarFRM()):
            data = oPerson.insert(arrData)
            if(not data['isSuccess']):
                QMessageBox.warning(self, "Error", _fromUtf8(data['message']), QMessageBox.Ok);
            else:
                QMessageBox.information(self, "Mensaje", _fromUtf8(data['message']), QMessageBox.Ok);
                self.initLimpiar()
                self.cerrar(True)
