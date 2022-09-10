import sys
import rclpy
from PyQt5 import QtCore, QtGui, QtWidgets

try: 
    # For standalone running
    from camera_input import CameraI
    from initiator import Initiator
    from science_input import ScienceI
    from ui import Ui_MainWindow

except:
    # For ros run
    from .camera_input import CameraI
    from .initiator import Initiator
    from .science_input import ScienceI
    from .ui import Ui_MainWindow


class RoverGUI(CameraI, ScienceI, Initiator):
    
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        Initiator.__init__(self, self.ui)
        CameraI.__init__(self, self.ui)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    sys.exit(app.exec_())
    rclpy.shutdown()

if __name__ == '__main__':
    main()