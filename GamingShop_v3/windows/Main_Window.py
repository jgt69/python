# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class VentanaTienda(object):
    def setupUi(self, VentanaTienda):
        VentanaTienda.setObjectName("VentanaTienda")
        VentanaTienda.resize(621, 518)
        self.centralwidget = QtWidgets.QWidget(VentanaTienda)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_mi_tienda = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mi_tienda.setGeometry(QtCore.QRect(120, 0, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_mi_tienda.setFont(font)
        self.lbl_mi_tienda.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mi_tienda.setObjectName("lbl_mi_tienda")
        self.lbl_logo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(80, 90, 451, 371))
        self.lbl_logo.setText("")
        self.lbl_logo.setPixmap(QtGui.QPixmap("img/razer.png"))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setObjectName("lbl_logo")
        VentanaTienda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaTienda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuTienda = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.menuTienda.setFont(font)
        self.menuTienda.setObjectName("menuTienda")
        VentanaTienda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaTienda)
        self.statusbar.setObjectName("statusbar")
        VentanaTienda.setStatusBar(self.statusbar)
        self.submenu_registrar_periferico = QtWidgets.QAction(VentanaTienda)
        self.submenu_registrar_periferico.setObjectName("submenu_registrar_periferico")
        self.submenu_listado_1 = QtWidgets.QAction(VentanaTienda)
        self.submenu_listado_1.setObjectName("submenu_listado_1")
        self.submenu_listado_2 = QtWidgets.QAction(VentanaTienda)
        self.submenu_listado_2.setObjectName("submenu_listado_2")
        self.submenu_listado_3 = QtWidgets.QAction(VentanaTienda)
        self.submenu_listado_3.setObjectName("submenu_listado_3")
        self.menuTienda.addAction(self.submenu_registrar_periferico)
        self.menuTienda.addAction(self.submenu_listado_1)
        self.menuTienda.addAction(self.submenu_listado_2)
        self.menuTienda.addAction(self.submenu_listado_3)
        self.menubar.addAction(self.menuTienda.menuAction())

        self.retranslateUi(VentanaTienda)
        QtCore.QMetaObject.connectSlotsByName(VentanaTienda)

    def retranslateUi(self, VentanaTienda):
        _translate = QtCore.QCoreApplication.translate
        VentanaTienda.setWindowTitle(_translate("VentanaTienda", "GAMING SHOP"))
        self.lbl_mi_tienda.setText(_translate("VentanaTienda", "GAMING SHOP"))
        self.menuTienda.setTitle(_translate("VentanaTienda", "Productos"))
        self.submenu_registrar_periferico.setText(_translate("VentanaTienda", "Registrar producto"))
        self.submenu_listado_1.setText(_translate("VentanaTienda", "Listado Text Edit "))
        self.submenu_listado_2.setText(_translate("VentanaTienda", "Listado List Widget"))
        self.submenu_listado_3.setText(_translate("VentanaTienda", "Listado Table Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaTienda = QtWidgets.QMainWindow()
    ui = VentanaTienda()
    ui.setupUi(VentanaTienda)
    VentanaTienda.show()
    sys.exit(app.exec_())
