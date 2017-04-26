# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uicForms\frmCapture.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MWCapture(object):
    def setupUi(self, MWCapture):
        MWCapture.setObjectName(_fromUtf8("MWCapture"))
        MWCapture.resize(651, 433)
        self.centralwidget = QtGui.QWidget(MWCapture)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(20, 20, 611, 51))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 611, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ImgWidget = QtGui.QWidget(self.groupBox)
        self.ImgWidget.setGeometry(QtCore.QRect(10, 20, 591, 241))
        self.ImgWidget.setObjectName(_fromUtf8("ImgWidget"))
        MWCapture.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MWCapture)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MWCapture.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MWCapture)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MWCapture.setStatusBar(self.statusbar)

        self.retranslateUi(MWCapture)
        QtCore.QMetaObject.connectSlotsByName(MWCapture)

    def retranslateUi(self, MWCapture):
        MWCapture.setWindowTitle(_translate("MWCapture", "MainWindow", None))
        self.startButton.setText(_translate("MWCapture", "Start Video", None))
        self.groupBox.setTitle(_translate("MWCapture", "Video", None))

