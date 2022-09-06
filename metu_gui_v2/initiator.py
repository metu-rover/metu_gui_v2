from PyQt5.QtCore import QThread
import rclpy

try: 
    # For standalone running
    from camera_input import CameraI
    from general_input import GeneralWorker, GeneralI
    from science_input import ScienceWorker, ScienceI

except:
    # For ros run
    from .camera_input import CameraI
    from .general_input import GeneralWorker, GeneralI
    from .science_input import ScienceWorker, ScienceI


class Initiator:
    def __init__(self, ui) -> None:
        self.ui = ui

    def ros_initiate(self):
        rclpy.init()
        self.general_subscriber = ScienceI(self.ui)
        self.science_subscriber = GeneralI(self.ui)

        # ? So many things happen between rosnode create and ros spin. This might be bad practise.
        self.general_thread_initiate()
        self.science_thread_initiate()

    def general_thread_initiate(self):

        self.general_thread = QThread()
        self.general_worker = GeneralWorker(self.general_subscriber)
        self.general_worker.moveToThread(self.general_thread)

        self.general_thread.started.connect(self.general_worker.run)
        self.general_worker.finished.connect(self.general_thread.quit)
        self.general_worker.finished.connect(self.general_worker.deleteLater)
        self.general_thread.finished.connect(self.general_thread.deleteLater)
        self.general_thread.start()

    def science_thread_initiate(self):

        self.science_thread = QThread()
        self.science_worker = ScienceWorker(self.science_subscriber)
        self.science_worker.moveToThread(self.science_thread)

        self.science_thread.started.connect(self.science_worker.run)
        self.science_worker.finished.connect(self.science_thread.quit)
        self.science_worker.finished.connect(self.science_worker.deleteLater)
        self.science_thread.finished.connect(self.science_thread.deleteLater)
        self.science_thread.start()
