# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoClaseVuelo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogoClaseVuelo(object):
    def setupUi(self, DialogoClaseVuelo):
        DialogoClaseVuelo.setObjectName("DialogoClaseVuelo")
        DialogoClaseVuelo.resize(320, 230)
        self.lbl_escoja_clase_vuelo = QtWidgets.QLabel(DialogoClaseVuelo)
        self.lbl_escoja_clase_vuelo.setGeometry(QtCore.QRect(20, 3, 151, 20))
        self.lbl_escoja_clase_vuelo.setObjectName("lbl_escoja_clase_vuelo")
        self.rbn_primera_clase = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbn_primera_clase.setGeometry(QtCore.QRect(20, 40, 131, 17))
        self.rbn_primera_clase.setObjectName("rbn_primera_clase")
        self.rbn_clase_negocio = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbn_clase_negocio.setGeometry(QtCore.QRect(20, 80, 131, 17))
        self.rbn_clase_negocio.setObjectName("rbn_clase_negocio")
        self.rbn_clase_economica = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbn_clase_economica.setGeometry(QtCore.QRect(20, 120, 131, 17))
        self.rbn_clase_economica.setObjectName("rbn_clase_economica")
        self.lbl_resultado_seleccion = QtWidgets.QLabel(DialogoClaseVuelo)
        self.lbl_resultado_seleccion.setGeometry(QtCore.QRect(30, 160, 221, 16))
        self.lbl_resultado_seleccion.setText("")
        self.lbl_resultado_seleccion.setObjectName("lbl_resultado_seleccion")

        self.retranslateUi(DialogoClaseVuelo)
        QtCore.QMetaObject.connectSlotsByName(DialogoClaseVuelo)

    def retranslateUi(self, DialogoClaseVuelo):
        _translate = QtCore.QCoreApplication.translate
        DialogoClaseVuelo.setWindowTitle(_translate("DialogoClaseVuelo", "Clase de vuelo"))
        self.lbl_escoja_clase_vuelo.setText(_translate("DialogoClaseVuelo", "Escoja la clase de vuelo"))
        self.rbn_primera_clase.setText(_translate("DialogoClaseVuelo", "Primera clase:"))
        self.rbn_clase_negocio.setText(_translate("DialogoClaseVuelo", "Clase Business:"))
        self.rbn_clase_economica.setText(_translate("DialogoClaseVuelo", "Clase económica:"))
