# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainLoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 630)
        MainWindow.setMinimumSize(QtCore.QSize(753, 630))
        MainWindow.setMaximumSize(QtCore.QSize(753, 630))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(307, 282, 211, 31))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:#365372;\n"
"border:none;\n"
"border-radius:0px;")
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, -10, 775, 630))
        self.widget.setMinimumSize(QtCore.QSize(775, 630))
        self.widget.setMaximumSize(QtCore.QSize(775, 630))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.278, x2:0.573, y2:0.784091, stop:0 rgba(1, 38, 78, 255), stop:1 rgba(171, 119, 143, 255));")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(350, 140, 121, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("background-color:none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/user (3).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(236, 190, 341, 241))
        self.label_2.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(296, 292, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("background-color:#01264E;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("src/user (3).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(296, 330, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setStyleSheet("background-color:#01264E;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("src/padlock.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(284, 442, 251, 41))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color:#c5bacc;\n"
"border-radius:10px;\n"
"color:#01264e;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.name_login)
        self.pushButton.clicked.connect(self.email_login)
        
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(299, 390, 101, 21))
        self.radioButton.setStyleSheet("background-color:#c5bacc;\n"
"border-radius:20px;\n"
"letter-spacing:1px;")
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(326, 330, 211, 31))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:#365372;\n"
"border:none;\n"
"border-radius:0px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(453, 390, 113, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:#c5bacc;\n"
"border:none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.widget.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", " User Email"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.radioButton.setText(_translate("MainWindow", "Remember Me"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", " Password"))
        self.lineEdit_3.setText(_translate("MainWindow", "Forget password"))
        

    def name_login(self):
            print(str(self.lineEdit.text()))
        #     print(self.name)
        
            
    def email_login(self):
            print(str(self.lineEdit_2.text()))
        #     print(self.email)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainLoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())