from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import random

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class ScienceI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui

        #? Grafiklere toolbar eklenebilir.

        self.sc1 = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc2 = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc3 = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc4 = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc5 = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc6 = MplCanvas(self, width=5, height=4, dpi=100)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 180) for i in range(n_data)]
        self.update_plot()

        self.sc2.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.sc3.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.sc4.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.sc5.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.sc6.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        self.ui.ScienceGraphGrid.addWidget(self.sc1, 0, 0, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.sc2, 0, 1, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.sc3, 0, 2, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.sc4, 1, 0, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.sc5, 1, 1, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.sc6, 1, 2, 1, 1)

        super().__init__('gui_science_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray, 'topic', self.listener_callback,10)
    
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')
        self.update_plot(msg.data[0])

        # TODO https://www.pythonguis.com/tutorials/plotting-matplotlib/ -> Update inplace implemente et.

        #* This is just a demo.
    def update_plot(self, num= 0):
        self.ydata = self.ydata[1:] + [num]
        self.sc1.axes.cla()
        self.sc1.axes.plot(self.xdata, self.ydata, 'r')
        self.sc1.draw()