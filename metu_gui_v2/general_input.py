import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from PyQt5.QtCore import QObject, pyqtSignal


class GeneralWorker(QObject):
    
    finished = pyqtSignal()

    def __init__(self, ros_node) -> None:
        super().__init__()
        self.ros_node = ros_node
        print("GeneralI node is initialized")

    def run(self):

        rclpy.spin(self.ros_node)
        self.ros_node.destroy_node()


class GeneralI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui
        super().__init__('gui_general_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray,'topic',self.listener_callback,10)
    
    def listener_callback(self, msg):
        #self.get_logger().info(f'I heard: {msg.data}')
        self.ui.RollLCDNumber.display(msg.data[0])
        self.ui.PitchLCDNumber.display(msg.data[1])
        self.ui.YawLCDNumber.display(msg.data[2])

