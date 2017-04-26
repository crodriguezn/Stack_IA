# -*- coding: utf-8 

"""
Created on '15/01/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
if face_cascade.empty(): raise Exception("¿Está seguro que es la ruta correcta?")

eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
if eye_cascade.empty(): raise Exception("¿Está seguro que es la ruta correcta?")

video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            print "x="+str(x)
            print "y="+str(y)
            print "w="+str(w)
            print "h="+str(h)

            #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
            cv2.circle(frame,(x,w), 63, (255,0,0), 2) #circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()