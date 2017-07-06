import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):

    def close_application(self):

        # popup warning
        choice = QtWidgets.QMessageBox.question(self, 'Extract!', "Get into the chopper?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass

    def home(self):

        # button definition
        btn = QtWidgets.QPushButton("Press here!", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)

        # toolbar
        extractAction = QtWidgets.QAction(QtGui.QIcon('baticon.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        # checkbox (activate toggle depending on what you want the default to be)

        checkBox = QtWidgets.QCheckBox('Enlarge Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)
        # checkBox.toggle()

        # progress bar display

        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtWidgets.QPushButton('Download', self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        # Combo-box (dropdown) display

        print(self.style().objectName())
        self.styleChoice = QtWidgets.QLabel("Windows Vista", self)

        comboBox = QtWidgets.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(50, 250)

        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    # Combo-box (dropdown) definition

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))

    # random progress bar definition

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    # random enlarge window definition

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)


    def __init__(self):
        super(Window, self).__init__()

        # main window display
        self.setGeometry(0, 0, 500, 300)
        self.move(300, 300)
        self.setWindowTitle("PyQt test")
        self.setWindowIcon(QtGui.QIcon('baticon.ico'))

        # menubar

        #menubar definition
        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        # displaying statustip
        self.statusBar()

        # menubar display
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
