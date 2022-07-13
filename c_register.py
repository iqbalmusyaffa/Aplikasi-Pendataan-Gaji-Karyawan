
from PyQt5 import QtWidgets
from ui_register import Ui_Register
import c_login

class C_Register(QtWidgets.QMainWindow, Ui_Register):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.tombolkembali.clicked.connect(self.Kembali_pressed)

    def Kembali_pressed(self):
        self.form = c_login.C_Login()
        self.form.show()
        self.close()

