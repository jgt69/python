"""

Created on 13 abr. 2020

"""
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QFileDialog, QLabel
from PyQt5.Qt import QMessageBox, QPushButton, QTableWidgetItem
from PyQt5.QtCore import QFile, QTextStream

from GamingShop4.windows.Main_Window import VentanaTienda
from GamingShop4.windows.Registro_5 import RegistroMain
from GamingShop4.windows.Listado_1 import Listado1Main
from GamingShop4.windows.Listado_2 import Listado2Main
from GamingShop4.windows.Listado_con_imagen import TableWidget
from GamingShop4.windows.Editar_Registro_3 import EditarRegistro
from GamingShop4.windows.Detalles import Ui_Detalles

from GamingShop4.modelo.clases import Periferico
from GamingShop4.modelo.operaciones_bd import registro_periferico
from GamingShop4.modelo.operaciones_bd import obtener_listado
from GamingShop4.modelo.operaciones_bd import obtener_listado_noid
from GamingShop4.modelo.operaciones_bd import borrar_item
from GamingShop4.modelo.operaciones_bd import obtener_item_por_id
from GamingShop4.modelo.operaciones_bd import guardar_cambios_producto

from GamingShop4.validar.validaciones import validar_marca, validar_modelo, validar_precio

from functools import partial
from pathlib import Path
from os import remove

import sys
import shutil

productos = None


def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta = archivo[0]
    shutil.copy(ruta, 'temp/image.jpg')
    pixmap = QPixmap('temp/image.jpg')
    ui_registro.lbl_imagen.setPixmap(pixmap)


def cambiar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta = archivo[0]
    shutil.copy(ruta, 'temp/image.jpg')
    pixmap = QPixmap('temp/image.jpg')
    ui_editar.lbl_imagen.setPixmap(pixmap)


def mostrar_registro():
    ui_registro.setupUi(MainWindow)
    QMessageBox.about(MainWindow, "AVISO", "Es necesario completar todos los campos \nantes de pulsar sobre 'ENVIAR' ")
    ui_registro.btn_registrar.clicked.connect(registrar_periferico)
    ui_registro.btn_seleccionar_archivo.clicked.connect(seleccionar_imagen)
    ui_registro.btn_cancel.clicked.connect(mostrar_inicio)


def mostrar_inicio():
    ui_principal.setupUi(MainWindow)

    ui_principal.submenu_registrar_periferico.triggered.connect(mostrar_registro)
    ui_principal.submenu_listado_1.triggered.connect(mostrar_listado1)
    ui_principal.submenu_listado_2.triggered.connect(mostrar_listado2)
    ui_principal.submenu_listado_3.triggered.connect(mostrar_table)


def registrar_periferico():
    periferico = Periferico()

    periferico.tipo = ui_registro.cbx_tipo.currentText()

    # Validating QlineEdit marca / modelo
    periferico.marca = ui_registro.txt_marca.text()
    if not validar_marca(periferico.marca):
        QMessageBox.critical(MainWindow, "Error", "La marca introducida es incorrecta")
        return

    periferico.modelo = ui_registro.txt_modelo.text()
    if not validar_modelo(periferico.modelo):
        QMessageBox.critical(MainWindow, "Error", "El modelo introducido es incorrecto")
        return

    # RadioButtons
    if ui_registro.rbn_basic.isChecked():
        periferico.gama = "Basic"

    if ui_registro.rbn_advance.isChecked():
        periferico.gama = "Advance"

    if ui_registro.rbn_elite.isChecked():
        periferico.gama = "Elite"

    # Validating QLineEdit precio
    periferico.precio = ui_registro.txt_precio.text()
    if not validar_precio(periferico.precio):
        QMessageBox.critical(MainWindow, "Error", "La cantidad introducida no es válida")
        return
    else:
        periferico.precio = periferico.precio.replace(",", ".")

    #  Select image
    id_info = registro_periferico(periferico)
    ruta_destino = 'img_catalog/' + str(id_info) + '.jpg'
    shutil.move('temp/image.jpg', ruta_destino)

    # Checkbox
    if ui_registro.chk_premium.isChecked():
        periferico.soporte = True

    # Reset LineEdit
    ui_registro.txt_marca.setText("")
    ui_registro.txt_modelo.setText("")
    ui_registro.txt_precio.setText("")

    # Reset ComboBox
    index = ui_registro.cbx_tipo.findText("Accessory", QtCore.Qt.MatchFixedString)
    ui_registro.cbx_tipo.setCurrentIndex(index)

    # Uncheck RadioButtons
    if ui_registro.rbn_basic.isChecked():
        ui_registro.rbn_basic.setChecked(False)

    if ui_registro.rbn_advance.isChecked():
        ui_registro.rbn_advance.setChecked(False)

    if ui_registro.rbn_elite.isChecked():
        ui_registro.rbn_elite.setChecked(False)

    # Uncheck Checkbox
    ui_editar.chk_premium.setChecked(False)

    ui_registro.lbl_imagen.clear()

    QMessageBox.about(MainWindow, "Info", "Registro OK")


