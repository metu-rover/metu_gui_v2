from PyQt5.QtCore import QObject, pyqtSignal
from rclpy.executors import MultiThreadedExecutor

"""
Class for spinning the nodes.
"""
class RecieverWorker(QObject):
    
    finished = pyqtSignal()

    def __init__(self, general_subscriber, science_subscriber) -> None:
        super().__init__()
        self.general_subscriber = general_subscriber
        self.science_subscriber = science_subscriber

    def run(self):

        #! Executor'u spinlendiği yerde tanımlamak lazım. Çünkü herhangi bir yerde self.executor yapınca hata veriyor.
        #! Teorime göre hali hazırda global bir executor var ve onla çakışıyor.
        
        # Executor is for adding multiple nodes at the same file. rospy.spin(node) allows only one node per executable file to run. 
        # However with executor this functionality is extended.
        executor = MultiThreadedExecutor() 
        executor.add_node(self.general_subscriber)
        executor.add_node(self.science_subscriber)
        executor.spin()
        self.general_subscriber.destroy_node()
        self.science_subscriber.destroy_node()