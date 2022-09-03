from ui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class RoverGUI:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    gui.MainWindow.show()
    sys.exit(app.exec_())