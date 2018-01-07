import sys
from PyQt5.QtWidgets import QWidget, QAction, QMenu

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        openFileMenu = QAction('Open file...', self)
        fileMenu.addAction(openFileMenu)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Dyphabet')
        self.show()"""

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()
