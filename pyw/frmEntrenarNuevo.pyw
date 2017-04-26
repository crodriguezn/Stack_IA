# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uicForms\frmEntrenarNuevo.ui'
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

class Ui_MWEntrenarNuevo(object):
    def setupUi(self, MWEntrenarNuevo):
        MWEntrenarNuevo.setObjectName(_fromUtf8("MWEntrenarNuevo"))
        MWEntrenarNuevo.setWindowModality(QtCore.Qt.WindowModal)
        MWEntrenarNuevo.resize(693, 281)
        self.centralwidget = QtGui.QWidget(MWEntrenarNuevo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 91, 101, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.txtApellido = QtGui.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(120, 91, 201, 20))
        self.txtApellido.setMaxLength(100)
        self.txtApellido.setObjectName(_fromUtf8("txtApellido"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 62, 101, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtNIP = QtGui.QLineEdit(self.centralwidget)
        self.txtNIP.setGeometry(QtCore.QRect(120, 60, 201, 20))
        self.txtNIP.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtNIP.setToolTip(_fromUtf8(""))
        self.txtNIP.setMaxLength(40)
        self.txtNIP.setObjectName(_fromUtf8("txtNIP"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 90, 61, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtNombre = QtGui.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(460, 90, 201, 20))
        self.txtNombre.setMaxLength(100)
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 60, 101, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 169, 671, 61))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnGuardar = QtGui.QPushButton(self.groupBox)
        self.btnGuardar.setGeometry(QtCore.QRect(210, 20, 110, 30))
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        self.btnCancelar = QtGui.QPushButton(self.groupBox)
        self.btnCancelar.setGeometry(QtCore.QRect(360, 20, 110, 30))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.lblTxtErrors = QtGui.QLabel(self.centralwidget)
        self.lblTxtErrors.setGeometry(QtCore.QRect(10, 124, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTxtErrors.setFont(font)
        self.lblTxtErrors.setFrameShadow(QtGui.QFrame.Plain)
        self.lblTxtErrors.setText(_fromUtf8(""))
        self.lblTxtErrors.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTxtErrors.setObjectName(_fromUtf8("lblTxtErrors"))
        self.birthday = QtGui.QDateEdit(self.centralwidget)
        self.birthday.setGeometry(QtCore.QRect(460, 60, 101, 22))
        self.birthday.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.birthday.setWrapping(True)
        self.birthday.setFrame(True)
        self.birthday.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.birthday.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.birthday.setMinimumDate(QtCore.QDate(1900, 9, 14))
        self.birthday.setDisplayFormat(_fromUtf8("yyyy-MM-dd"))
        self.birthday.setCalendarPopup(True)
        self.birthday.setObjectName(_fromUtf8("birthday"))
        MWEntrenarNuevo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MWEntrenarNuevo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MWEntrenarNuevo.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MWEntrenarNuevo)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MWEntrenarNuevo.setStatusBar(self.statusbar)

        self.retranslateUi(MWEntrenarNuevo)
        QtCore.QMetaObject.connectSlotsByName(MWEntrenarNuevo)
        MWEntrenarNuevo.setTabOrder(self.txtNIP, self.txtApellido)
        MWEntrenarNuevo.setTabOrder(self.txtApellido, self.txtNombre)
        MWEntrenarNuevo.setTabOrder(self.txtNombre, self.birthday)
        MWEntrenarNuevo.setTabOrder(self.birthday, self.btnGuardar)
        MWEntrenarNuevo.setTabOrder(self.btnGuardar, self.btnCancelar)

    def retranslateUi(self, MWEntrenarNuevo):
        MWEntrenarNuevo.setWindowTitle(_translate("MWEntrenarNuevo", "Reconocimiento Facial -- Guardar", None))
        self.label.setText(_translate("MWEntrenarNuevo", "Apellidos:", None))
        self.label_2.setText(_translate("MWEntrenarNuevo", "Cédula/Pasaporte:", None))
        self.label_3.setText(_translate("MWEntrenarNuevo", "Nombres:", None))
        self.label_4.setText(_translate("MWEntrenarNuevo", "DATOS PERSONALES", None))
        self.label_5.setText(_translate("MWEntrenarNuevo", "Fecha Nacimiento:", None))
        self.btnGuardar.setText(_translate("MWEntrenarNuevo", "Guardar", None))
        self.btnCancelar.setText(_translate("MWEntrenarNuevo", "Cancelar", None))

