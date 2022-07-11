# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setStyleSheet("*{\n"
"background:#A7CECB; \n"
"}\n"
"\n"
"QFrame{ \n"
"background:#CACC90;\n"
"border-radius:10px;\n"
"}\n"
"QLineEdit{\n"
"background:#f2f2f2 50%;\n"
"border-radius:5px;\n"
"border:none;\n"
"font-size: 20px;\n"
"font-weight:bold;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton{\n"
"font-size:20px;\n"
"color:#fff;\n"
"border:none;\n"
"border-radius:5px;\n"
"background:#005b8f;\n"
"}\n"
"QPushButton:hover{\n"
"background:#B8B8B8;\n"
"}\n"
"QPushButton:pressed{\n"
"background:#585858;\n"
"}")
        self.menu1 = QtWidgets.QFrame(Form)
        self.menu1.setGeometry(QtCore.QRect(80, 80, 500, 340))
        self.menu1.setMinimumSize(QtCore.QSize(500, 340))
        self.menu1.setMaximumSize(QtCore.QSize(500, 340))
        self.menu1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu1.setObjectName("menu1")
        self.label = QtWidgets.QLabel(self.menu1)
        self.label.setGeometry(QtCore.QRect(170, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.menu1)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/user-min.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.menu1)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 41, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/password-min.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.menu1)
        self.lineEdit.setGeometry(QtCore.QRect(120, 130, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.menu1)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 210, 361, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.menu1)
        self.label_4.setGeometry(QtCore.QRect(140, 100, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.menu1)
        self.label_5.setGeometry(QtCore.QRect(120, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.menu1)
        self.label_6.setGeometry(QtCore.QRect(120, 180, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.tombol2 = QtWidgets.QPushButton(self.menu1)
        self.tombol2.setGeometry(QtCore.QRect(340, 270, 121, 41))
        self.tombol2.setStyleSheet("")
        self.tombol2.setObjectName("tombol2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "REGISTER"))
        self.label_5.setText(_translate("Form", "Username"))
        self.label_6.setText(_translate("Form", "Password"))
        self.tombol2.setText(_translate("Form", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
