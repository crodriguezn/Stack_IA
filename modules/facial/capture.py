# -*- coding: utf-8 

"""
Created on '02/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

import cv2
import sys
import numpy
import os
import PyQt4


class faceCapture(object):
    __pathHaarcascades__ = None
    __fn_dir__ = None

    def __init__(self, fn_dir='faces/', fn_haar='haarcascades/', fn_name_haar='haarcascade_frontalface_alt.xml'):
        self.__fn_dir__ = fn_dir
        self.__pathHaarcascades__ = os.path.join(fn_haar, fn_name_haar)

    def ejecutar(self, fileName, fn_name):
        size = 4
        path = os.path.join(self.__fn_dir__, fileName)
        if not os.path.exists(path): os.makedirs(path)

        (im_width, im_height) = (112, 92)
        haar_cascade = cv2.CascadeClassifier(self.__pathHaarcascades__)
        webcam = cv2.VideoCapture(0)
        count = 0
        while count < 20:
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 0)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
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
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
                    1,(0, 255, 0))
                count += 1
            cv2.imshow('Captura de Rostro Facial', im)
            cv2.waitKey(10)
            """key = cv2.waitKey(10)
            if key == 27:
                break"""
        webcam.release()
        cv2.destroyAllWindows()
        return ({'isSuccess':True, 'message':None,'data':None})


