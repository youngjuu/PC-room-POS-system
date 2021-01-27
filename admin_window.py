# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import *

libpaths = QtWidgets.QApplication.libraryPaths() #추가
libpaths.append("C:\\Users\사용자\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyQt5\Qt\plugins")
QtWidgets.QApplication.setLibraryPaths(libpaths)

class Ui_adminWindow(object):
#-----------------------------------------------------------------------------
#파이썬 파일 연결
    def randomSeat(self):
        from random_seat_maker import create_random
        create_random()
    def initFile(self):
        from log_file_initiate import log_file_initiate
        log_file_initiate()
    def changeSeatAttribute(self):
        from changeSeat_Attribute import changeAttribute
        changeAttribute()
    def change_discountYn(self):
        from change_discountYn import change_discountYn,discount_tp
        change_discountYn()
        discount_tp()
        change_discountYn()
    def manage_sales(self):
        from manage_sales import manage_sales
        manage_sales()
#-----------------------------------------------------------------------------  
    def setupUi(self, adminWindow):
        adminWindow.setObjectName("adminWindow")
        adminWindow.resize(409, 600)
        self.centralwidget = QtWidgets.QWidget(adminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 170, 211, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 100, 211, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 240, 211, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        #self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_8.setGeometry(QtCore.QRect(90, 440, 211, 51))
        #self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(90, 380, 211, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        adminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 17))
        self.menubar.setObjectName("menubar")
        adminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminWindow)
        self.statusbar.setObjectName("statusbar")
        adminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminWindow)
        QtCore.QMetaObject.connectSlotsByName(adminWindow)
#-----------------------------------------------------------------------------
#이벤트 헨들러
        #self.pushButton_8.clicked.connect(self.randomSeat) #자리 랜덤화
        self.pushButton_12.clicked.connect(self.initFile) #결제로그 초기화
        self.pushButton_10.clicked.connect(self.changeSeatAttribute) #자리 속성 설정
        self.pushButton_9.clicked.connect(self.change_discountYn) #상품 할인 설정
        self.pushButton_11.clicked.connect(self.manage_sales) #매출 관리
#-----------------------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("adminWindow", "MainWindow"))
        self.pushButton_9.setText(_translate("adminWindow", "2. 상품 할인 설정"))
        self.pushButton_10.setText(_translate("adminWindow", "1. 자리 속성 설정"))
        self.pushButton_11.setText(_translate("adminWindow", "3. 매출 관리"))
        #self.pushButton_8.setText(_translate("adminWindow", "자리 랜덤화"))
        self.pushButton_12.setText(_translate("adminWindow", "결제로그 초기화"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminWindow = QtWidgets.QMainWindow()
    ui = Ui_adminWindow()
    ui.setupUi(adminWindow)
    adminWindow.show()
    sys.exit(app.exec_())

