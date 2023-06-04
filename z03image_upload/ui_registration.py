# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "tree.jpg"   # icon图标的图片
                                    ), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 按钮
        # "上传红外图像"
        self.mix_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.mix_pushButton.setGeometry(QtCore.QRect(90, 610, 171, 51))
        self.mix_pushButton.setObjectName("infr_pushButton")

        # "上传可见光图像"
        self.flu_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.flu_pushButton.setGeometry(QtCore.QRect(70, 270, 171, 41))
        self.flu_pushButton.setObjectName("visible_pushButton")
        # "CNN"
        self.CNN_registration = QtWidgets.QPushButton(self.centralwidget)
        self.CNN_registration.setGeometry(QtCore.QRect(590, 450, 141, 31))
        self.CNN_registration.setObjectName("CNN_registration")


        self.infr_view = QtWidgets.QLabel(self.centralwidget)
        self.infr_view.setGeometry(QtCore.QRect(50, 350, 240, 240))
        # (横坐标, 纵坐标, 宽度, 181)
        self.infr_view.setAutoFillBackground(False)
        self.infr_view.setStyleSheet(
            "*{background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(214,249,255,100) , stop:1 rgba(158,232,250,100)); border: 2px solid rgba(205,92,92,255); border-radius:20px;}")
        self.infr_view.setText("")
        self.infr_view.setObjectName("infr_view")
        self.vis_view = QtWidgets.QLabel(self.centralwidget)
        self.vis_view.setGeometry(QtCore.QRect(50, 10, 240, 240))
        self.vis_view.setStyleSheet(
            "*{background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(214,249,255,100) , stop:1 rgba(158,232,250,100)); border: 2px solid rgba(205,92,92,255); border-radius:20px;}")
        self.vis_view.setText("")
        self.vis_view.setObjectName("vis_view")



        self.CNN_result = QtWidgets.QLabel(self.centralwidget)
        self.CNN_result.setGeometry(QtCore.QRect(440, 250, 441, 191))
        self.CNN_result.setStyleSheet(
            "*{background: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(214,249,255,100) , stop:1 rgba(158,232,250,100)); border: 2px solid rgba(205,92,92,255); border-radius:20px;}")
        self.CNN_result.setText("")
        self.CNN_result.setObjectName("CNN_result")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "registration"))
        self.mix_pushButton.setText(_translate("MainWindow", "上传mix图像"))

        self.flu_pushButton.setText(_translate("MainWindow", "上传flu图像"))
        self.CNN_registration.setText(_translate("MainWindow", "CNN"))