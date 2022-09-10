from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import random

"""
Science 
"""

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
        self._plot_ref = None # Only needed in the in-place draw
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
        self.subscription = self.create_subscription(Float64MultiArray, 'topic', self.listener_callback, 10)
    
    def listener_callback(self, msg):
        #self.get_logger().info(f'I heard: {msg.data}')
        self.update_plot(msg.data[0])


    #* https://www.pythonguis.com/tutorials/plotting-matplotlib/ is implemented for the plots.
    #* clean method is slower but it allows change in the x axis. Combination of clean and inplace methods can be used.

    '''
    def update_plot(self, num=0):
        # Drop off the first x,y element, append a new one.
        self.ydata = self.ydata[1:] + [num]
        self.xdata = self.xdata[1:] + [self.xdata[-1]+1]
        self.sc1.axes.cla()  # Clear the canvas.
        self.sc1.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.sc1.draw()
    '''

    def update_plot(self, num=0):
        # Drop off the first x,y element, append a new one.
        self.ydata = self.ydata[1:] + [num]
        self.xdata = self.xdata[1:] + [self.xdata[-1]+1]

        # Note: we no longer need to clear the axis.
        if self._plot_ref is None:
            # First time we have no plot reference, so do a normal plot.
            # .plot returns a list of line <reference>s, as we're
            # only getting one we can take the first element.
            plot_refs = self.sc1.axes.plot(self.xdata, self.ydata, 'r')
            self._plot_ref = plot_refs[0]

        else:
            # We have a reference, we can use it to update the data for that line.
            #self._plot_ref.set_data(self.xdata,self.ydata)
            self._plot_ref.set_ydata(self.ydata)
            self._plot_ref.set_xdata(self.xdata)
            print(len(self.xdata))

        self.sc1.draw()
