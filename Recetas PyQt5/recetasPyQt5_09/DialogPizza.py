# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogPizza.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PizzaDialog(object):
    def setupUi(self, PizzaDialog):
        PizzaDialog.setObjectName("PizzaDialog")
        PizzaDialog.resize(377, 242)
        self.lbl_precio_pizza = QtWidgets.QLabel(PizzaDialog)
        self.lbl_precio_pizza.setGeometry(QtCore.QRect(20, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio_pizza.setFont(font)
        self.lbl_precio_pizza.setObjectName("lbl_precio_pizza")
        self.lbl_seleccione_extras = QtWidgets.QLabel(PizzaDialog)
        self.lbl_seleccione_extras.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.lbl_seleccione_extras.setObjectName("lbl_seleccione_extras")
        self.chk_queso = QtWidgets.QCheckBox(PizzaDialog)
        self.chk_queso.setGeometry(QtCore.QRect(30, 70, 70, 17))
        self.chk_queso.setObjectName("chk_queso")
        self.chk_aceitunas = QtWidgets.QCheckBox(PizzaDialog)
        self.chk_aceitunas.setGeometry(QtCore.QRect(30, 100, 70, 17))
        self.chk_aceitunas.setObjectName("chk_aceitunas")
        self.chk_salsas = QtWidgets.QCheckBox(PizzaDialog)
        self.chk_salsas.setGeometry(QtCore.QRect(30, 130, 70, 17))
        self.chk_salsas.setObjectName("chk_salsas")
        self.precio_final = QtWidgets.QLabel(PizzaDialog)
        self.precio_final.setGeometry(QtCore.QRect(30, 180, 321, 16))
        self.precio_final.setText("")
        self.precio_final.setObjectName("precio_final")

        self.retranslateUi(PizzaDialog)
        QtCore.QMetaObject.connectSlotsByName(PizzaDialog)

    def retranslateUi(self, PizzaDialog):
        _translate = QtCore.QCoreApplication.translate
        PizzaDialog.setWindowTitle(_translate("PizzaDialog", "Pizza"))
        self.lbl_precio_pizza.setText(_translate("PizzaDialog", "Precio Pizza 15€"))
        self.lbl_seleccione_extras.setText(_translate("PizzaDialog", "Seleccione extras:"))
        self.chk_queso.setText(_translate("PizzaDialog", "Queso"))
        self.chk_aceitunas.setText(_translate("PizzaDialog", "Aceitunas"))
        self.chk_salsas.setText(_translate("PizzaDialog", "Salsas"))
