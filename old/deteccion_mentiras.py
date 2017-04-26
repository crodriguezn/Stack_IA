# -*- coding: utf-8 

"""
Created on '15/01/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

import cv2
import numpy as np

class Detectar(object):

    def __init__(self):
        self.camara = cv2.VideoCapture(0)
        self.contador = 0

    def get_image(self):
        im = cv2.QueryFrame(self.camara)
        return im

    def loop(self):
        # Creamos una copia para poderla modificar
        captura, mostrar = self.detectar(self.get_image())
        if mostrar:
            cv2.ShowImage("!Lies - eyes", captura)

    def detectar(self, imagen):
        global centro

        copia = cv2.cloneImage(imagen)
        # Tomamos imagen
        dimensiones = cv2.resize(copia)
        # La transformamos a escala de grises para mayor rapidez
        grises = cv2.CreateImage(dimensiones, 8, 1)
        cv2.CvtColor(copia, grises, cv2.CV_RGB2GRAY) # cv.CvtColor(src, dst, code)

        storage = cv2.CreateMemStorage() # video

        # Ecualizamos el histograma
        cv2.EqualizeHist(grises, grises)

        #Suavizo la imagen para eliminar el ruido
        cv2.Smooth(grises, grises, cv2.CV_GAUSSIAN,5,5)

        # Cargamos el fichero cascada para ojos
        ojos = cv2.Load("./haarcascades/haarcascade_eye_tree_eyeglasses.xml")

        # Reconocemos los objetos
        objOjo = cv2.HaarDetectObjects(copia, ojos, storage, 1.1, 2, 0, (120, 120))

        #print objOjo
        mostrar = False
        if 0 < len(objOjo) < 3 :
            #(x, y, ancho, alto) del area que nos interesa
            area = ( objOjo[0][0][0],
                        objOjo[0][0][1],
                        objOjo[0][0][2],
                        objOjo[0][0][3]
                )
            for i in objOjo:
                # cortamos el area que nos interesa
                cv2.SetImageROI(copia, area)



                # Una vez teniendo el area que nos interesa tenemos que
                # aplciarle filtros para que deteccion de circulos funcione bien
                image_size = cv2.GetSize(copia)

                gray = cv2.CreateImage(image_size, 8, 1)

                #Creo la matriz en la que voy a meter los posibles circulos
                #Si el numero de circulos es mayor que 8, el programa no funciona

                storageCir = cv2.CreateMat(1, 8, cv2.CV_32FC3)

                cv2.CvtColor(copia, gray, cv2.CV_RGB2GRAY) # cv.CvtColor(src, dst, code)

                # Ecualizamos el histograma
                cv2.EqualizeHist(gray, gray)

                #Suavizo la imagen para eliminar el ruido
                cv2.Smooth(gray, gray, cv2.CV_GAUSSIAN,5,5)

                # buscamos circulos.... aqui nos concentraremos en buscar la iris
                #circles = cv.HoughCircles(grayImg, storage, cv.CV_HOUGH_GRADIENT, 2, 10,32,200,minRad, minRad*2)


                dp = 2
                minDist = 200.0
                param1 = 32
                param2 = 60
                minRadius = 12
                maxRadius = 24
                cv2.HoughCircles(gray, storageCir, cv2.CV_HOUGH_GRADIENT, dp, minDist,
                                    param1, param2, minRadius, maxRadius)

                #print storageCir.cols
                #print "----"

                # recorremos los circulos encontrados
                for n in range(0, storageCir.cols): # storage.cols contiene el numero de circulos encontrados

                    #Obtengo la tupla que contiene los valores del primer circulo
                    r = cv2.Get1D(storageCir, n)
                    #"c" es una tupla de dos valores redondeados (cv.round)
                    #que contiene la posicion del circulo
                    c = (cv2.Round(r[0]), cv2.Round(r[1]))
                    #Dibujo el circulo
                    # Circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
                    cv2.Circle(copia, c, cv2.Round(r[2]), cv2.CV_RGB(255,1,1), 2)
                    cv2.Circle(copia, c, 1, cv2.CV_RGB(0,255,0), 2)

                    # incrementamos contador hasta 200, que seran los veces para calcular el promedio
                    intentos = 50
                    separacion = 10
                    if self.getContador() < intentos:
                        cont = self.getContador() + 1
                        self.setContador(cont)

                        centro[0] = centro[0] + c[0]
                        centro[1] = centro[1] + c[1]
                    else:
                        x = centro[0] / intentos
                        y = centro[1] / intentos
                        print "+++"
                        cv2.Circle(copia, (x, y), 1, cv2.CV_RGB(0,0,255), 2)
                        # metemos un filtro para no tomar lo centro parecidos pero iguales
                        diff_x = abs(x - c[0])
                        diff_y = abs(y - c[1])
                        if diff_y > separacion and diff_x > separacion:
                            # hacer algo estan muy separados
                            print "AGUAS!"
                            cv2.Circle(copia, c, cv2.Round(r[2]), cv2.CV_RGB(255,255,255), 2)


                mostrar = True

        return copia, mostrar


    def setContador(self, contador):
        self.contador = contador
        return

    def getContador(self):
        return self.contador

    def main(self):
        while (cv2.waitKey(15)==-1):
            self.loop()

centro = [0, 0]

cv2.namedWindow("!Lies - eyes")
Detectar().main()