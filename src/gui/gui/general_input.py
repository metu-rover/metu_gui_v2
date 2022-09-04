import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray


class GeneralI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui
        super().__init__('gui_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray,'topic',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
    
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}' )    
