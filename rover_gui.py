from ui import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from camera_input import CameraI
from general_input import GeneralI
from initiator import Initiator
from science_input import ScienceI


class RoverGUI(GeneralI, CameraI, ScienceI, Initiator):
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        GeneralI.__init__(self, self.ui)
        CameraI.__init__(self, self.ui)
        ScienceI.__init__(self, self.ui)
        Initiator.__init__(self, self.ui)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    gui.MainWindow.show()
    sys.exit(app.exec_())