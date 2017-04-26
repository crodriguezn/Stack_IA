# -*- coding: utf-8

"""
Created on '26/02/2017'
@author: Luis Rodriguez
Computer __author__ = 'Desarrollador'
"""
import sys
import os

from PyQt4 import QtGui, QtCore
from PyQt4 import QtWebKit
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        #imagen central
        self.webView = QtWebKit.QWebView(self)
        self.webView.setGeometry(QtCore.QRect(0, 60, 1024, 512))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.webView.load(QUrl(os.path.join('images/', 'inteligencia-artificial.png')))



        exitAction = QtGui.QAction(QtGui.QIcon(os.path.join('images/icons', 'exit.png')),'&Exit', self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip('Salir de la Aplicación')
        exitAction.triggered.connect(self.close)

        self.statusBar().showMessage('Bienvenido Administrador')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)


        self.toolbar = self.addToolBar('Salir')
        self.toolbar.addAction(exitAction)


        # ícono ventana
        icono_ventana = QtGui.QIcon(os.path.join('images/icons/', '328150.png'))
        self.setWindowIcon(icono_ventana)

        self.setGeometry(200, 100, 1024, 600)
        self.setWindowTitle('Reconocimiento Facial')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()