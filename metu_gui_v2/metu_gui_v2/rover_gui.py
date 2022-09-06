import sys
import rclpy
from rclpy.node import Node
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

try: 

    from camera_input import CameraI
    from general_input import GeneralI, Worker
    from initiator import Initiator
    from science_input import ScienceI
    from ui import Ui_MainWindow

except:
    from .camera_input import CameraI
    from .general_input import GeneralI, Worker
    from .initiator import Initiator
    from .science_input import ScienceI
    from .ui import Ui_MainWindow


class RoverGUI(GeneralI, CameraI, ScienceI, Initiator):
    
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.runLongTask()
        #CameraI.__init__(self, self.ui)
        #ScienceI.__init__(self, self.ui)
        #Initiator.__init__(self, self.ui)


    def runLongTask(self):

        self.thread = QThread()
        self.worker = Worker(self.ui)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)

        self.thread.start()


    def reportProgress(self,num):
        print(num)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = RoverGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()