from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

"""
This class is for handling the general tab. Class itself is a ros node and it has access to ui.
"""

class GeneralI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui
        super().__init__('gui_general_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray,'topic',self.listener_callback,10)
    
    def listener_callback(self, msg):
        #self.get_logger().info(f'I heard: {msg.data}')

        # Changing the LCDnumbers according to the ros data
        self.ui.RollLCDNumber.display(msg.data[0])
        self.ui.PitchLCDNumber.display(msg.data[1])
        self.ui.YawLCDNumber.display(msg.data[2])
        self.ui.RecievedMessage.setText(f"{msg.data}")