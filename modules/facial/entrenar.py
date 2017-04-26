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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.uic import *
from helpers import helper_validacion as HV
from model.person import mPerson
from modules.facial import capture

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
frmEntrenar = loadUiType("./uicForms/frmEntrenarFacial.ui")[0]

class faceEntrenar(QMainWindow, frmEntrenar):

    def __init__(self, parent=None):
        super(faceEntrenar, self).__init__(parent)
        self.video_size = QSize(320, 240)
        self.setupUi(self)
        self.initUI()



    def initUI(self):

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

        self.setWindowTitle(_fromUtf8('Entrenamiento Facial'))
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

        self.image_label.setFixedSize(self.video_size)

    #Evento para cuando la ventana se muestra
    def showEvent(self, event):
        #self.barra_de_estado.setText("¡¡¡Bienvenido!!!")
        #self.setup_camera()
        pass

    def hideEvent(self, event):
        #self.barra_de_estado.setText("¡¡¡Bienvenido!!!")
        #self.quitCapture()
        pass

    def quitCapture(self):
        print "pressed Quit"
        #self.capture.release()
        #cv2.VideoCapture.release()
        #cv2.destroyAllWindows()

        #QCoreApplication.quit()

    def setup_camera(self):
        """Initialize camera.
        """
        #self.capture = cv2.VideoCapture(0)
        #self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        #self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())



    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        size = 4
        (im_width, im_height) = (112, 92)
        haar_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
        fn_dir='faces/'
        path = os.path.join(fn_dir, self.__nip__)
        if not os.path.exists(path): os.makedirs(path)
        webcam = cv2.VideoCapture(0)
        count = 0
        while count < 20:
            (rval, frame) = webcam.read()
            frame = cv2.flip(frame, 1, 0)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
            faces = haar_cascade.detectMultiScale(mini)
            faces = sorted(faces, key=lambda x: x[3])
            if faces:
                face_i = faces[0]
                (x, y, w, h) = [v * size for v in face_i]
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (im_width, im_height))
                pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
                       if n[0]!='.' ]+[0])[-1] + 1
                cv2.imwrite('%s/%s.png' % (path, pin), face_resize)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(frame, self.__text__, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
                count += 1
            cv2.waitKey(10)
            image = QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QImage.Format_RGB888)
            #image = cv2.imshow('Captura de Rostro Facial', im)
            self.image_label.setPixmap(QPixmap.fromImage(image))
        webcam.release()
        cv2.destroyAllWindows()

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
        oPerson = person.personModel()
        arrData = {'id':0, 'document':self.__nip__,'surname':apellido,'name':nombre,'birthday':birthday}
        rSG = QMessageBox.question(self, _fromUtf8('Solicitud de Guardar'),_fromUtf8("¿Está seguro que desea guardar?"), QMessageBox.Yes, QMessageBox.No)
        if rSG == QMessageBox.Yes:
            if(self.validarFRM()):
                data = oPerson.insert(arrData)
                if(not data['isSuccess']):
                    QMessageBox.warning(self, "Error", _fromUtf8(data['message']), QMessageBox.Ok);
                else:
                    #obj = capture.faceCapture('../../faces/','../../haarcascades/')


                    self.__text__ = apellido+' '+nombre
                    #self.timer.timeout.connect()
                    self.display_video_stream()
                    QMessageBox.information(self, "Mensaje", _fromUtf8(data['message']), QMessageBox.Ok);
                    self.initLimpiar()
                    self.cerrar(True)
                    """obj = capture.faceCapture()
                    text = apellido+' '+nombre
                    dataCapture = obj.ejecutar(nip, text)
                    if(dataCapture['isSuccess']):
                        QMessageBox.information(self, "Mensaje", _fromUtf8(data['message']), QMessageBox.Ok);
                        """
