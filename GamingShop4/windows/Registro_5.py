# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro_5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class RegistroMain(object):
    def setupUi(self, RegistroMain):
        RegistroMain.setObjectName("RegistroMain")
        RegistroMain.resize(480, 750)
        RegistroMain.move(500, 50)
        RegistroMain.setWindowIcon(QIcon('./icon/anonymous.png'))
        self.centralwidget = QtWidgets.QWidget(RegistroMain)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo_registro = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo_registro.setGeometry(QtCore.QRect(90, 10, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo_registro.setFont(font)
        self.lbl_titulo_registro.setObjectName("lbl_titulo_registro")
        self.lbl_tipo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tipo.setGeometry(QtCore.QRect(30, 90, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tipo.setFont(font)
        self.lbl_tipo.setObjectName("lbl_tipo")
        self.lbl_marca = QtWidgets.QLabel(self.centralwidget)
        self.lbl_marca.setGeometry(QtCore.QRect(30, 140, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_marca.setFont(font)
        self.lbl_marca.setObjectName("lbl_marca")
        self.lbl_modelo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_modelo.setGeometry(QtCore.QRect(30, 190, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_modelo.setFont(font)
        self.lbl_modelo.setObjectName("lbl_modelo")
        self.lbl_gama = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gama.setGeometry(QtCore.QRect(30, 250, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gama.setFont(font)
        self.lbl_gama.setObjectName("lbl_gama")
        self.lbl_precio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_precio.setGeometry(QtCore.QRect(30, 365, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setObjectName("lbl_precio")
        self.cbx_tipo = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_tipo.setGeometry(QtCore.QRect(140, 90, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cbx_tipo.setFont(font)
        self.cbx_tipo.setObjectName("cbx_tipo")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.txt_marca = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_marca.setGeometry(QtCore.QRect(140, 140, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.txt_marca.setFont(font)
        self.txt_marca.setObjectName("txt_marca")
        self.txt_modelo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_modelo.setGeometry(QtCore.QRect(140, 190, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.txt_modelo.setFont(font)
        self.txt_modelo.setObjectName("txt_modelo")
        self.txt_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_precio.setGeometry(QtCore.QRect(140, 360, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.txt_precio.setFont(font)
        self.txt_precio.setObjectName("txt_precio")
        self.btn_registrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registrar.setGeometry(QtCore.QRect(60, 660, 120, 40))
        self.btn_registrar.setObjectName("btn_registrar")
        self.lbl_texto_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_texto_imagen.setGeometry(QtCore.QRect(30, 420, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_texto_imagen.setFont(font)
        self.lbl_texto_imagen.setObjectName("lbl_texto_imagen")
        self.lbl_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen.setGeometry(QtCore.QRect(140, 430, 241, 151))
        self.lbl_imagen.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_imagen.setLineWidth(2)
        self.lbl_imagen.setText("")
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.btn_seleccionar_archivo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_seleccionar_archivo.setGeometry(QtCore.QRect(20, 450, 115, 30))
        self.btn_seleccionar_archivo.setObjectName("btn_seleccionar_archivo")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(270, 660, 120, 40))
        self.btn_cancel.setObjectName("btn_cancel")
        self.rbn_basic = QtWidgets.QRadioButton(self.centralwidget)
        self.rbn_basic.setGeometry(QtCore.QRect(150, 250, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbn_basic.setFont(font)
        self.rbn_basic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbn_basic.setObjectName("rbn_basic")
        self.rbn_advance = QtWidgets.QRadioButton(self.centralwidget)
        self.rbn_advance.setGeometry(QtCore.QRect(150, 280, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbn_advance.setFont(font)
        self.rbn_advance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbn_advance.setObjectName("rbn_advance")
        self.rbn_elite = QtWidgets.QRadioButton(self.centralwidget)
        self.rbn_elite.setGeometry(QtCore.QRect(150, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbn_elite.setFont(font)
        self.rbn_elite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rbn_elite.setObjectName("rbn_elite")
        self.lbl_premium = QtWidgets.QLabel(self.centralwidget)
        self.lbl_premium.setGeometry(QtCore.QRect(30, 600, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_premium.setFont(font)
        self.lbl_premium.setObjectName("lbl_premium")
        self.chk_premium = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_premium.setGeometry(QtCore.QRect(210, 605, 31, 17))
        self.chk_premium.setText("")
        self.chk_premium.setObjectName("chk_premium")
        RegistroMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegistroMain)
        self.statusbar.setObjectName("statusbar")
        RegistroMain.setStatusBar(self.statusbar)

        self.retranslateUi(RegistroMain)
        QtCore.QMetaObject.connectSlotsByName(RegistroMain)

    def retranslateUi(self, RegistroMain):
        _translate = QtCore.QCoreApplication.translate
        RegistroMain.setWindowTitle(_translate("RegistroMain", "Registro de producto"))
        self.lbl_titulo_registro.setText(_translate("RegistroMain", "Registro de producto"))
        self.lbl_tipo.setText(_translate("RegistroMain", "Tipo"))
        self.lbl_marca.setText(_translate("RegistroMain", "Marca"))
        self.lbl_modelo.setText(_translate("RegistroMain", "Modelo"))
        self.lbl_gama.setText(_translate("RegistroMain", "Gama"))
        self.lbl_precio.setText(_translate("RegistroMain", "Precio"))
        self.cbx_tipo.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Selecciona el tipo de producto</b></p></body></html>"))
        self.cbx_tipo.setItemText(0, _translate("RegistroMain", "Accessory"))
        self.cbx_tipo.setItemText(1, _translate("RegistroMain", "Display"))
        self.cbx_tipo.setItemText(2, _translate("RegistroMain", "Gaming Chair"))
        self.cbx_tipo.setItemText(3, _translate("RegistroMain", "Headset"))
        self.cbx_tipo.setItemText(4, _translate("RegistroMain", "Keyboard"))
        self.cbx_tipo.setItemText(5, _translate("RegistroMain", "Mouse"))
        self.cbx_tipo.setItemText(6, _translate("RegistroMain", "Wireless Audio"))
        self.txt_marca.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Introduce la marca</b></p></body></html>"))
        self.txt_modelo.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Introduce el modelo</b></p></body></html>"))
        self.txt_precio.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Introduce el precio en €</b></p></body></html>"))
        self.btn_registrar.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Pulsa para añadir nuevo producto a la BBDD</b></p></body></html>"))
        self.btn_registrar.setText(_translate("RegistroMain", "ENVIAR"))
        self.lbl_texto_imagen.setText(_translate("RegistroMain", "Imagen"))
        self.lbl_imagen.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Vista prevía de la imagen</b></p></body></html>"))
        self.btn_seleccionar_archivo.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Selecciona una imagen del producto</b></p></body></html>"))
        self.btn_seleccionar_archivo.setText(_translate("RegistroMain", "Seleccionar archivo"))
        self.btn_cancel.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Pulsa para cerrar la ventana</b></p></body></html>"))
        self.btn_cancel.setText(_translate("RegistroMain", "CANCELAR"))
        self.rbn_basic.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Gama básica, económica o outlet</b></p></body></html>"))
        self.rbn_basic.setText(_translate("RegistroMain", "Basic"))
        self.rbn_advance.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Gama altas prestaciones</b></p></body></html>"))
        self.rbn_advance.setText(_translate("RegistroMain", "Advance"))
        self.rbn_elite.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Gama para gamers profesionales</b></p></body></html>"))
        self.rbn_elite.setText(_translate("RegistroMain", "Elite"))
        self.lbl_premium.setText(_translate("RegistroMain", "Premium support"))
        self.chk_premium.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Soporte personalizado con coste extra</b></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistroMain = QtWidgets.QMainWindow()
    ui = RegistroMain()
    ui.setupUi(RegistroMain)
    RegistroMain.show()
    sys.exit(app.exec_())