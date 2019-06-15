# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Frozn\Desktop\window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.OneBtm = QtWidgets.QPushButton(self.centralwidget)
        self.OneBtm.setObjectName("OneBtm")
        self.verticalLayout.addWidget(self.OneBtm)
        self.TwoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.TwoBtn.setObjectName("TwoBtn")
        self.verticalLayout.addWidget(self.TwoBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OneBtm.setText(_translate("MainWindow", "PushButton"))
        self.TwoBtn.setText(_translate("MainWindow", "PushButton"))

