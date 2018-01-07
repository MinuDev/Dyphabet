import sys
from PyQt5.QtWidgets import QWidget, QAction, QMenu, QMainWindow

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #  Making the menu bar
        self.topMenu()

        #  Defining the windows' properties
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Dyphabet')
        #  Drawing the window
        self.show()

    def topMenu(self):
        #  Creating the menu bar
        menuBar = self.menuBar()
        #  fileMenu START
        #  Adding the File menu in the bar
        fileMenu = menuBar.addMenu('File')
        #  Creating the submenus to the File menu
        FOpenFile = QAction('Open file', self)
        FSaveAs = QAction('Save as', self)
        FSave = QAction('Save', self)
        FExit = QAction('Exit', self)
        #  Adding the submenus to the File menu
        fileMenu.addAction(FOpenFile)
        fileMenu.addAction(FSaveAs)
        fileMenu.addAction(FSave)
        fileMenu.addAction(FExit)
        #  fileMenu END
        #  editMenu START
        editMenu = menuBar.addMenu('Edit')

        EUndo = QAction('Undo', self)
        ERedo = QAction('Redo', self)
        EInsertSubtitle = QAction('Insert Subtitle', self)
        EInsertBefore = QAction('Insert Before', self)
        ERemoveSelected = QAction('Remove Selected', self)
        ECut = QAction('Cut', self)
        ECopy = QAction('Copy', self)
        EPaste = QAction('Paste', self)
        EStyle = QMenu('Styles', self)
        ESItalic = QAction('Italic', self)
        ESBold = QAction('Bold', self)
        ESUnderline = QAction('Underline', self)
        ESSetColor = QAction('Set color', self)
        ESDelColorTags = QAction('Remove color tags', self)
        ESDelAllTags = QAction('Remove all tags', self)
        ETranslatorMode = QAction('Translator mode', self)
