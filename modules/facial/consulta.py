# -*- coding: utf-8 

"""
Created on '03/03/2017'
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
from model.person import mPerson
from modules.facial.nuevo import *
from helpers.setStyleSheet import *
from pyw.frmConsultaDataBD import *

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

# function size_desktop_local -----------------
# return QSize
def desktop():
    return QApplication.desktop().size()

# Cargar nuestro archivo .ui
frmDataTableBD = loadUiType("./uicForms/frmConsultaDataBD.ui")[0]
frmDataTableBDPYW = Ui_MWConsultaData

class WConsultarData(QMainWindow, frmDataTableBD):

    def __init__(self, parent=None):
        super(WConsultarData, self).__init__(parent)
        self.setupUi(self)
        self.__initUI()
        self.__initNuevo()
        self.oPersona = mPerson()


    def __initUI(self):

        # ícono ventana
        self.setWindowIcon(QIcon(os.path.join('images/icons/', 'Data-View-Details-icon.png')))

        self.setFixedSize(self.size())
        self.center()


        #barra de estado
        self.statusBar().showMessage('Captura')
        self.barra_de_estado = self.statusBar()
        self.etiqueta_palabras = QLabel(_fromUtf8('Administrador | Copyright © 2017 by Luis Rodriguez'))
        self.barra_de_estado.addPermanentWidget(self.etiqueta_palabras)  # mensaje permanente
        #self.show()

        size = desktop()
        height = size.height()
        width  = size.width()
        self.setGeometry(width/4, height/6, 730, 422);
        #self.setMaximumSize(700, 400);
        #self.setMinimumSize(700, 400);
        #self.setVisible(True)


        #boton

        #self.btnNuevo = QPushButton()
        self.btnNuevo.setStyleSheet(btn_success())
        self.btnNuevo.setIcon(QIcon(os.path.join('images/icons/', 'new.png')))
        self.btnNuevo.setIconSize(QSize(20,20))
        self.btnNuevo.clicked.connect(self.__clickNuevo)

        #self.btnCapturar = QPushButton()
        self.btnCapturar.setStyleSheet(btn_success())
        self.btnCapturar.setIcon(QIcon(os.path.join('images/icons/', 'face_scan.png')))
        self.btnCapturar.setIconSize(QSize(20,20))

        #self.btnEditar = QPushButton()
        self.btnEditar.setStyleSheet(btn_warning())
        self.btnEditar.setIcon(QIcon(os.path.join('images/icons/', 'edit.png')))
        self.btnEditar.setIconSize(QSize(20,20))

        #self.btnEliminar = QPushButton()
        self.btnEliminar.setStyleSheet(btn_danger())
        self.btnEliminar.setIcon(QIcon(os.path.join('images/icons/', 'delete.png')))
        self.btnEliminar.setIconSize(QSize(20,20))

        #self.btnActualizar = QPushButton()
        self.btnActualizar.setStyleSheet(btn_default())
        self.btnActualizar.setIcon(QIcon(os.path.join('images/icons/', 'refresh.png')))
        self.btnActualizar.setIconSize(QSize(20,20))
        self.btnActualizar.clicked.connect(self.actionActualizar)

        #self.btnCancelar = QPushButton()
        self.btnCancelar.setStyleSheet(btn_primary())
        self.btnCancelar.setIcon(QIcon(os.path.join('images/icons/', 'icono_cancelar.png')))
        self.btnCancelar.setIconSize(QSize(20,20))
        self.btnCancelar.clicked.connect(self.cerrar)



        #self.table.setSortingEnabled(True)
        #self.table.resizeColumnsToContents()
        """self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 130)
        self.table.setColumnWidth(3, 130)
        self.table.setColumnWidth(4, 158)
        self.table.setColumnWidth(5, 100)"""

        #self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        #self.table.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        #self.table.setDragEnabled(True)
        #self.table.setDragDropMode(QAbstractItemView.DragDrop)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.cellDoubleClicked.connect(self.cell_double_clicked)
        #self.table.resizeRowToContents(False)
        #self.table.cellClicked.connect(self.slotItemClicked)

        self.table.setStyleSheet(table_view())



    def __initNuevo(self):
        self.WNuevo = WNuevo(self)
        #self.ventanaWKF.setWindowTitle('Ventana hija')
        #self.ventanaWKF.resize(240, 200)


    def __clickNuevo(self):
        #print 'paso funcion knowledgeFaceEntrenar'
        self.WNuevo.show()
        #self.WNuevo.hide()

    #Evento para cuando la ventana se muestra
    def showEvent(self, event):
        #self.barra_de_estado.setText("¡¡¡Bienvenido!!!")
        #self.setup_camera()
        print'pasa'
        self.actionActualizar()

    def hideEvent(self, event):
        #self.barra_de_estado.setText("¡¡¡Bienvenido!!!")
        #self.quitCapture()
        self.actionActualizar()

    def actionActualizar(self):
        print "click actualiar"
        self.viewAllData()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(((screen.width()/2)-(self.frameSize().width()/2)),((screen.height()/2)-(self.frameSize().height()/2)))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, _fromUtf8('Solicitud de cierre'),_fromUtf8("¿Está seguro que desea cerrar?"), QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            #self.initLimpiar()
            event.accept()
        else:
            event.ignore()

    def cerrar(self, isBan=False):
        if(not isBan):
            self.close()
        else:
            self.hide()

    def viewAllData(self):

        oMPerson = mPerson()
        arrData = oMPerson.getAllData()

        if not arrData['isSuccess']:
            return
        elif arrData['data'] == []:
            self.statusBar.showMessage('Last Action: Table Empty')
            print 'Last Action: Table Empty'
            return

        dictData = arrData['data']
        # rows and columns
        num_rows = len(dictData)
        num_cols = len(dictData[0])
        self.table.clearContents()

        self.table.setRowCount(num_rows)
        self.table.setColumnCount(num_cols)
        self.table.setHorizontalHeaderLabels(['ID','Documento', 'Apellidos','Nombres', 'Fecha Nac.','Capturado?', _fromUtf8('Acción')])
        self.table.hideColumn(0)
        stdFlags = Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled

        n = 0
        for data in dictData:
            if n % 2 == 0:
                background = QColor(229, 229, 229)
            else:
                background = QColor(255, 255, 255)
            #id
            id = QTableWidgetItem()
            id.setText(str(data['id']))
            id.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            id.setFlags(stdFlags)
            id.setBackground(background)
            self.table.setItem(n, 0, id)

            #documento
            document = QTableWidgetItem()
            document.setText(str(data['document']))
            document.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            document.setFlags(stdFlags)
            document.setBackground(background)
            self.table.setItem(n, 1, document)

            #surname
            surname = QTableWidgetItem()
            surname.setText(str(data['surname']))
            surname.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
            surname.setFlags(stdFlags)
            surname.setBackground(background)
            self.table.setItem(n, 2, surname)

            #name
            name = QTableWidgetItem()
            name.setText(str(data['name']))
            name.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
            name.setFlags(stdFlags)
            name.setBackground(background)
            self.table.setItem(n, 3, name)

            #birthday
            birthday = QTableWidgetItem()
            birthday.setText(str(data['birthday']))
            birthday.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            birthday.setFlags(stdFlags)
            birthday.setBackground(background)
            self.table.setItem(n, 4, birthday)

            #isCapture
            lblImagen = QLabel()

            if(data['isCapture']==1):
                _isCapture = os.path.join('images/icons/', 'ok_accept.png')
            else:
                _isCapture = os.path.join('images/icons/', 'cancel.png')
            lblImagen.setPixmap(QPixmap(_isCapture).scaled(20, 20))
            lblImagen.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

            self.table.setCellWidget(n, 5, lblImagen)
            self.table.setItem(n, 5, QTableWidgetItem())
            self.table.item(n, 5).setBackground(background)

            """
            button_layout = QHBoxLayout()
            button_layout.setContentsMargins(0,0,0,0)
            button_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            button_layout.addWidget(btnCapturar)
            button_layout.addWidget(btnEditar)
            button_layout.addWidget(btnEliminar)

            buttons_widget = QWidget()
            buttons_widget.setLayout(button_layout)

            self.table.setCellWidget(n, 6, buttons_widget)
            btnCapturar.clicked.connect(self.handleButtonClicked)
            #btnEditar.clicked.connect(self.handleButtonClicked)"""
            n += 1


    def handleButtonClicked(self):
        button = qApp.focusWidget()
        # or button = self.sender()
        print(self.sender().parent() is self)
        index = self.table.indexAt(button.pos())
        if index.isValid():
            mydata = str(self.table.item(index.row(), 2).text())
            print(mydata)
            print(index.row(), index.column())

    @pyqtSlot(int,int)
    def slotItemClicked(self,item,item2):
        QMessageBox.information(self,"QTableWidget Cell Click","Row: "+QString.number(item)+" |Column: "+QString.number(item2))

    @pyqtSlot(int, int)
    def cell_double_clicked(self, row, column):
        print('cell double clicked (row: {}, column: {})'.format(row, column))
        #self.output_text.appendPlainText('cell double clicked (row: {}, column: {})'.format(row, column))
        #self.scroll_to_end()
        print(str(self.table.item(row, column).text()))
        QMessageBox.warning(self, _fromUtf8('Información'),_fromUtf8(str(row)), QMessageBox.Ok)

    def slotSearch(self):
        txtdni = self.leDni.text()
        if len(txtdni) <> 8:
            self.statusBar.showMessage('Last Action: Dni incorrecta')
            print 'Last Action: Cell Dni data incorrect'
            self.clearCells()
            return
        else:
            self.search(txtdni)


"""def main():
    app = QApplication(sys.argv)
    ex = dataTableBD()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()"""