# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1375, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TheTab = QtWidgets.QTabWidget(self.centralwidget)
        self.TheTab.setGeometry(QtCore.QRect(0, 0, 1371, 811))
        self.TheTab.setObjectName("TheTab")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.GPSMapGroupBox = QtWidgets.QGroupBox(self.MainTab)
        self.GPSMapGroupBox.setGeometry(QtCore.QRect(10, 20, 661, 481))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.GPSMapGroupBox.setFont(font)
        self.GPSMapGroupBox.setObjectName("GPSMapGroupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.GPSMapGroupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 641, 431))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.GPSMapLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.GPSMapLayout.setContentsMargins(0, 0, 0, 0)
        self.GPSMapLayout.setObjectName("GPSMapLayout")
        self.VelocityGroupBox = QtWidgets.QGroupBox(self.MainTab)
        self.VelocityGroupBox.setGeometry(QtCore.QRect(10, 520, 661, 241))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VelocityGroupBox.setFont(font)
        self.VelocityGroupBox.setObjectName("VelocityGroupBox")
        self.VelocityTotalText = QtWidgets.QLabel(self.VelocityGroupBox)
        self.VelocityTotalText.setGeometry(QtCore.QRect(20, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VelocityTotalText.setFont(font)
        self.VelocityTotalText.setObjectName("VelocityTotalText")
        self.VelocityFLText = QtWidgets.QLabel(self.VelocityGroupBox)
        self.VelocityFLText.setGeometry(QtCore.QRect(20, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VelocityFLText.setFont(font)
        self.VelocityFLText.setObjectName("VelocityFLText")
        self.VelocityFRText = QtWidgets.QLabel(self.VelocityGroupBox)
        self.VelocityFRText.setGeometry(QtCore.QRect(20, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VelocityFRText.setFont(font)
        self.VelocityFRText.setObjectName("VelocityFRText")
        self.VelocityRLText = QtWidgets.QLabel(self.VelocityGroupBox)
        self.VelocityRLText.setGeometry(QtCore.QRect(20, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VelocityRLText.setFont(font)
        self.VelocityRLText.setObjectName("VelocityRLText")
        self.VelocityRRText = QtWidgets.QLabel(self.VelocityGroupBox)
        self.VelocityRRText.setGeometry(QtCore.QRect(340, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VelocityRRText.setFont(font)
        self.VelocityRRText.setObjectName("VelocityRRText")
        self.VelocityTotalLCDNumber = QtWidgets.QLCDNumber(self.VelocityGroupBox)
        self.VelocityTotalLCDNumber.setGeometry(QtCore.QRect(180, 50, 111, 31))
        self.VelocityTotalLCDNumber.setObjectName("VelocityTotalLCDNumber")
        self.VelocityFLLCDNumber = QtWidgets.QLCDNumber(self.VelocityGroupBox)
        self.VelocityFLLCDNumber.setGeometry(QtCore.QRect(180, 90, 111, 31))
        self.VelocityFLLCDNumber.setObjectName("VelocityFLLCDNumber")
        self.VelocityFRLCDNumber = QtWidgets.QLCDNumber(self.VelocityGroupBox)
        self.VelocityFRLCDNumber.setGeometry(QtCore.QRect(180, 130, 111, 31))
        self.VelocityFRLCDNumber.setObjectName("VelocityFRLCDNumber")
        self.VelocityRLLCDNumber = QtWidgets.QLCDNumber(self.VelocityGroupBox)
        self.VelocityRLLCDNumber.setGeometry(QtCore.QRect(180, 170, 111, 31))
        self.VelocityRLLCDNumber.setObjectName("VelocityRLLCDNumber")
        self.VelocityRRLCDNumber = QtWidgets.QLCDNumber(self.VelocityGroupBox)
        self.VelocityRRLCDNumber.setGeometry(QtCore.QRect(490, 50, 111, 31))
        self.VelocityRRLCDNumber.setObjectName("VelocityRRLCDNumber")
        self.IMUGroupBox = QtWidgets.QGroupBox(self.MainTab)
        self.IMUGroupBox.setGeometry(QtCore.QRect(690, 20, 661, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.IMUGroupBox.setFont(font)
        self.IMUGroupBox.setObjectName("IMUGroupBox")
        self.RollText = QtWidgets.QLabel(self.IMUGroupBox)
        self.RollText.setGeometry(QtCore.QRect(20, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RollText.setFont(font)
        self.RollText.setObjectName("RollText")
        self.PitchText = QtWidgets.QLabel(self.IMUGroupBox)
        self.PitchText.setGeometry(QtCore.QRect(20, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PitchText.setFont(font)
        self.PitchText.setObjectName("PitchText")
        self.YawText = QtWidgets.QLabel(self.IMUGroupBox)
        self.YawText.setGeometry(QtCore.QRect(20, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.YawText.setFont(font)
        self.YawText.setObjectName("YawText")
        self.RollLCDNumber = QtWidgets.QLCDNumber(self.IMUGroupBox)
        self.RollLCDNumber.setGeometry(QtCore.QRect(110, 50, 91, 31))
        self.RollLCDNumber.setObjectName("RollLCDNumber")
        self.PitchLCDNumber = QtWidgets.QLCDNumber(self.IMUGroupBox)
        self.PitchLCDNumber.setGeometry(QtCore.QRect(110, 100, 91, 31))
        self.PitchLCDNumber.setObjectName("PitchLCDNumber")
        self.YawLCDNumber = QtWidgets.QLCDNumber(self.IMUGroupBox)
        self.YawLCDNumber.setGeometry(QtCore.QRect(110, 150, 91, 31))
        self.YawLCDNumber.setObjectName("YawLCDNumber")
        self.BatteryGroupBox = QtWidgets.QGroupBox(self.MainTab)
        self.BatteryGroupBox.setGeometry(QtCore.QRect(690, 270, 661, 231))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BatteryGroupBox.setFont(font)
        self.BatteryGroupBox.setObjectName("BatteryGroupBox")
        self.BatteryShow = QtWidgets.QLabel(self.BatteryGroupBox)
        self.BatteryShow.setGeometry(QtCore.QRect(60, 30, 541, 191))
        self.BatteryShow.setText("")
        self.BatteryShow.setObjectName("BatteryShow")
        self.CommunicationGroupBox = QtWidgets.QGroupBox(self.MainTab)
        self.CommunicationGroupBox.setGeometry(QtCore.QRect(690, 520, 661, 241))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CommunicationGroupBox.setFont(font)
        self.CommunicationGroupBox.setObjectName("CommunicationGroupBox")
        self.RecievedText = QtWidgets.QLabel(self.CommunicationGroupBox)
        self.RecievedText.setGeometry(QtCore.QRect(20, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RecievedText.setFont(font)
        self.RecievedText.setObjectName("RecievedText")
        self.SentText = QtWidgets.QLabel(self.CommunicationGroupBox)
        self.SentText.setGeometry(QtCore.QRect(340, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SentText.setFont(font)
        self.SentText.setObjectName("SentText")
        self.RecievedMessage = QtWidgets.QLabel(self.CommunicationGroupBox)
        self.RecievedMessage.setGeometry(QtCore.QRect(20, 90, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RecievedMessage.setFont(font)
        self.RecievedMessage.setScaledContents(True)
        self.RecievedMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.RecievedMessage.setWordWrap(True)
        self.RecievedMessage.setObjectName("RecievedMessage")
        self.line = QtWidgets.QFrame(self.CommunicationGroupBox)
        self.line.setGeometry(QtCore.QRect(310, 30, 20, 201))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.SentMessage = QtWidgets.QLabel(self.CommunicationGroupBox)
        self.SentMessage.setGeometry(QtCore.QRect(340, 90, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SentMessage.setFont(font)
        self.SentMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SentMessage.setObjectName("SentMessage")
        self.TheTab.addTab(self.MainTab, "")
        self.CameraTab = QtWidgets.QWidget()
        self.CameraTab.setObjectName("CameraTab")
        self.MainCameraGroupBox = QtWidgets.QGroupBox(self.CameraTab)
        self.MainCameraGroupBox.setGeometry(QtCore.QRect(20, 10, 671, 761))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MainCameraGroupBox.setFont(font)
        self.MainCameraGroupBox.setObjectName("MainCameraGroupBox")
        self.MainCamera = QtWidgets.QLabel(self.MainCameraGroupBox)
        self.MainCamera.setGeometry(QtCore.QRect(10, 40, 651, 701))
        self.MainCamera.setStyleSheet("background : white")
        self.MainCamera.setText("")
        self.MainCamera.setObjectName("MainCamera")
        self.EndEffectorCameraGroupBox = QtWidgets.QGroupBox(self.CameraTab)
        self.EndEffectorCameraGroupBox.setGeometry(QtCore.QRect(710, 10, 641, 361))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EndEffectorCameraGroupBox.setFont(font)
        self.EndEffectorCameraGroupBox.setObjectName("EndEffectorCameraGroupBox")
        self.EndEffectorCamera = QtWidgets.QLabel(self.EndEffectorCameraGroupBox)
        self.EndEffectorCamera.setGeometry(QtCore.QRect(10, 40, 621, 311))
        self.EndEffectorCamera.setStyleSheet("background : blue")
        self.EndEffectorCamera.setText("")
        self.EndEffectorCamera.setObjectName("EndEffectorCamera")
        self.ScienceHubCameraGroupBox = QtWidgets.QGroupBox(self.CameraTab)
        self.ScienceHubCameraGroupBox.setGeometry(QtCore.QRect(710, 390, 641, 371))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScienceHubCameraGroupBox.setFont(font)
        self.ScienceHubCameraGroupBox.setObjectName("ScienceHubCameraGroupBox")
        self.ScienceHubCamera = QtWidgets.QLabel(self.ScienceHubCameraGroupBox)
        self.ScienceHubCamera.setGeometry(QtCore.QRect(10, 40, 621, 321))
        self.ScienceHubCamera.setStyleSheet("background : yellow")
        self.ScienceHubCamera.setText("")
        self.ScienceHubCamera.setObjectName("ScienceHubCamera")
        self.TheTab.addTab(self.CameraTab, "")
        self.ScienceTab = QtWidgets.QWidget()
        self.ScienceTab.setObjectName("ScienceTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ScienceTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1331, 761))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ScienceGraphGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ScienceGraphGrid.setContentsMargins(0, 0, 0, 0)
        self.ScienceGraphGrid.setObjectName("ScienceGraphGrid")
        self.Graph4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Graph4.setStyleSheet("background: red; margin: 20px")
        self.Graph4.setText("")
        self.Graph4.setObjectName("Graph4")
        self.ScienceGraphGrid.addWidget(self.Graph4, 1, 0, 1, 1)
        self.Graph5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Graph5.setStyleSheet("background: red; margin: 20px")
        self.Graph5.setText("")
        self.Graph5.setObjectName("Graph5")
        self.ScienceGraphGrid.addWidget(self.Graph5, 1, 1, 1, 1)
        self.Graph3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Graph3.setStyleSheet("background: red; margin: 20px")
        self.Graph3.setText("")
        self.Graph3.setObjectName("Graph3")
        self.ScienceGraphGrid.addWidget(self.Graph3, 0, 2, 1, 1)
        self.Graph = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Graph.setStyleSheet("background: red; margin: 20px")
        self.Graph.setText("")
        self.Graph.setObjectName("Graph")
        self.ScienceGraphGrid.addWidget(self.Graph, 0, 0, 1, 1)
        self.Graph2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Graph2.setStyleSheet("background: red; margin: 20px")
        self.Graph2.setText("")
        self.Graph2.setObjectName("Graph2")
        self.ScienceGraphGrid.addWidget(self.Graph2, 0, 1, 1, 1)
        self.Graph6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Graph6.setStyleSheet("background: red; margin: 20px")
        self.Graph6.setText("")
        self.Graph6.setObjectName("Graph6")
        self.ScienceGraphGrid.addWidget(self.Graph6, 1, 2, 1, 1)
        self.TheTab.addTab(self.ScienceTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TheTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "METU GUI"))
        self.GPSMapGroupBox.setTitle(_translate("MainWindow", "GPS Map"))
        self.VelocityGroupBox.setTitle(_translate("MainWindow", "Velocity"))
        self.VelocityTotalText.setText(_translate("MainWindow", "Velocity Total :"))
        self.VelocityFLText.setText(_translate("MainWindow", "Velocity FL :"))
        self.VelocityFRText.setText(_translate("MainWindow", "Velocity FR :"))
        self.VelocityRLText.setText(_translate("MainWindow", "Velocity RL :"))
        self.VelocityRRText.setText(_translate("MainWindow", "Velocity RR :"))
        self.IMUGroupBox.setTitle(_translate("MainWindow", "IMU Data"))
        self.RollText.setText(_translate("MainWindow", "Roll : "))
        self.PitchText.setText(_translate("MainWindow", "Pitch :"))
        self.YawText.setText(_translate("MainWindow", "Yaw :"))
        self.BatteryGroupBox.setTitle(_translate("MainWindow", "Battery"))
        self.CommunicationGroupBox.setTitle(_translate("MainWindow", "Communication"))
        self.RecievedText.setText(_translate("MainWindow", "Recieved : "))
        self.SentText.setText(_translate("MainWindow", "Sent :"))
        self.RecievedMessage.setText(_translate("MainWindow", "Random Bullshit Go"))
        self.SentMessage.setText(_translate("MainWindow", "Random Bullshit Come"))
        self.TheTab.setTabText(self.TheTab.indexOf(self.MainTab), _translate("MainWindow", "Main"))
        self.MainCameraGroupBox.setTitle(_translate("MainWindow", "Main Camera"))
        self.EndEffectorCameraGroupBox.setTitle(_translate("MainWindow", "End Effector Camera"))
        self.ScienceHubCameraGroupBox.setTitle(_translate("MainWindow", "Science Hub Camera"))
        self.TheTab.setTabText(self.TheTab.indexOf(self.CameraTab), _translate("MainWindow", "Camera"))
        self.TheTab.setTabText(self.TheTab.indexOf(self.ScienceTab), _translate("MainWindow", "Science Unit"))
         



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
