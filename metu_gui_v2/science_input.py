from rclpy.node import Node
from std_msgs.msg import Float64MultiArray


class ScienceI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui
        super().__init__('gui_science_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray, 'topic', self.listener_callback,10)
    
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')