def mostrar_listado1():
    ui_listado1.setupUi(MainWindow)
    perifericos = obtener_listado_noid()
    texto = ""
    for p in perifericos:
        texto += " Tipo: " + p[0] + " | Marca: " + p[1] + " | Modelo: " + p[2] + " | Gama: " + p[
            3] + " | Precio: " + str(p[4]) + "€\n"
    ui_listado1.txt_listado1.setText(texto)


def mostrar_listado2():
    global productos
    ui_listado2.setupUi(MainWindow)
    productos = obtener_listado_noid()

    for p in productos:
        ui_listado2.lst_listado2.addItem(" Producto: " + p[0] + "  |  Marca: " + p[1] + "  |  Modelo: " + p[2])

    ui_listado2.lst_listado2.itemClicked.connect(ver_detalles_producto)


def ver_detalles_producto():
    indice_seleccionado = ui_listado2.lst_listado2.currentRow()
    producto = productos[indice_seleccionado]

    info = ""
    info += "Tipo de producto: " + str(producto[0]) + "\n"
    info += "Marca: " + str(producto[1]) + "\n"
    info += "Modelo: " + str(producto[2]) + "\n"
    info += "Gama: " + str(producto[3]) + "\n"
    info += "Precio: " + str(producto[4]) + "€"

    QMessageBox.about(MainWindow, "Info del Producto", info)


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

        #  Inserción de una imagen miniatura del producto
        lbl_minimg = QLabel()
        lbl_minimg.setScaledContents(True)
        ruta_imagen = 'img_catalog/' + str(registro[0]) + '.jpg'
        if Path(ruta_imagen).is_file():
            pixmap = QPixmap(ruta_imagen)
            lbl_minimg.setPixmap(pixmap)
            ui_table.tbl_perifericos.setCellWidget(fila, columna, lbl_minimg)

        # Agregar botón BORRAR al Table Widget
        btn_borrar = QPushButton("BORRAR")
        # con partial se ejecutara borrar_el producto con el id indicado por registro[0]
        btn_borrar.clicked.connect(partial(borrar_producto, registro[0]))
        ui_table.tbl_perifericos.setCellWidget(fila, columna + 1, btn_borrar)

        # Agregar botón EDITAR al Table Widget
        btn_edit = QPushButton("EDITAR")
        btn_edit.clicked.connect(partial(editar_item, registro[0]))
        ui_table.tbl_perifericos.setCellWidget(fila, columna + 2, btn_edit)

        # Agregar botón DETALLES al Table Widget
        btn_detail = QPushButton("DETALLES")
        btn_detail.clicked.connect(partial(detalles_item, registro[0]))
        ui_table.tbl_perifericos.setCellWidget(fila, columna + 3, btn_detail)

        fila += 1


def detalles_item(id_detalle):
    ui_detalles.setupUi(MainWindow)

    detalle = obtener_item_por_id(id_detalle)

    ui_detalles.lbl_marca.setText(detalle.marca)

    ui_detalles.lbl_tipo.setText(detalle.tipo)

    ui_detalles.lbl_modelo.setText(detalle.modelo)

    ui_detalles.lbl_precio.setText(str(detalle.precio).replace('.', ',') + "€")

    # Selección logo de la marca
    if detalle.marca == "Alienware":
        logo = QPixmap('logos/alienware.png')
        ui_detalles.lbl_logo_marca.setPixmap(logo)

    if detalle.marca == "Corsair":
        logo = QPixmap('logos/corsair.png')
        ui_detalles.lbl_logo_marca.setPixmap(logo)

    if detalle.marca == "Noblechairs":
        logo = QPixmap('logos/noblechairs.jpg')
        ui_detalles.lbl_logo_marca.setPixmap(logo)

    if detalle.marca == "Razer":
        logo = QPixmap('logos/razer.png')
        ui_detalles.lbl_logo_marca.setPixmap(logo)

    if detalle.marca == "Roccat":
        logo = QPixmap('logos/roccat.png')
        ui_detalles.lbl_logo_marca.setPixmap(logo)

    if detalle.marca == "ROG":
        logo = QPixmap('logos/ROG.png')
        ui_detalles.lbl_logo_marca.setPixmap(logo)

    pixmap = QPixmap('img_catalog/' + str(detalle.id) + '.jpg')
    ui_detalles.lbl_imagen.setPixmap(pixmap)

    ui_detalles.btn_volver.clicked.connect(mostrar_table)


