from PyQt5 import QtWidgets
from ui_home import Ui_Home

class c_home(QtWidgets.QMainWindow, Ui_Home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)

        mess.exec_()
