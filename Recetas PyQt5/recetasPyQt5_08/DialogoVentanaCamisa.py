# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoVentanaCamisa.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogoVentaCamisa(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 407)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.lbl_seleccion_talla_camisa = QtWidgets.QLabel(Dialog)
        self.lbl_seleccion_talla_camisa.setGeometry(QtCore.QRect(40, 20, 181, 20))
        self.lbl_seleccion_talla_camisa.setObjectName("lbl_seleccion_talla_camisa")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 160, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vly_talla_camisa = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vly_talla_camisa.setContentsMargins(0, 0, 0, 0)
        self.vly_talla_camisa.setObjectName("vly_talla_camisa")
        self.rbn_talla_xl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbn_talla_xl.setObjectName("rbn_talla_xl")
        self.vly_talla_camisa.addWidget(self.rbn_talla_xl)
        self.rbn_talla_l = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbn_talla_l.setObjectName("rbn_talla_l")
        self.vly_talla_camisa.addWidget(self.rbn_talla_l)
        self.rbn_talla_m = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbn_talla_m.setObjectName("rbn_talla_m")
        self.vly_talla_camisa.addWidget(self.rbn_talla_m)
        self.rbn_talla_s = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbn_talla_s.setObjectName("rbn_talla_s")
        self.vly_talla_camisa.addWidget(self.rbn_talla_s)
        self.lbl_seleccion_metodo_pago = QtWidgets.QLabel(Dialog)
        self.lbl_seleccion_metodo_pago.setGeometry(QtCore.QRect(40, 200, 211, 16))
        self.lbl_seleccion_metodo_pago.setObjectName("lbl_seleccion_metodo_pago")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 230, 180, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vly_metodo_pago = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vly_metodo_pago.setContentsMargins(0, 0, 0, 0)
        self.vly_metodo_pago.setObjectName("vly_metodo_pago")
        self.rbn_pago_tarjeta = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbn_pago_tarjeta.setObjectName("rbn_pago_tarjeta")
        self.vly_metodo_pago.addWidget(self.rbn_pago_tarjeta)
        self.rbn_contado = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbn_contado.setObjectName("rbn_contado")
        self.vly_metodo_pago.addWidget(self.rbn_contado)
        self.rbn_cheque_regalo = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbn_cheque_regalo.setObjectName("rbn_cheque_regalo")
        self.vly_metodo_pago.addWidget(self.rbn_cheque_regalo)
        self.lbl_selecciones = QtWidgets.QLabel(Dialog)
        self.lbl_selecciones.setGeometry(QtCore.QRect(20, 360, 360, 16))
        self.lbl_selecciones.setText("")
        self.lbl_selecciones.setObjectName("lbl_selecciones")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 180, 261, 20))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ventana selección "))
        self.lbl_seleccion_talla_camisa.setText(_translate("Dialog", "Escoja la talla de su camisa"))
        self.rbn_talla_xl.setText(_translate("Dialog", "XL"))
        self.rbn_talla_l.setText(_translate("Dialog", "L"))
        self.rbn_talla_m.setText(_translate("Dialog", "M"))
        self.rbn_talla_s.setText(_translate("Dialog", "S"))
        self.lbl_seleccion_metodo_pago.setText(_translate("Dialog", "Seleccione su método de pago"))
        self.rbn_pago_tarjeta.setText(_translate("Dialog", "Pago con tarjeta"))
        self.rbn_contado.setText(_translate("Dialog", "Pago al contado"))
        self.rbn_cheque_regalo.setText(_translate("Dialog", "Pago con cheque regalo"))