def borrar_producto(id_borrar):
    alerta = QMessageBox.question(MainWindow, "¡¡¡ ATENCIÓN !!!", "Vas a borrar el producto con ID: " + str(id_borrar))
    if alerta == QMessageBox.Yes:
        borrar_item(id_borrar)
        remove('img_catalog/' + str(id_borrar) + '.jpg')
        mostrar_table()
    else:
        mostrar_table()


def editar_item(id_editar):
    QMessageBox.critical(MainWindow, "AVISO", "Se va a editar el ID: " + str(id_editar))

    ui_editar.setupUi(MainWindow)

    item_a_editar = obtener_item_por_id(id_editar)

    index = ui_editar.cbx_tipo.findText(item_a_editar.tipo, QtCore.Qt.MatchFixedString)

    # RadioButtons
    if item_a_editar.gama == 'Basic':
        ui_editar.rbn_basic.setChecked(True)

    if item_a_editar.gama == 'Advance':
        ui_editar.rbn_advance.setChecked(True)

    if item_a_editar.gama == 'Elite':
        ui_editar.rbn_elite.setChecked(True)

    ui_editar.cbx_tipo.setCurrentIndex(index)

    ui_editar.txt_marca.setText(item_a_editar.marca)
    ui_editar.txt_modelo.setText(item_a_editar.modelo)
    ui_editar.txt_precio.setText(str(item_a_editar.precio).replace('.', ','))

    # Checkbox
    if item_a_editar.soporte == 1:
        ui_editar.chk_premium.setChecked(True)

    # Recuperar imagen en la ventana editar
    pixmap = QPixmap('img_catalog/' + str(item_a_editar.id) + '.jpg')
    ui_editar.lbl_imagen.setPixmap(pixmap)

    ui_editar.btn_seleccionar_archivo.clicked.connect(cambiar_imagen)

    ui_editar.btn_cancel.clicked.connect(mostrar_table)

    ui_editar.btn_editar.clicked.connect(partial(guardar_cambios_item, item_a_editar.id))


def guardar_cambios_item(id_guardar):
    guardar_new_item = Periferico()
    guardar_new_item.id = id_guardar
    guardar_new_item.tipo = ui_editar.cbx_tipo.currentText()

    # Validación de los QLineEdit
    guardar_new_item.marca = ui_editar.txt_marca.text()
    if not validar_marca(guardar_new_item.marca):
        QMessageBox.critical(MainWindow, "Error", "La marca introducida es incorrecta")
        return

    guardar_new_item.modelo = ui_editar.txt_modelo.text()
    if not validar_modelo(guardar_new_item.modelo):
        QMessageBox.critical(MainWindow, "Error", "El modelo introducido es incorrecto")
        return

    guardar_new_item.precio = ui_editar.txt_precio.text().replace(",", ".")
    if not validar_precio(guardar_new_item.precio):
        QMessageBox.critical(MainWindow, "Error", "La cantidad introducida no es válida")
        return

    # RadioButtons
    if ui_editar.rbn_basic.isChecked():
        guardar_new_item.gama = "Basic"

    if ui_editar.rbn_advance.isChecked():
        guardar_new_item.gama = "Advance"

    if ui_editar.rbn_elite.isChecked():
        guardar_new_item.gama = "Elite"

    # Checkbox
    if ui_editar.chk_premium.isChecked():
        guardar_new_item.soporte = True

    #  Selección de la imagen, si no ha cambiado se mantiene la existente
    temporal = 'temp/image.jpg'
    if Path(temporal).is_file():
        ruta_destino = 'img_catalog/' + str(id_guardar) + '.jpg'
        shutil.move('temp/image.jpg', ruta_destino)

    guardar_cambios_producto(guardar_new_item)

    QMessageBox.about(MainWindow, "Información", "Se guardaron los cambios en el registro con ID: " + str(id_guardar))

    mostrar_table()


# Ventana principal e instanciación de las ventanas secundarias
app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

ui_principal = VentanaTienda()
ui_registro = RegistroMain()
ui_listado1 = Listado1Main()
ui_listado2 = Listado2Main()
ui_table = TableWidget()
ui_editar = EditarRegistro()
ui_detalles = Ui_Detalles()

mostrar_inicio()

# Stylesheet QSS from file:
file = QFile("style/style5.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

MainWindow.show()
sys.exit(app.exec_())
