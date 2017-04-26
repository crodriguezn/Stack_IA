# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uicForms\frmConsultaDataBD.ui'
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

class Ui_MWConsultaData(object):
    def setupUi(self, MWConsultaData):
        MWConsultaData.setObjectName(_fromUtf8("MWConsultaData"))
        MWConsultaData.setWindowModality(QtCore.Qt.WindowModal)
        MWConsultaData.resize(730, 422)
        self.centralwidget = QtGui.QWidget(MWConsultaData)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 521, 361))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(540, 20, 161, 271))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnCapturar = QtGui.QPushButton(self.groupBox)
        self.btnCapturar.setGeometry(QtCore.QRect(28, 60, 110, 30))
        self.btnCapturar.setObjectName(_fromUtf8("btnCapturar"))
        self.btnEditar = QtGui.QPushButton(self.groupBox)
        self.btnEditar.setGeometry(QtCore.QRect(28, 101, 110, 30))
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))
        self.btnEliminar = QtGui.QPushButton(self.groupBox)
        self.btnEliminar.setGeometry(QtCore.QRect(28, 140, 110, 30))
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.btnNuevo = QtGui.QPushButton(self.groupBox)
        self.btnNuevo.setGeometry(QtCore.QRect(28, 20, 110, 30))
        self.btnNuevo.setObjectName(_fromUtf8("btnNuevo"))
        self.btnActualizar = QtGui.QPushButton(self.groupBox)
        self.btnActualizar.setGeometry(QtCore.QRect(28, 180, 110, 30))
        self.btnActualizar.setObjectName(_fromUtf8("btnActualizar"))
        self.btnCancelar = QtGui.QPushButton(self.groupBox)
        self.btnCancelar.setGeometry(QtCore.QRect(28, 220, 110, 30))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        MWConsultaData.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MWConsultaData)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MWConsultaData.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MWConsultaData)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MWConsultaData.setStatusBar(self.statusbar)

        self.retranslateUi(MWConsultaData)
        QtCore.QMetaObject.connectSlotsByName(MWConsultaData)

    def retranslateUi(self, MWConsultaData):
        MWConsultaData.setWindowTitle(_translate("MWConsultaData", "Consulta de Datos", None))
        self.groupBox.setTitle(_translate("MWConsultaData", "Acciones", None))
        self.btnCapturar.setText(_translate("MWConsultaData", "Capturar", None))
        self.btnEditar.setText(_translate("MWConsultaData", "Editar", None))
        self.btnEliminar.setText(_translate("MWConsultaData", "Eliminar", None))
        self.btnNuevo.setText(_translate("MWConsultaData", "Nuevo", None))
        self.btnActualizar.setText(_translate("MWConsultaData", "Actualizar", None))
        self.btnCancelar.setText(_translate("MWConsultaData", "Cancelar", None))

