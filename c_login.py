
from PyQt5 import QtWidgets
from ui_login import Ui_Login
from c_home import c_home

class C_Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.tombol1.clicked.connect(self.tombol1_clicked)
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)

        mess.exec_()
    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)

        mess.exec_()
    def tombol1_clicked(self):
        usern = self.username.text()
        passw = self.password.text()
        if ((usern == 'admin') and (passw == 'admin')):
            self.messagebox("Berhasil", "Anda sudah Login")
            self.Dialog = QtWidgets.QDialog()
            self.Form = c_home()
            self.Form.setupUi(self.Form)
            self.close()
        else:
            self.warning("Gagal","Masukan Username dan Password yang Benar")
