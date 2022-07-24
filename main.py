import sys
from PyQt5.QtWidgets import QApplication
from c_login import C_Login


app = QApplication(sys.argv)
login = C_Login()
sys.exit(app.exec_())
