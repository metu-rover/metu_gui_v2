from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import random

"""
Sample class for matplotlib usage in Pyqt. 
"""
#TODO This class might be deprecated.
#? This is only for figures it does not include titles, labels etc.
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

"""
This class is for handling the science tab. Class itself is a ros node and it has access to ui.
This class is mostly based on graphs.
"""

class ScienceI(Node):
    def __init__(self, ui) -> None:
        self.ui = ui

        #? Grafiklere toolbar eklenebilir.

        self.graphs = [MplCanvas(self, width=5, height=4, dpi=100) for i in range(6)]

        n_data = 50
        # These are not the ideal solutions but they are for test cases. So nvm. This graphs will be configured after the needs are set properly.
        self.xdata = [list(range(n_data))for i in range(6)]
        self.ydata = [[random.randint(0, 180) for i in range(n_data)] for i in range(6)]
        self._plot_ref = [None for i in range(6)] # Only needed in the in-place draw
        self.update_plot()


        self.ui.ScienceGraphGrid.addWidget(self.graphs[0], 0, 0, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.graphs[1], 0, 1, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.graphs[2], 0, 2, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.graphs[3], 1, 0, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.graphs[4], 1, 1, 1, 1)
        self.ui.ScienceGraphGrid.addWidget(self.graphs[5], 1, 2, 1, 1)

        super().__init__('gui_science_test_subscriber')
        self.subscription = self.create_subscription(Float64MultiArray, 'topic', self.listener_callback, 10)
    
    def listener_callback(self, msg):
        #self.get_logger().info(f'I heard: {msg.data}')
        self.update_plot(msg.data)


    #* https://www.pythonguis.com/tutorials/plotting-matplotlib/ is implemented for the plots.
    #* clean method is slower but it allows change in the x axis. Combination of clean and inplace methods can be used.

    # TODO default num=0 is dirty

    
    # Clean method
    def update_plot(self, num=None):
        for i in range(len(self.ydata)):
        # Drop off the first x,y element, append a new one.
            self.ydata[i] = self.ydata[i][1:] + [num[i]] if num != None else self.ydata[i]  # This line is terrible
            self.xdata[i] = self.xdata[i][1:] + [self.xdata[i][-1]+1] if num != None else self.xdata[i] # This line is terrible
            self.graphs[i].axes.cla()  # Clear the canvas.
            self.graphs[i].axes.plot(self.xdata[i], self.ydata[i], 'r')
            # Trigger the canvas to update and redraw.
            self.graphs[i].draw()
    

    """
    # In-place method
    def update_plot(self, num=None):
        # Drop off the first x,y element, append a new one.
        for i in range(len(self.ydata)):
            self.ydata[i] = self.ydata[i][1:] + [num[i]] if num != None else self.ydata[i]  # This line is terrible
            self.xdata[i] = self.xdata[i][1:] + [self.xdata[i][-1]+1] if num != None else self.ydata[i]  # This line is terrible

            # Note: we no longer need to clear the axis.
            if self._plot_ref[i] is None:
                # First time we have no plot reference, so do a normal plot.
                # .plot returns a list of line <reference>s, as we're
                # only getting one we can take the first element.
                plot_refs = self.graphs[i].axes.plot(self.xdata[i], self.ydata[i], 'r')
                self._plot_ref[i] = plot_refs[0]

            else:
                # We have a reference, we can use it to update the data for that line.
                #self._plot_ref.set_data(self.xdata,self.ydata)
                self._plot_ref[i].set_ydata(self.ydata[i])
                self._plot_ref[i].set_xdata(self.xdata[i])

            self.graphs[i].draw()
    """