# -*- coding: utf-8 

"""
Created on '08/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests
import urllib2
import xml.etree.cElementTree as cET
from model.inplanet import mInplanet
from model.inplanet import eInplanet


def pWeb(URL):
    req = requests.get(URL)
    return req

URL_F = "http://openerp.in-planet.net/FIRMADOS/"
URL_A = "http://openerp.in-planet.net/AUTORIZADOS/"
URL_BASE = "http://jarroba.com/"
mInplanet = mInplanet()

# Realizamos la petición a la web
req = pWeb(URL_F)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    #entradas = html.find_all('table', {'class': 'col-md-4 col-xs-12'})
    entradas = html.find_all('a')
    #print(entradas)
    j = 0
    for i, entrada in enumerate(entradas):
        j += 1
        text = entrada.getText()
        if((not text=='Name') and (not text=='Last modified') and (not text=='Size') and (not text=='Description') and (not text=='Parent Directory')):
            num = len(text)
            tipo = text[num-4:num]
            if(tipo=='.xml'):
                print "%d - %s  |  %s" % (j, text, tipo)
                URL = URL_F + text
                #print(URL)
                fin = urllib2.urlopen(URL)
                tree = cET.parse(fin)
                root = tree.getroot()
                #for imp in root.getiterator("infoTributaria"):
                ambiente = None
                tipoEmision = None
                razonSocial = None
                ruc = None
                claveAcceso = None
                codDoc = None
                estab = None
                ptoEmi = None
                secuencial = None
                dirMatriz = None
                for child  in root:
                    #imp.text = '%.2f' %(float(imp.text) + float(imp.text)*.1)
                    #print child.tag
                    if(child.tag=='infoTributaria'):
                        #print 'infoTributaria'
                        """ambiente"""
                        for ambiente in child.iter('ambiente'):
                            ambiente = ambiente.text
                        """tipoEmision"""
                        for tipoEmision in child.iter('tipoEmision'):
                            tipoEmision = tipoEmision.text
                        """razonSocial"""
                        for razonSocial in child.iter('razonSocial'):
                            razonSocial = razonSocial.text
                        """ruc"""
                        for ruc in child.iter('ruc'):
                            ruc = ruc.text
                        """claveAcceso"""
                        for claveAcceso in child.iter('claveAcceso'):
                            claveAcceso = claveAcceso.text
                        """codDoc"""
                        for codDoc in child.iter('codDoc'):
                            codDoc = codDoc.text
                        """estab"""
                        for estab in child.iter('estab'):
                            estab = estab.text
                        """ptoEmi"""
                        for ptoEmi in child.iter('ptoEmi'):
                            ptoEmi = ptoEmi.text
                        """secuencial"""
                        for secuencial in child.iter('secuencial'):
                            secuencial = secuencial.text
                        """dirMatriz"""
                        for dirMatriz in child.iter('dirMatriz'):
                            dirMatriz = dirMatriz.text

                        """print "ambiente => %s - tipoEmision => %s" % (ambiente, tipoEmision)
                        print "razonSocial => %s - ruc => %s - dirMatriz => %s" % (razonSocial, ruc, dirMatriz)
                        print "claveAcceso => %s" % (claveAcceso)
                        print "codDoc => %s - estab => %s - ptoEmi => %s - secuencial => %s" % (codDoc, estab, ptoEmi, secuencial)"""
                        eInplanet = {'id': 0, 'ruc': ruc, 'razonSocial': razonSocial, 'dirMatriz': dirMatriz}
                        eInplanetInfoTributaria = {'id': 0, 'ambiente': int(ambiente), 'tipoEmision': int(tipoEmision), 'id_inplanet': eInplanet['id'], 'claveAcceso': claveAcceso, 'codDoc': codDoc, 'estab': estab, 'ptoEmi': ptoEmi, 'secuencial': secuencial}
                        print(eInplanet)
                        print(eInplanetInfoTributaria)
                        data = mInplanet.load(eInplanet['ruc'], 'ruc', eInplanet['id'], 'id' )

                        id = None
                        if (data['isSuccess']==True):
                            if(data['data']==None):
                                oBus = mInplanet.insert(eInplanet)
                                print(oBus['message'])
                            else:
                                id = int(data['data']['id'])
                                eInplanet = enInplanet()
                                eInplanet.id = id
                                eInplanet.ruc = data['data']['ruc']
                                print('ya existe id=> ', eInplanet.id, eInplanet.ruc)

                    """if(child.tag=='infoFactura'):
                        print 'infoFactura'
                    if(child.tag=='detalles'):
                        print 'detalles'"""


        else:
            j -= 1

        if(j==2):
            exit()
    """
    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        # Sino llamamos al método "getText()" nos devuelve también el HTML
        autor = entrada.find('span', {'class': 'autor'})
        fecha = entrada.find('span', {'class': 'fecha'}).getText()

        # Imprimo el Título, Autor y Fecha de las entradas
        print "%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha)
    """
else:
    print "Status Code %d" % status_code


