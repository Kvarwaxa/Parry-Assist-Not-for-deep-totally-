from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class OverlayManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.hide_alert)

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.setGeometry(screen)
        self.label = QtWidgets.QLabel("PARRY NOW NIGGER", self)
        self.label.setStyleSheet("color: red; font-size: 80px; font-weight: bold;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(self.rect())
        self.hide()

    def trigger(self):
        self.show()
        self.timer.start()

    def hide_alert(self):
        self.hide()
        self.timer.stop()

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
