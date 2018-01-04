import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Dyphabet')
        self.show()
