from .app import Spotleafy
from PyQt5 import QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Spotleafy()
    gui.show()
    sys.exit(app.exec_())
