# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/xml/ui_main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(657, 731)
        self.radar = Radar(MainScreen)
        self.radar.setGeometry(QtCore.QRect(70, 180, 500, 500))
        self.radar.setObjectName("radar")
        self.gridLayoutWidget = QtWidgets.QWidget(MainScreen)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 625, 158))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_vt_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_vt_4.setObjectName("lineEdit_vt_4")
        self.gridLayout.addWidget(self.lineEdit_vt_4, 3, 7, 1, 1)
        self.btn_create_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_create_4.setObjectName("btn_create_4")
        self.gridLayout.addWidget(self.btn_create_4, 3, 8, 1, 1)
        self.btn_create_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_create_2.setObjectName("btn_create_2")
        self.gridLayout.addWidget(self.btn_create_2, 1, 8, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 6, 1, 1)
        self.lineEdit_vt_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_vt_3.setObjectName("lineEdit_vt_3")
        self.gridLayout.addWidget(self.lineEdit_vt_3, 2, 7, 1, 1)
        self.btn_create_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_create_1.setObjectName("btn_create_1")
        self.gridLayout.addWidget(self.btn_create_1, 0, 8, 1, 1)
        self.btn_create_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_create_3.setObjectName("btn_create_3")
        self.gridLayout.addWidget(self.btn_create_3, 2, 8, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1)
        self.lineEdit_kc_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_kc_3.setObjectName("lineEdit_kc_3")
        self.gridLayout.addWidget(self.lineEdit_kc_3, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        self.lineEdit_kc_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_kc_2.setObjectName("lineEdit_kc_2")
        self.gridLayout.addWidget(self.lineEdit_kc_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_pv_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pv_4.setObjectName("lineEdit_pv_4")
        self.gridLayout.addWidget(self.lineEdit_pv_4, 3, 3, 1, 1)
        self.lineEdit_kc_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_kc_4.setObjectName("lineEdit_kc_4")
        self.gridLayout.addWidget(self.lineEdit_kc_4, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 6, 1, 1)
        self.lineEdit_hd_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hd_4.setObjectName("lineEdit_hd_4")
        self.gridLayout.addWidget(self.lineEdit_hd_4, 3, 5, 1, 1)
        self.lineEdit_hd_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hd_3.setObjectName("lineEdit_hd_3")
        self.gridLayout.addWidget(self.lineEdit_hd_3, 2, 5, 1, 1)
        self.lineEdit_vt_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_vt_1.setObjectName("lineEdit_vt_1")
        self.gridLayout.addWidget(self.lineEdit_vt_1, 0, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEdit_kc_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_kc_1.setObjectName("lineEdit_kc_1")
        self.gridLayout.addWidget(self.lineEdit_kc_1, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 4, 1, 1)
        self.lineEdit_pv_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pv_2.setObjectName("lineEdit_pv_2")
        self.gridLayout.addWidget(self.lineEdit_pv_2, 1, 3, 1, 1)
        self.lineEdit_vt_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_vt_2.setObjectName("lineEdit_vt_2")
        self.gridLayout.addWidget(self.lineEdit_vt_2, 1, 7, 1, 1)
        self.lineEdit_pv_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pv_1.setObjectName("lineEdit_pv_1")
        self.gridLayout.addWidget(self.lineEdit_pv_1, 0, 3, 1, 1)
        self.lineEdit_hd_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hd_1.setObjectName("lineEdit_hd_1")
        self.gridLayout.addWidget(self.lineEdit_hd_1, 0, 5, 1, 1)
        self.lineEdit_pv_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pv_3.setObjectName("lineEdit_pv_3")
        self.gridLayout.addWidget(self.lineEdit_pv_3, 2, 3, 1, 1)
        self.lineEdit_hd_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hd_2.setObjectName("lineEdit_hd_2")
        self.gridLayout.addWidget(self.lineEdit_hd_2, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(MainScreen)
        self.checkBox.setGeometry(QtCore.QRect(20, 700, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.v_multiple = QtWidgets.QSpinBox(MainScreen)
        self.v_multiple.setGeometry(QtCore.QRect(208, 699, 42, 22))
        self.v_multiple.setMinimum(1)
        self.v_multiple.setMaximum(100)
        self.v_multiple.setSingleStep(10)
        self.v_multiple.setProperty("value", 10)
        self.v_multiple.setObjectName("v_multiple")
        self.label = QtWidgets.QLabel(MainScreen)
        self.label.setGeometry(QtCore.QRect(100, 702, 111, 16))
        self.label.setObjectName("label")

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Form"))
        self.lineEdit_vt_4.setToolTip(_translate("MainScreen", "hải lý/giờ"))
        self.btn_create_4.setText(_translate("MainScreen", "Tạo mục tiêu"))
        self.btn_create_2.setText(_translate("MainScreen", "Tạo mục tiêu"))
        self.label_16.setText(_translate("MainScreen", "Vận tốc"))
        self.label_4.setText(_translate("MainScreen", "Vận tốc"))
        self.lineEdit_vt_3.setToolTip(_translate("MainScreen", "hải lý/giờ"))
        self.btn_create_1.setText(_translate("MainScreen", "Tạo mục tiêu"))
        self.btn_create_3.setText(_translate("MainScreen", "Tạo mục tiêu"))
        self.label_12.setText(_translate("MainScreen", "Hướng đi"))
        self.lineEdit_kc_3.setToolTip(_translate("MainScreen", "hải lý"))
        self.label_11.setText(_translate("MainScreen", "Phương vị"))
        self.lineEdit_kc_2.setToolTip(_translate("MainScreen", "hải lý"))
        self.label_7.setText(_translate("MainScreen", "Khoảng cách"))
        self.lineEdit_pv_4.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_kc_4.setToolTip(_translate("MainScreen", "hải lý"))
        self.label_15.setText(_translate("MainScreen", "Vận tốc"))
        self.lineEdit_hd_4.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_hd_3.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_vt_1.setToolTip(_translate("MainScreen", "hải lý/giờ"))
        self.label_10.setText(_translate("MainScreen", "Phương vị"))
        self.label_9.setText(_translate("MainScreen", "Phương vị"))
        self.label_3.setText(_translate("MainScreen", "Hướng đi"))
        self.label_2.setText(_translate("MainScreen", "Phương vị"))
        self.label_8.setText(_translate("MainScreen", "Khoảng cách"))
        self.lineEdit_kc_1.setToolTip(_translate("MainScreen", "hải lý"))
        self.label_14.setText(_translate("MainScreen", "Hướng đi"))
        self.label_6.setText(_translate("MainScreen", "Khoảng cách"))
        self.label_17.setText(_translate("MainScreen", "Vận tốc"))
        self.label_13.setText(_translate("MainScreen", "Hướng đi"))
        self.lineEdit_pv_2.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_vt_2.setToolTip(_translate("MainScreen", "hải lý/giờ"))
        self.lineEdit_pv_1.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_hd_1.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_pv_3.setToolTip(_translate("MainScreen", "độ"))
        self.lineEdit_hd_2.setToolTip(_translate("MainScreen", "độ"))
        self.label_5.setToolTip(_translate("MainScreen", "hải lý"))
        self.label_5.setText(_translate("MainScreen", "Khoảng cách"))
        self.checkBox.setText(_translate("MainScreen", "CFAR"))
        self.v_multiple.setPrefix(_translate("MainScreen", "x"))
        self.label.setText(_translate("MainScreen", "Vận tốc mô phỏng"))

from radar import Radar
