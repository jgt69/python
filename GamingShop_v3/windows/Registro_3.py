# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registro_3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class RegistroMain(object):
    def setupUi(self, RegistroMain):
        RegistroMain.setObjectName("RegistroMain")
        RegistroMain.resize(480, 520)
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
        self.lbl_tipo.setGeometry(QtCore.QRect(30, 100, 60, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tipo.setFont(font)
        self.lbl_tipo.setObjectName("lbl_tipo")
        self.lbl_marca = QtWidgets.QLabel(self.centralwidget)
        self.lbl_marca.setGeometry(QtCore.QRect(30, 150, 60, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_marca.setFont(font)
        self.lbl_marca.setObjectName("lbl_marca")
        self.lbl_modelo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_modelo.setGeometry(QtCore.QRect(30, 200, 80, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_modelo.setFont(font)
        self.lbl_modelo.setObjectName("lbl_modelo")
        self.lbl_gama = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gama.setGeometry(QtCore.QRect(30, 250, 60, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gama.setFont(font)
        self.lbl_gama.setObjectName("lbl_gama")
        self.lbl_precio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_precio.setGeometry(QtCore.QRect(30, 300, 60, 22))
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
        self.txt_precio.setGeometry(QtCore.QRect(140, 290, 240, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.txt_precio.setFont(font)
        self.txt_precio.setObjectName("txt_precio")
        self.cbx_gama = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_gama.setGeometry(QtCore.QRect(140, 240, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cbx_gama.setFont(font)
        self.cbx_gama.setObjectName("cbx_gama")
        self.cbx_gama.addItem("")
        self.cbx_gama.addItem("")
        self.cbx_gama.addItem("")
        self.btn_registrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registrar.setGeometry(QtCore.QRect(180, 390, 120, 40))
        self.btn_registrar.setObjectName("btn_registrar")
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
        self.cbx_tipo.setItemText(0, _translate("RegistroMain", "Accessory"))
        self.cbx_tipo.setItemText(1, _translate("RegistroMain", "Display"))
        self.cbx_tipo.setItemText(2, _translate("RegistroMain", "Gaming Chair"))
        self.cbx_tipo.setItemText(3, _translate("RegistroMain", "Headset"))
        self.cbx_tipo.setItemText(4, _translate("RegistroMain", "Keyboard"))
        self.cbx_tipo.setItemText(5, _translate("RegistroMain", "Mouse"))
        self.cbx_tipo.setItemText(6, _translate("RegistroMain", "Wireless Audio"))
        self.cbx_gama.setItemText(0, _translate("RegistroMain", "Basic"))
        self.cbx_gama.setItemText(1, _translate("RegistroMain", "Advance"))
        self.cbx_gama.setItemText(2, _translate("RegistroMain", "Elite"))
        self.btn_registrar.setToolTip(_translate("RegistroMain", "<html><head/><body><p><b>Pulsa para añadir nuevo producto a la BBDD</b></p></body></html>"))
        self.btn_registrar.setText(_translate("RegistroMain", "ENVIAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistroMain = QtWidgets.QMainWindow()
    ui = RegistroMain()
    ui.setupUi(RegistroMain)
    RegistroMain.show()
    sys.exit(app.exec_())
