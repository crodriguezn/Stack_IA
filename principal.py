# -*- coding: utf-8 

"""
Created on '26/02/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

import sys
import os

from modules.facial.consulta import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

#const error
(ERROR, INFOR, WARN) = (100, 101, 102)

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


class WPrincipal(QMainWindow):

    def __init__(self, parent=None):
        super(WPrincipal, self).__init__(parent)
        self.__initUI()
        FRM_PRINCIPAL = self


    def __initUI(self):
        #ventana de face
        self.initConsultarData()

        #imagen central
        self.lblImagen = QLabel(self)
        self.imagenIA = QPixmap(os.path.join('images/', 'inteligencia-artificial.png'))
        self.lblImagen.setPixmap(self.imagenIA)
        self.lblImagen.setGeometry(QRect(0, 60, 924, 412))
        #self.imagenIA.scaled(self.imagenIA.width(), self.imagenIA.height())
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lblImagen)

        #accion de salir
        exitAction = QAction(QIcon(os.path.join('images/icons', 'salir.png')),'&Salir', self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip(_fromUtf8('Salir de la Aplicación'))
        exitAction.triggered.connect(self.cerrar)

        #accion facial-entrenar
        faceEntrenarAction = QAction(QIcon(os.path.join('images/icons', '778289_multimedia_512x512.png')),'&Entrenar', self)
        faceEntrenarAction.setShortcut('ctrl+E')
        faceEntrenarAction.setStatusTip(_fromUtf8('App Reconocimiento | Facil | Entrenar'))
        faceEntrenarAction.triggered.connect(self.consultarData)

        #accion facial-comparar
        faceCompararAction = QAction(QIcon(os.path.join('images/icons', 'plainicon.com-46169-8af1-256px.png')),'&Comparar', self)
        faceCompararAction.setShortcut('ctrl+C')
        faceCompararAction.setStatusTip(_fromUtf8('App Reconocimiento | Facil | Comparar'))
        faceCompararAction.triggered.connect(self.knowledgeFaceComparar)

        #accion de voz
        voiceAction = QAction(QIcon(os.path.join('images/icons', 'icone-musica-gospel-8.png')),'&Voz', self)
        voiceAction.setShortcut('ctrl+V')
        voiceAction.setStatusTip(_fromUtf8('App Reconocimiento | Voz'))
        voiceAction.triggered.connect(self.knowledgeVoice)

        #accion de informacion
        infoAction = QAction(QIcon(os.path.join('images/icons', 'informacion.png')),'&Informacion', self)
        infoAction.setShortcut('ctrl+I')
        infoAction.setStatusTip(_fromUtf8('Ayuda | Información'))
        infoAction.triggered.connect(self.informacion)

        #barra de estado
        self.statusBar().showMessage('')
        barra_de_estado = self.statusBar()
        self.etiqueta_palabras = QLabel(_fromUtf8('Administrador | Copyright © 2017 by Luis Rodriguez'))
        barra_de_estado.addPermanentWidget(self.etiqueta_palabras)  # mensaje permanente

        menubar = self.menuBar()

        #menu inicio
        homeMenu = menubar.addMenu('&Inicio')
        homeMenu.addAction(exitAction)

        #menu aplicacion
        aplicationMenu = menubar.addMenu('&App Reconocimiento')
        faceMenu = aplicationMenu.addMenu(QIcon(os.path.join('images/icons', 'User-Interface-Face-Recognition-Scan-icon-150x150.png')),"&Facial")
        faceMenu.setStatusTip(_fromUtf8('App Reconocimiento | Facil'))
        faceMenu.addAction(faceEntrenarAction)
        faceMenu.addAction(faceCompararAction)
        aplicationMenu.addAction(voiceAction)


        #menu ayuda
        helpMenu = menubar.addMenu('&Ayuda')
        helpMenu.addAction(infoAction)

        self.toolbar = self.addToolBar('Salir')
        self.toolbar.addAction(exitAction)
        self.toolbar = self.addToolBar(_fromUtf8('Información'))
        self.toolbar.addAction(infoAction)


        # ícono ventana
        icono_ventana = QIcon(os.path.join('images/icons/', '328150.png'))
        self.setWindowIcon(icono_ventana)

        self.resize(924, 500)
        self.setWindowTitle(_fromUtf8('Aplicación de Inteligencia Artificial'))
        #self.resize(self.imagenIA.width(), self.imagenIA.height()+90)
        self.setFixedSize(self.size())
        #self.setEnabled(False) #desactivar la ventana
        self.center()
        #self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #self.move((screen.width() - size.width())/2, (screen.height() - size.height())/2)
        self.move(((screen.width()/2)-(self.frameSize().width()/2)),((screen.height()/2)-(self.frameSize().height()/2)))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, _fromUtf8('Confirmación de salir de la aplicación'),_fromUtf8("¿Desea salir de la aplicación?"), QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            event.ignore()

    def cerrar(self):
        self.close()

    def informacion(self):
        textInformacion = "The MIT License (MIT)\nCopyright © 2017 by Luis Rodriguez --IAUNEMI v1.0--\nEs un aplicativo de Inteligencia Artificial (IA) orientado a multiples funcionalidades"
        QMessageBox.about(self, _fromUtf8("Acerca de"), _fromUtf8(textInformacion))

    def consultarData(self):
        #print 'paso funcion knowledgeFaceEntrenar'
        self.WConsultarData.show()

    def knowledgeFaceComparar(self):
        print 'paso funcion knowledgeFaceComparar'

    def knowledgeVoice(self):
        print "paso funcion knowledgeVoice"

    def initConsultarData(self):
        self.WConsultarData = WConsultarData(self)


    def showMessage(self, message, type):
        title = self.windowTitle()
        if type == WARN:
           QMessageBox.warning(self, title, message)
        elif type == ERROR:
            QMessageBox.critical(self, title, message)
        else:
           QMessageBox.information(self, title, message)

def main():
    app = QApplication(sys.argv)
    ex = WPrincipal()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()