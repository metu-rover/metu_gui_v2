import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray

from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time


class Worker(QObject):
    
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, ui) -> None:
        super().__init__()
        self.ui = ui

    def run(self):
        rclpy.init()
        print("GeneralI node is initialized")
        minimal_subscriber = GeneralI(self.ui)
        rclpy.spin(minimal_subscriber)
        minimal_subscriber.destroy_node()
        rclpy.shutdown()


class GeneralI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui
        super().__init__('gui_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray,'topic',self.listener_callback,10)
    
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')
        self.ui.RollLCDNumber.display(msg.data[0])
        self.ui.PitchLCDNumber.display(msg.data[1])
        self.ui.YawLCDNumber.display(msg.data[2])

