# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listado_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Listado2Main(object):
    def setupUi(self, Listado2Main):
        Listado2Main.setObjectName("Listado2Main")
        Listado2Main.resize(690, 500)
        self.centralwidget = QtWidgets.QWidget(Listado2Main)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado1.setGeometry(QtCore.QRect(230, 20, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_listado1.setFont(font)
        self.lbl_listado1.setObjectName("lbl_listado1")
        self.lst_listado2 = QtWidgets.QListWidget(self.centralwidget)
        self.lst_listado2.setGeometry(QtCore.QRect(15, 80, 660, 360))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lst_listado2.setFont(font)
        self.lst_listado2.setFrameShape(QtWidgets.QFrame.Box)
        self.lst_listado2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lst_listado2.setLineWidth(3)
        self.lst_listado2.setMidLineWidth(1)
        #self.lst_listado2.setItemAlignment(QtCore.Qt.AlignLeading)
        self.lst_listado2.setObjectName("lst_listado2")
        Listado2Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Listado2Main)
        self.statusbar.setObjectName("statusbar")
        Listado2Main.setStatusBar(self.statusbar)

        self.retranslateUi(Listado2Main)
        QtCore.QMetaObject.connectSlotsByName(Listado2Main)

    def retranslateUi(self, Listado2Main):
        _translate = QtCore.QCoreApplication.translate
        Listado2Main.setWindowTitle(_translate("Listado2Main", "Listado List Widget"))
        self.lbl_listado1.setText(_translate("Listado2Main", "Listado List Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Listado2Main = QtWidgets.QMainWindow()
    ui = Listado2Main()
    ui.setupUi(Listado2Main)
    Listado2Main.show()
    sys.exit(app.exec_())
