'''

Created on 7 abr. 2020

'''
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5.Qt import QMessageBox, QPushButton, QTableWidgetItem
from PyQt5.QtCore import QFile, QTextStream

from windows.Main_Window import VentanaTienda
from windows.Registro_3 import RegistroMain
from windows.Listado_1 import Listado1Main
from windows.Listado_2 import Listado2Main
from windows.Listado_3_btn import TableWidget
from windows.Editar_Registro_2 import EditarRegistro

from modelo.clases import Periferico
from modelo.operaciones_bd import registro_periferico
from modelo.operaciones_bd import obtener_listado
from modelo.operaciones_bd import obtener_listado_NOID
from modelo.operaciones_bd import borrar_item
from modelo.operaciones_bd import obtener_item_por_id
from modelo.operaciones_bd import guardar_cambios_producto

import sys
from functools import partial

productos = None


def mostrar_registro():
    ui_registro.setupUi(MainWindow)
    QMessageBox.about(MainWindow, "AVISO", "Es necesario completar todos los campos \nantes de pulsar sobre 'ENVIAR' ")
    ui_registro.btn_registrar.clicked.connect(registrar_periferico)


def registrar_periferico():
    periferico = Periferico()
    periferico.tipo = ui_registro.cbx_tipo.currentText()
    periferico.marca = ui_registro.txt_marca.text()
    periferico.modelo = ui_registro.txt_modelo.text()
    periferico.gama = ui_registro.cbx_gama.currentText()
    periferico.precio = float(ui_registro.txt_precio.text().replace(",", "."))
        
    registro_periferico(periferico)

    ui_registro.txt_marca.setText("")
    ui_registro.txt_modelo.setText("")
    ui_registro.txt_precio.setText("")
    
    index = ui_registro.cbx_tipo.findText("Accessory", QtCore.Qt.MatchFixedString)
    index2 = ui_registro.cbx_gama.findText("Basic", QtCore.Qt.MatchFixedString)
        
    ui_registro.cbx_tipo.setCurrentIndex(index)
    ui_registro.cbx_gama.setCurrentIndex(index2)

    QMessageBox.about(MainWindow, "Info", "Registro OK")
    print("Registro OK")


def mostrar_listado1():
    ui_listado1.setupUi(MainWindow)
    perifericos = obtener_listado_NOID()
    texto = ""
    for p in perifericos:
        texto += " Tipo: " + p[0] + " | Marca: " + p[1] + " | Modelo: " + p[2] + " | Gama: " + p[3] + " | Precio: " + str(p[4]) + "€\n"
    ui_listado1.txt_listado1.setText(texto)


def mostrar_listado2():
    global productos
    ui_listado2.setupUi(MainWindow)
    productos = obtener_listado_NOID()

    for p in productos:
        ui_listado2.lst_listado2.addItem(" Producto: " + p[0] + "  |  Marca: "+ p[1] + "  |  Modelo: " + p[2])
        
    ui_listado2.lst_listado2.itemClicked.connect(ver_detalles_producto)


def ver_detalles_producto():
    indice_seleccionado = ui_listado2.lst_listado2.currentRow()
    producto = productos[indice_seleccionado]
    
    info =""
    info += "Tipo de producto: " + str(producto[0]) + "\n"
    info += "Marca: " + str(producto[1]) + "\n"
    info += "Modelo: " + str(producto[2]) + "\n"
    info += "Gama: " + str(producto[3]) + "\n"
    info += "Precio: " + str(producto[4]) + "€"
    
    QMessageBox.about(MainWindow,"Info del Producto", info)
    

def mostrar_table():
    ui_table.setupUi(MainWindow)
    fila = 0
    
    for registro in obtener_listado():
        ui_table.tbl_perifericos.insertRow(fila)
        columna = 0
    
        for elemento in registro:
            celda = QTableWidgetItem(str(elemento))
            ui_table.tbl_perifericos.setItem(fila, columna, celda)
            columna += 1
        
        # Agregar botón BORRAR al Table Widget
        btn_borrar = QPushButton("BORRAR")
        # con partial se ejecutara borrar_el producto con el id indicado por registro[0]
        btn_borrar.clicked.connect(partial(borrar_producto, registro[0]))
        ui_table.tbl_perifericos.setCellWidget(fila, columna, btn_borrar)
        
        # Agregar botón EDITAR al Table Widget
        btn_edit = QPushButton("EDITAR")
        btn_edit.clicked.connect(partial(editar_item, registro[0]))
        ui_table.tbl_perifericos.setCellWidget(fila, columna + 1, btn_edit)
        
        fila += 1


def borrar_producto(id_borrar): 
    alerta = QMessageBox.question(MainWindow, "¡¡¡ ATENCIÓN !!!", "Vas a borrar el producto con ID: " + str(id_borrar))
    if alerta == QMessageBox.Yes:
       
        borrar_item(id_borrar)
        mostrar_table()   
    else:
        mostrar_table()


def editar_item(id_editar):
    QMessageBox.about(MainWindow, "AVISO", "Se va a editar el ID: " + str(id_editar))
    
    ui_editar.setupUi(MainWindow)

    item_a_editar = obtener_item_por_id(id_editar)

    index = ui_editar.cbx_tipo.findText(item_a_editar.tipo, QtCore.Qt.MatchFixedString)
    index2 = ui_editar.cbx_gama.findText(item_a_editar.gama, QtCore.Qt.MatchFixedString)

    ui_editar.cbx_tipo.setCurrentIndex(index)
    ui_editar.txt_marca.setText(item_a_editar.marca)
    ui_editar.txt_modelo.setText(item_a_editar.modelo)
    ui_editar.cbx_gama.setCurrentIndex(index2)
    ui_editar.txt_precio.setText(str(item_a_editar.precio))
    
    ui_editar.btn_editar.clicked.connect(partial(guardar_cambios_item, item_a_editar.id))


def guardar_cambios_item(id_guardar):
    QMessageBox.about(MainWindow, "Información", "Se han guardado los cambios sobre el registro con ID: " + str(id_guardar))
    
    guardar_new_item = Periferico()
    guardar_new_item.id = id_guardar
    guardar_new_item.tipo = ui_editar.cbx_tipo.currentText()
    guardar_new_item.marca = ui_editar.txt_marca.text()
    guardar_new_item.modelo = ui_editar.txt_modelo.text()
    guardar_new_item.gama = ui_editar.cbx_gama.currentText()
    guardar_new_item.precio = float(ui_editar.txt_precio.text().replace(",", "."))

    guardar_cambios_producto(guardar_new_item)
    
    mostrar_table()


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

ui_principal = VentanaTienda()
ui_registro = RegistroMain()
ui_listado1 = Listado1Main()
ui_listado2 = Listado2Main()
ui_table = TableWidget()
ui_editar = EditarRegistro()

ui_principal.setupUi(MainWindow)

ui_principal.submenu_registrar_periferico.triggered.connect(mostrar_registro)
ui_principal.submenu_listado_1.triggered.connect(mostrar_listado1)
ui_principal.submenu_listado_2.triggered.connect(mostrar_listado2)
ui_principal.submenu_listado_3.triggered.connect(mostrar_table)

# Stylesheet QSS from file:
file = QFile("style\style.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

MainWindow.show()
sys.exit(app.exec_())


