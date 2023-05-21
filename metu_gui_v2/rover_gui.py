import sys
import rclpy
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton

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

        # Set up the video capture
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 671)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 771)

        # Set up the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)

        # Initializing mixins
        Initiator.__init__(self, self.ui)
        CameraI.__init__(self, self.ui)
    
    def update_frame(self):
        # Read a new frame from the camera
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to a QImage
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Set the QImage as the pixmap for the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.ui.MainCamera.setPixmap(pixmap)
            self.ui.EndEffectorCamera.setPixmap(pixmap)
            self.ui.ScienceHubCamera.setPixmap(pixmap)

# Starting gui and the loop
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    sys.exit(app.exec_())
    rclpy.shutdown()

if __name__ == '__main__':
    main()