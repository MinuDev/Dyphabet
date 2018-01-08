import sys
from PyQt5.QtWidgets import QWidget, QAction, QMenu, QMainWindow, QFileDialog, qApp, QApplication

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #  Making the menu bar
        self.topMenu()
        #  Defining the windows' properties
        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Dyphabet')
        #  Drawing the window
        self.show()

    def topMenu(self):
        #  Creating the menu bar
        menuBar = self.menuBar()


        #  fileMenu START
        #  Adding the File menu in the bar
        fileMenu = menuBar.addMenu('File')
        #  Creating the submenus
        fOpenFile = QAction('Open file', self)
        fOpenFile.setShortcut('Ctrl+O')
        fOpenFile.setStatusTip('Open new file')
        fOpenFile.triggered.connect(self.showDialog)
        fSaveAs = QAction('Save as', self)
        fSave = QAction('Save', self)
        fExit = QAction('Exit', self)
        fExit.setShortcut('Alt+F4')
        action = fileMenu.exec_(self.mapToGlobal(event.pos()))
        if action == fExit:
            qApp.quit()
        #  Adding all submenus
        fileMenu.addAction(fOpenFile)
        fileMenu.addAction(fSaveAs)
        fileMenu.addAction(fSave)
        fileMenu.addAction(fExit)
        #  fileMenu END


        #  editMenu START
        editMenu = menuBar.addMenu('Edit')
        #  Creating the submenus
        eUndo = QAction('Undo', self)
        eRedo = QAction('Redo', self)
        eInsertSubtitle = QAction('Insert Subtitle', self)
        eInsertBefore = QAction('Insert Before', self)
        eRemoveSelected = QAction('Remove Selected', self)
        eCut = QAction('Cut', self)
        eCopy = QAction('Copy', self)
        ePaste = QAction('Paste', self)
        eStyle = QMenu('Styles', self)
        eSItalic = QAction('Italic', self)
        eSBold = QAction('Bold', self)
        eSUnderline = QAction('Underline', self)
        eSSetColor = QAction('Set color', self)
        eSDelColorTags = QAction('Remove color tags', self)
        eSDelAllTags = QAction('Remove all tags', self)
        eTranslatorMode = QAction('Translator mode', self, checkable=True)
        #  Adding all submenus
        editMenu.addAction(eUndo)
        editMenu.addAction(eRedo)
        editMenu.addAction(eInsertSubtitle)
        editMenu.addAction(eInsertBefore)
        editMenu.addAction(eRemoveSelected)
        editMenu.addAction(eCut)
        editMenu.addAction(eCopy)
        editMenu.addAction(ePaste)
        eStyle.addAction(eSItalic)
        eStyle.addAction(eSBold)
        eStyle.addAction(eSUnderline)
        eStyle.addAction(eSSetColor)
        eStyle.addAction(eSDelColorTags)
        eStyle.addAction(eSDelAllTags)
        editMenu.addMenu(eStyle)
        editMenu.addAction(eTranslatorMode)
        #  editMenu END


        #  viewMenu START
        viewMenu = menuBar.addMenu('View')
        #  Creating the submenus
        vToolbar = QAction('Show toolbar', self, checkable = True)
        vTimestamp = QAction('Show timestamp', self, checkable = True)
        vLinesCount = QAction('Show lines count', self, checkable = True)
        #  Setting checkables to True
        vToolbar.setChecked(True)
        vTimestamp.setChecked(True)
        vLinesCount.setChecked(True)
        #  Adding all submenus
        viewMenu.addAction(vToolbar)
        viewMenu.addAction(vTimestamp)
        viewMenu.addAction(vLinesCount)
        #  viewMenu END


        #  searchMenu START
        searchMenu = menuBar.addMenu('Search')
        #  Creating the submenus
        sSearch = QAction('Search', self)
        sFindNext = QAction('Find Next', self)
        sSearchAndReplace = QAction('Search and Replace', self)
        sFindByLineNumber = QAction('Find by line number', self)
        #  Adding all submenus
        searchMenu.addAction(sSearch)
        searchMenu.addAction(sFindNext)
        searchMenu.addAction(sSearchAndReplace)
        searchMenu.addAction(sFindByLineNumber)
        #  searchMenu END


        #  toolsMenu START
        toolsMenu = menuBar.addMenu('Tools')
        #  Creating the submenus
        tJoinSubtitles = QAction('Join subtitles', self)
        #  Adding all submenus
        toolsMenu.addAction(tJoinSubtitles)
        #  toolsMenu END


        #  settingsMenu START
        settingsMenu = menuBar.addMenu('Settings')
        #  Creating the submenus
        tSettings = QAction('Settings', self)
        tOutputSettings = QAction('Output Settings', self)
        tChangeLanguage = QMenu('Change language', self)
        tLanguage1 = QAction('Language1', self)
        tLanguage2 = QAction('Language2', self)
        tLanguage3 = QAction('Language3', self)
        tLanguage4 = QAction('Language4', self)
        #  Adding all submenus
        settingsMenu.addAction(tSettings)
        settingsMenu.addAction(tOutputSettings)
        settingsMenu.addMenu(tChangeLanguage)
        tChangeLanguage.addAction(tLanguage1)
        tChangeLanguage.addAction(tLanguage2)
        tChangeLanguage.addAction(tLanguage3)
        tChangeLanguage.addAction(tLanguage4)
        #  toolsMenu END


        #  helpMenu START
        helpMenu = menuBar.addMenu('Help')
        #  Creating the submenus
        hHelp = QAction('Help', self)
        hAbout = QAction('About', self)
        #  Adding all submenus
        helpMenu.addAction(hHelp)
        helpMenu.addAction(hAbout)
        #  helpMenu END

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '%USERNAME%\\Desktop')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
