# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_saludo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ventanasaludo(object):
    def setupUi(self, Ventanasaludo):
        Ventanasaludo.setObjectName("Ventanasaludo")
        Ventanasaludo.resize(320, 163)
        self.lbl_escriba = QtWidgets.QLabel(Ventanasaludo)
        self.lbl_escriba.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.lbl_escriba.setObjectName("lbl_escriba")
        self.txt_nombre = QtWidgets.QLineEdit(Ventanasaludo)
        self.txt_nombre.setGeometry(QtCore.QRect(120, 30, 171, 20))
        self.txt_nombre.setObjectName("txt_nombre")
        self.lbl_saludo = QtWidgets.QLabel(Ventanasaludo)
        self.lbl_saludo.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.lbl_saludo.setObjectName("lbl_saludo")
        self.lbl_mensaje = QtWidgets.QLabel(Ventanasaludo)
        self.lbl_mensaje.setGeometry(QtCore.QRect(120, 70, 171, 20))
        self.lbl_mensaje.setText("")
        self.lbl_mensaje.setObjectName("lbl_mensaje")
        self.btn_saludar = QtWidgets.QPushButton(Ventanasaludo)
        self.btn_saludar.setGeometry(QtCore.QRect(160, 120, 111, 23))
        self.btn_saludar.setObjectName("btn_saludar")

        self.retranslateUi(Ventanasaludo)
        QtCore.QMetaObject.connectSlotsByName(Ventanasaludo)

    def retranslateUi(self, Ventanasaludo):
        _translate = QtCore.QCoreApplication.translate
        Ventanasaludo.setWindowTitle(_translate("Ventanasaludo", "Venta de saludo"))
        self.lbl_escriba.setText(_translate("Ventanasaludo", "Escriba su nombre:"))
        self.lbl_saludo.setText(_translate("Ventanasaludo", "Saludo"))
        self.btn_saludar.setText(_translate("Ventanasaludo", "SALUDAR"))
