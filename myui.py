# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(744, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_method = QtWidgets.QComboBox(self.centralwidget)
        self.btn_method.setGeometry(QtCore.QRect(570, 290, 131, 31))
        self.btn_method.setObjectName("btn_method")
        self.btn_method.addItem("")
        self.btn_method.addItem("")
        self.btn_method.addItem("")
        self.btn_method.addItem("")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(590, 330, 101, 31))
        self.btn_start.setObjectName("btn_start")
        self.finished_table = QtWidgets.QTableWidget(self.centralwidget)
        self.finished_table.setGeometry(QtCore.QRect(0, 390, 531, 331))
        self.finished_table.setRowCount(10)
        self.finished_table.setColumnCount(5)
        self.finished_table.setObjectName("finished_table")
        item = QtWidgets.QTableWidgetItem()
        self.finished_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.finished_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.finished_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.finished_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.finished_table.setHorizontalHeaderItem(4, item)
        self.running_table = QtWidgets.QTableWidget(self.centralwidget)
        self.running_table.setGeometry(QtCore.QRect(0, 30, 531, 331))
        self.running_table.setRowCount(10)
        self.running_table.setColumnCount(5)
        self.running_table.setObjectName("running_table")
        item = QtWidgets.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.running_table.setHorizontalHeaderItem(4, item)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 531, 192))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 360, 531, 192))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.raise_()
        self.textEdit.raise_()
        self.btn_method.raise_()
        self.btn_start.raise_()
        self.finished_table.raise_()
        self.running_table.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_method.setItemText(0, _translate("MainWindow", "时间片轮转"))
        self.btn_method.setItemText(1, _translate("MainWindow", "优先级"))
        self.btn_method.setItemText(2, _translate("MainWindow", "最短进程优先"))
        self.btn_method.setItemText(3, _translate("MainWindow", "最短剩余时间"))
        self.btn_start.setText(_translate("MainWindow", "开始调度"))
        item = self.finished_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.finished_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "进程状态"))
        item = self.finished_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "优先级"))
        item = self.finished_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "需要时间"))
        item = self.finished_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "剩余时间"))
        item = self.running_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.running_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "进程状态"))
        item = self.running_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "优先级"))
        item = self.running_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "需要时间"))
        item = self.running_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "剩余时间"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">running queue</p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">finished queue</p></body></html>"))

