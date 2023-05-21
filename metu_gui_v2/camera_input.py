from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
import folium
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimediaWidgets import *
import io
import cv2
import numpy as np
from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
import time
"""
To be implemented.
"""

class CameraI:
    def __init__(self, ui) -> None:
        self.ui = ui                                
       
        m = folium.Map(location=[39.889011,32.7801363], tiles="Stamen Toner", zoom_start=13)

        data = io.BytesIO()
        m.save(data, close_file=False)

        w = QtWebEngineWidgets.QWebEngineView()
        w.setHtml(data.getvalue().decode())
        self.ui.GPSMapLayout.addWidget(w)

