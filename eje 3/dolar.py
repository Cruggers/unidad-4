# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:31:54 2022

@author: Emiliano
"""

import json
from urllib.request import urlopen


class Dolar:
    __resultado=None
    def __init__(self):
        self.__resultado=None
    def run(self):
        url_template = "https://www.dolarsi.com/api/api.php?type=dolar"
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    def getResultado(self):
        return self.__resultado
    def getCambio(self,valor):
        datos=self.getResultado()
        conver=str(datos[0]['casa']['venta'])
        conver=conver.split(sep=(','))
        conver=conver[0]+'.'+conver[1]
        precio=float(conver)*valor
        return precio
