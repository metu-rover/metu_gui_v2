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
        self.capture1 = cv2.VideoCapture(0)
        self.capture2 = cv2.VideoCapture(2)

        self.capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 671)
        self.capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 771)
        self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 671)
        self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 771)

        # Set up the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)

        # Initializing mixins
        Initiator.__init__(self, self.ui)
        CameraI.__init__(self, self.ui)
    
    def update_frame(self):
        # Read a new frame from the camera
        ret1, frame1 = self.capture1.read()
        ret2, frame2 = self.capture2.read()

        if ret1:
            # Convert the frame to a QImage
            rgb_image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            h1, w1, ch1 = rgb_image1.shape
            bytes_per_line = ch1 * w1
            q_image = QImage(rgb_image1.data, w1, h1, bytes_per_line, QImage.Format_RGB888)

            # Set the QImage as the pixmap for the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.ui.MainCamera.setPixmap(pixmap)

        if ret2:
            # Convert the frame to a QImage
            rgb_image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
            h2, w2, ch2 = rgb_image2.shape
            bytes_per_line = ch2 * w2
            q_image = QImage(rgb_image2.data, w2, h2, bytes_per_line, QImage.Format_RGB888)

            # Set the QImage as the pixmap for the QLabel
            pixmap = QPixmap.fromImage(q_image)
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