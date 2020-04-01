# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PuntoVentaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PuntoVentaDialog(object):
    def setupUi(self, PuntoVentaDialog):
        PuntoVentaDialog.setObjectName("PuntoVentaDialog")
        PuntoVentaDialog.resize(598, 196)
        self.lbl_producto_mouse = QtWidgets.QLabel(PuntoVentaDialog)
        self.lbl_producto_mouse.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.lbl_producto_mouse.setObjectName("lbl_producto_mouse")
        self.txt_valor_mouse = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_valor_mouse.setGeometry(QtCore.QRect(150, 20, 121, 20))
        self.txt_valor_mouse.setObjectName("txt_valor_mouse")
        self.sbx_cantidad_mouse = QtWidgets.QSpinBox(PuntoVentaDialog)
        self.sbx_cantidad_mouse.setGeometry(QtCore.QRect(300, 20, 71, 22))
        self.sbx_cantidad_mouse.setProperty("value", 0)
        self.sbx_cantidad_mouse.setObjectName("sbx_cantidad_mouse")
        self.txt_subtotal_mouse = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_subtotal_mouse.setGeometry(QtCore.QRect(400, 20, 141, 20))
        self.txt_subtotal_mouse.setObjectName("txt_subtotal_mouse")
        self.txt_valor_teclado = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_valor_teclado.setGeometry(QtCore.QRect(150, 70, 121, 20))
        self.txt_valor_teclado.setObjectName("txt_valor_teclado")
        self.txt_subtotal_teclado = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_subtotal_teclado.setGeometry(QtCore.QRect(400, 70, 141, 20))
        self.txt_subtotal_teclado.setObjectName("txt_subtotal_teclado")
        self.lbl_producto_teclado = QtWidgets.QLabel(PuntoVentaDialog)
        self.lbl_producto_teclado.setGeometry(QtCore.QRect(30, 70, 101, 16))
        self.lbl_producto_teclado.setObjectName("lbl_producto_teclado")
        self.sbx_cantidad_teclado = QtWidgets.QSpinBox(PuntoVentaDialog)
        self.sbx_cantidad_teclado.setGeometry(QtCore.QRect(300, 70, 71, 22))
        self.sbx_cantidad_teclado.setProperty("value", 0)
        self.sbx_cantidad_teclado.setObjectName("sbx_cantidad_teclado")
        self.lbl_gran_total = QtWidgets.QLabel(PuntoVentaDialog)
        self.lbl_gran_total.setGeometry(QtCore.QRect(370, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gran_total.setFont(font)
        self.lbl_gran_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_gran_total.setObjectName("lbl_gran_total")

        self.retranslateUi(PuntoVentaDialog)
        QtCore.QMetaObject.connectSlotsByName(PuntoVentaDialog)

    def retranslateUi(self, PuntoVentaDialog):
        _translate = QtCore.QCoreApplication.translate
        PuntoVentaDialog.setWindowTitle(_translate("PuntoVentaDialog", "Punto de Venta"))
        self.lbl_producto_mouse.setText(_translate("PuntoVentaDialog", "Valor Mouse HyperX"))
        self.txt_valor_mouse.setText(_translate("PuntoVentaDialog", ""))
        self.txt_subtotal_mouse.setText(_translate("PuntoVentaDialog", ""))
        self.txt_valor_teclado.setText(_translate("PuntoVentaDialog", ""))
        self.txt_subtotal_teclado.setText(_translate("PuntoVentaDialog", ""))
        self.lbl_producto_teclado.setText(_translate("PuntoVentaDialog", "Valor Teclado HyperX"))
        self.lbl_gran_total.setText(_translate("PuntoVentaDialog", ""))
