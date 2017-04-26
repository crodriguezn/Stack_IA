# -*- coding: utf-8 

"""
Created on '02/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

from PyQt4 import QtCore,QtGui
import sys
import cv2
import numpy as np

class ImageWidget(QtGui.QWidget):
    def __init__(self,parent=None):
        super(ImageWidget,self).__init__(parent)
        self.image=None

    def setImage(self,image):
        self.image=image
        sz=image.size()
        self.setMinimumSize(sz)
        self.update()

    def paintEvent(self,event):
        qp=QtGui.QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0,0),self.image)
        qp.end()

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.videoFrame=ImageWidget()
        self.setCentralWidget(self.videoFrame)
        self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateImage)
        self.timer.start(30)
        self.capture = cv2.VideoCapture(0)

    def updateImage(self):
        _, img = self.capture.read()
        #img=cv2.cvtColor(img, cv.CV_BGR2RGB)
        height, width, bpc = img.shape
        bpl = bpc * width
        image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
        self.videoFrame.setImage(image)


def main():
    app=QtGui.QApplication(sys.argv)
    w=MainWindow()
    w.show()
    app.exec_()

if __name__=='__main__':
    main()