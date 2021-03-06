# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.viewer = ImageViewer(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewer.sizePolicy().hasHeightForWidth())
        self.viewer.setSizePolicy(sizePolicy)
        self.viewer.setObjectName("viewer")
        self.verticalLayout.addWidget(self.viewer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.resetPointsButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetPointsButton.setObjectName("resetPointsButton")
        self.horizontalLayout.addWidget(self.resetPointsButton)
        self.applyTransform = QtWidgets.QPushButton(self.centralwidget)
        self.applyTransform.setObjectName("applyTransform")
        self.horizontalLayout.addWidget(self.applyTransform)
        self.resetTransformButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetTransformButton.setObjectName("resetTransformButton")
        self.horizontalLayout.addWidget(self.resetTransformButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.menu.addAction(self.openAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????????????? ???????????????????????????? ??????????????????????"))
        self.label.setText(_translate("MainWindow", "???????????????? 4 ??????????"))
        self.resetPointsButton.setText(_translate("MainWindow", "?????????? ??????????"))
        self.applyTransform.setText(_translate("MainWindow", "?????????????????? ????????????????????????"))
        self.resetTransformButton.setText(_translate("MainWindow", "???????????????? ??????????????????????????"))
        self.saveButton.setText(_translate("MainWindow", "?????????????????? ??????????????????"))
        self.menu.setTitle(_translate("MainWindow", "????????"))
        self.openAction.setText(_translate("MainWindow", "??????????????"))
from ImageViewer import ImageViewer
