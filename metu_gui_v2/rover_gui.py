import sys
import rclpy
from PyQt5 import QtCore, QtGui, QtWidgets

"""
This file is the core file for the gui. It can even be named core.py (I will think about it).
It iniliaze gui call initiator class. 
"""

# ros2 run metu_gui_v2 listener execution needs import paths to be ".<something>" . At the final product only .* imports will be used.
# python3 slicer.py execution needs import paths to be normal. Normal imports are for testing.


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


class RoverGUI(CameraI, ScienceI, Initiator): # Mixins
    
    def __init__(self) -> None:

        # Gui is initialized and send to other classes.
        # ui.py is a seperate file because it changes a lot in the development process and file itself is quite large.
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

        # Initializing mixins
        Initiator.__init__(self, self.ui)
        CameraI.__init__(self, self.ui)


# Starting gui and the loop
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    sys.exit(app.exec_())
    rclpy.shutdown()

if __name__ == '__main__':
    main()