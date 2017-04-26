# -*- coding: utf-8 

"""
Created on '14/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

from model.inplanet import *
mInplanet = mInplanet()
arrInplanet = {'id': 0, 'ruc': '0992267453001', 'razonSocial': 'INPLANET', 'dirMatriz': 'Malecón #312 y Federico Proaño'}
data = mInplanet.load(arrInplanet['ruc'], 'ruc', arrInplanet['id'], 'id')