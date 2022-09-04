import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .camera_input import CameraI
from .general_input import GeneralI
from .initiator import Initiator
from .science_input import ScienceI
import rclpy
from rclpy.node import Node
from .ui import Ui_MainWindow


class RoverGUI(GeneralI, CameraI, ScienceI, Initiator):
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        CameraI.__init__(self, self.ui)
        ScienceI.__init__(self, self.ui)
        Initiator.__init__(self, self.ui)


        rclpy.init()

        minimal_subscriber = GeneralI(self.ui)

        rclpy.spin(minimal_subscriber)

        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        minimal_subscriber.destroy_node()
        rclpy.shutdown()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()