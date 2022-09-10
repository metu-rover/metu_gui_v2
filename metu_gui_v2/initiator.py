from PyQt5.QtCore import QThread
import rclpy

# Same reason with the rover_gui.py file
try: 
    # For standalone running
    from camera_input import CameraI
    from general_input import GeneralI
    from science_input import ScienceI
    from ros_reciever_thread import RecieverWorker

except:
    # For ros run
    from .camera_input import CameraI
    from .general_input import GeneralI
    from .science_input import ScienceI
    from .ros_reciever_thread import RecieverWorker


"""
This class is for initating the ros subscribtion nodes and a QThread.
"""

class Initiator:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.ros_initiate()

    # Initialing ros nodes
    def ros_initiate(self):
        rclpy.init()
        self.general_subscriber = ScienceI(self.ui)
        self.science_subscriber = GeneralI(self.ui)
        self.ros_reciever_thread_initiate()

    # Initializing QThread
    def ros_reciever_thread_initiate(self):

        self.general_thread = QThread()
        self.general_worker = RecieverWorker(self.general_subscriber, self.science_subscriber)
        self.general_worker.moveToThread(self.general_thread)

        self.general_thread.started.connect(self.general_worker.run)
        self.general_worker.finished.connect(self.general_thread.quit)
        self.general_worker.finished.connect(self.general_worker.deleteLater)
        self.general_thread.finished.connect(self.general_thread.deleteLater)
        self.general_thread.start()

