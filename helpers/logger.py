# -*- coding: utf-8 

"""
Created on '02/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""
import os
import logging
import logging.handlers
from datetime import datetime

class Log(object):
    # Los niveles son:
    #   DEBUG - El nivel mas alto
    #   INFO
    #   WARNING
    #   ERROR
    #   CRITIAL - El nivel mas bajo
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    logger = None

    def __init__(self, title=''):
        # Creamos una instancia al logger con el nombre especificado
        self.__title = title

    def write(self, msg, log_type=DEBUG):

        self.logger = logging.getLogger(self.__title)
        # Indicamos el nivel máximo de seguridad para los mensajes que queremos que se
        # guarden en el archivo de logs
        dt = datetime.today()

        nameFile = str(dt.hour)+'_'+str(dt.minute)+'_'+str(dt.second)+'.log'
        pathFile = 'default'
        if log_type == self.DEBUG:
            self.logger.setLevel(logging.DEBUG)
            #nameFile = 'debug.log'
            pathFile = 'log/debug/'+str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)+'/'

        if log_type == self.INFO:
            self.logger.setLevel(logging.INFO)
            #nameFile = 'info.log'
            pathFile = 'log/info/'+str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)+'/'

        if log_type == self.WARNING:
            self.logger.setLevel(logging.WARNING)
            #nameFile = 'warning.log'
            pathFile = 'log/warning/'+str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)+'/'

        if log_type == self.ERROR:
            self.logger.setLevel(logging.ERROR)
            #nameFile = 'error.log'
            pathFile = 'log/error/'+str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)+'/'

        if log_type == self.CRITICAL:
            self.logger.setLevel(logging.CRITICAL)
            #nameFile = 'critical.log'
            pathFile = 'log/critical/'+str(dt.year)+'/'+str(dt.month)+'/'+str(dt.day)+'/'

        if not os.path.exists(pathFile): os.makedirs(pathFile)

        # Creamos una instancia de logging.handlers, en la cual vamos a definir el nombre
        # de los archivos, la rotación que va a tener, y el formato del mismo

        # Si maxBytes=0, no rotara el archivo por tamaño
        # Si backupCount=0, no eliminara ningún fichero rotado
        file = os.path.join(pathFile, nameFile)
        handler = logging.handlers.RotatingFileHandler(filename=file, mode='a', maxBytes=1024, backupCount=5)

        # Definimos el formato del contenido del archivo de logs
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s \n %(message)s',datefmt='%y-%m-%d %H:%M:%S')
        # Añadimos el formato al manejador
        handler.setFormatter(formatter)

        # Añadimos el manejador a nuestro logging
        self.logger.addHandler(handler)

        if (log_type == self.DEBUG):
            self.logger.debug(msg)

        if (log_type == self.INFO):
            self.logger.info(msg)

        if (log_type == self.WARNING):
            self.logger.warning(msg)

        if (log_type == self.ERROR):
            self.logger.error(msg)

        if (log_type == self.CRITICAL):
            self.logger.critical(msg)
