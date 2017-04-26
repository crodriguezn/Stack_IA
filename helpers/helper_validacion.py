# -*- coding: utf-8 

"""
Created on '15/01/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

class HelperValicacion():

    def __init__(self):
        pass

    def isEmpty(self, data=None):
        if(data==None):
            return True
        elif(len(data)==0):
            return True
        else:
            return False
