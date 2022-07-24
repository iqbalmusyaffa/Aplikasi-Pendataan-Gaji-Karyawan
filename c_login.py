from PyQt5 import QtWidgets
import pymysql
from ui_login import Ui_Login
from Menu import *
import c_register
import c_login
class C_Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.login.clicked.connect(self.login_clicked)
        self.register.clicked.connect(self.register_clicked)
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
    def login_clicked(self):
        usern = self.username.text()
        passw = self.password.text()
        conn=pymysql.connect(host="localhost",user="root",password="",db="gaji",port=3306,autocommit=True)
        cur=conn.cursor()
        query = "select * from login where username=%s and password=%s"
        data=cur.execute(query, (usern,passw))
        results = cur.fetchall()
        if results:
            self.messagebox("Berhasil", "Anda sudah Login")
            self.Dialog = QtWidgets.QDialog()
            self.close()
            self.berhasil()
        else:
            self.warning("Gagal","Masukan Username dan Password Dengan Benar..Jika Belum Register Silahkan Sign Up")
            self.Form = c_login.C_Login()
            self.Form.setupUi(self.Form)
            self.close()
    def register_clicked(self):
        self.Form = c_register.C_Register()
        self.Form.show()
        self.close()

    def berhasil(self):
        self.Form = Menu()
        self.Form.show()
