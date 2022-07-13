from PyQt5 import QtWidgets
from ui_home import Ui_Home
import c_home

class C_Home(QtWidgets.QMainWindow, Ui_Home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
