from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
import io

"""
To be implemented.
"""

class CameraI:
    def __init__(self, ui) -> None:
        self.ui = ui
    
        self.ui.movie = QMovie("/home/yoy/Desktop/metu_rover/src/metu_gui_v2/assets/ezgif.com-gif-maker.gif")
        self.ui.MainCamera.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie2 = QMovie("/home/yoy/Desktop/metu_rover/src/metu_gui_v2/assets/ezgif.com-gif-maker (1).gif")
        self.ui.EndEffectorCamera.setMovie(self.ui.movie2)
        self.ui.movie2.start()

        self.ui.movie3 = QMovie("/home/yoy/Desktop/metu_rover/src/metu_gui_v2/assets/ezgif.com-gif-maker (2).gif")
        self.ui.ScienceHubCamera.setMovie(self.ui.movie3)
        self.ui.movie3.start()
        

        self.ui.movie4 = QMovie("/home/yoy/Desktop/metu_rover/src/metu_gui_v2/assets/ezgif.com-gif-maker (4).gif")
        self.ui.BatteryShow.setMovie(self.ui.movie4)
        self.ui.movie4.start()

        m = folium.Map(location=[39.889011,32.7801363], tiles="Stamen Toner", zoom_start=13)

        data = io.BytesIO()
        m.save(data, close_file=False)

        w = QtWebEngineWidgets.QWebEngineView()
        w.setHtml(data.getvalue().decode())
        self.ui.GPSMapLayout.addWidget(w)