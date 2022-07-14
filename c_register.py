from PyQt5 import QtWidgets
import pymysql
from ui_register import Ui_Register
import c_login
import c_register

class C_Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.tombolkembali.clicked.connect(self.Kembali_pressed)
        self.tombolregister.clicked.connect(self.Register_clicked)

    def Kembali_pressed(self):
        self.form = c_login.C_Login()
        self.form.show()
        self.close()

    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def warning(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def Register_clicked(self):
        usern = self.username.text()
        passw = self.password.text()
        confirm = self.confirmpassword.text()
        conn = pymysql.connect(host="localhost", user="root",password="", db="gaji", port=3306, autocommit=True)
        cur = conn.cursor()
        cur.execute("select * from login where username='"+ usern +"' and password='"+ passw +"'")
        if (len(cur.fetchone()) > 0):
            self.warning("Gagal", "Username dan Password sudah dibuat")
            self.Form = c_register.C_Register()
            self.Form.setupUi(self.Form)
            self.close()
        else:
            cur.execute("insert into login values('"+ usern +"','"+ passw +"','"+ confirm +"')")
            conn.commit()
            self.messagebox("Berhasil", "Username dan Password berhasil dibuat")
            self.Dialog = QtWidgets.QDialog()
            self.Form = c_login.C_Login()
            self.Form.setupUi(self.Form)
            self.close()

