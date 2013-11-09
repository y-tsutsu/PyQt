# coding: utf-8

# Form implementation generated from reading ui file 'ramen_timer.ui'
#
# Created: Sat Nov  9 14:40:25 2013
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.count = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 1, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 0, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 0, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.resetButton.clicked.connect(self.reset_countdown)
        self.stopButton.clicked.connect(self.stop_countdown)
        self.startButton.clicked.connect(self.start_countdown)
        self.quitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.reset_countdown()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ramen Timer"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.resetButton.setText(_translate("MainWindow", "RESET"))

        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.do_countdown)

    def update_display(self):
        i = self.count / 100
        self.lcdNumber.display("%6.2f" % (self.count / 100))

    def do_countdown(self):
        self.count -= 1
        self.update_display()
        if self.count <= 0:
            self.stop_countdown()
 
    def start_countdown(self):
        if self.count > 0:
            self.timer.start()
 
    def stop_countdown(self):
        self.timer.stop()

    def reset_countdown(self):
        self.stop_countdown()
        self.count = 18000
        self.update_display()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
