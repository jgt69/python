'''

Created on 3 abr. 2020

'''
# -*- coding: utf-8 -*-

class Periferico():
    
    def __init__(self, id=0, tipo="", marca="X", modelo="X", gama="", precio=0.0):

        self.id = id
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.gama = gama
        self.precio = precio
        
    def a_texto(self):
        
        return "Tipo: {} Marca: {} Modelo: {} Gama: {} Precio: {} \n".format(self.tipo, self.marca, self.modelo,
                                                                          self.gama, self.precio) 