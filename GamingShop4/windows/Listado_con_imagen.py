# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listado_3_btn.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class TableWidget(object):
    def setupUi(self, TableWidget):
        TableWidget.setObjectName("TableWidget")
        TableWidget.resize(1200, 800)
        TableWidget.move(100, 50)
        TableWidget.setWindowIcon(QIcon('./icon/anonymous.png'))
        self.centralwidget = QtWidgets.QWidget(TableWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado3.setGeometry(QtCore.QRect(60, 20, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_listado3.setFont(font)
        self.lbl_listado3.setObjectName("lbl_listado3")
        self.tbl_perifericos = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_perifericos.setGeometry(QtCore.QRect(40, 80, 1120, 640))
        self.tbl_perifericos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tbl_perifericos.setObjectName("tbl_perifericos")
        self.tbl_perifericos.setColumnCount(10)
        self.tbl_perifericos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbl_perifericos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_perifericos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_perifericos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_perifericos.setHorizontalHeaderItem(9, item)
        self.tbl_perifericos.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_perifericos.horizontalHeader().setMinimumSectionSize(30)
        self.tbl_perifericos.horizontalHeader().setStretchLastSection(True)
        self.tbl_perifericos.verticalHeader().setDefaultSectionSize(80)
        self.tbl_perifericos.verticalHeader().setMinimumSectionSize(20)
        header = self.tbl_perifericos.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        TableWidget.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TableWidget)
        self.statusbar.setObjectName("statusbar")
        TableWidget.setStatusBar(self.statusbar)

        self.retranslateUi(TableWidget)
        QtCore.QMetaObject.connectSlotsByName(TableWidget)

    def retranslateUi(self, TableWidget):
        _translate = QtCore.QCoreApplication.translate
        TableWidget.setWindowTitle(_translate("TableWidget", "Product View"))
        self.lbl_listado3.setText(_translate("TableWidget", "PRODUCT VIEW"))
        item = self.tbl_perifericos.horizontalHeaderItem(0)
        item.setText(_translate("TableWidget", "ID"))
        item = self.tbl_perifericos.horizontalHeaderItem(1)
        item.setText(_translate("TableWidget", "Tipo"))
        item = self.tbl_perifericos.horizontalHeaderItem(2)
        item.setText(_translate("TableWidget", "Marca"))
        item = self.tbl_perifericos.horizontalHeaderItem(3)
        item.setText(_translate("TableWidget", "Modelo"))
        item = self.tbl_perifericos.horizontalHeaderItem(4)
        item.setText(_translate("TableWidget", "Gama"))
        item = self.tbl_perifericos.horizontalHeaderItem(5)
        item.setText(_translate("TableWidget", "Precio"))
        item = self.tbl_perifericos.horizontalHeaderItem(6)
        item.setText(_translate("TableWidget", "Imagen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TableWidget = QtWidgets.QMainWindow()
    ui = TableWidget()
    ui.setupUi(TableWidget)
    TableWidget.show()
    sys.exit(app.exec_())
