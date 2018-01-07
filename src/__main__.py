from gui import GUI
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # TODO: Call the GUI module to start the main Window
    UI = QApplication(sys.argv)
    userInterface = GUI()
    sys.exit(UI.exec_())
