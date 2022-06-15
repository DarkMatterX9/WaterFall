import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

HOMEPAGE = ""
MASTER_FONT = QFont("Sanserif", 12)

def main():
    # creating main window class
    class MainWindow(QMainWindow):
        
        #Constructor 
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)

            #set window title
            self.setWindowTitle("WaterFall")
            #set window icon
            #self.setWindowIcon(QIcon("icons/python.png"))
            self.setGeometry(200, 200, 900, 600)

            #add toolbar
            toolbar = QToolBar()
            self.addToolBar(toolbar)

            #toolbar settings
            toolbar.setFixedHeight(30)

            #Back Button (toolbar)
            self.backButton = QPushButton()
            self.backButton.setIcon(QIcon('icons/backbtn.png'))
            self.backButton.setIconSize(QSize(29, 29))
            self.backButton.clicked.connect(self.backBtn)

            #Forward Button (toolbar)
            self.forwardButton = QPushButton()
            self.forwardButton.setIcon(QIcon('icons/forwardbtn.png'))
            self.forwardButton.setIconSize(QSize(29, 29))
            self.forwardButton.clicked.connect(self.forwardBtn)

            #Reload Button (toolbar)
            self.reloadButton = QPushButton()
            self.reloadButton.setIcon(QIcon('icons/reloadbtn.png'))
            self.reloadButton.setIconSize(QSize(29, 29))
            self.reloadButton.clicked.connect(self.reloadBtn)

            #Home Button (toolbar)
            self.homeButton = QPushButton()
            self.homeButton.setIcon(QIcon('icons/homebtn.png'))
            self.homeButton.setIconSize(QSize(29, 29))
            self.homeButton.clicked.connect(self.homeBtn)

            #address box (toolbar)
            self.addressLineEdit = QLineEdit()

            #completer array
            self.array_completer = []
            completer = QCompleter(self.array_completer)
            completer.setFilterMode(Qt.MatchFlag.MatchContains)

            self.addressLineEdit.setFont(MASTER_FONT)
            self.addressLineEdit.returnPressed.connect(self.goBtn)
            self.addressLineEdit.mousePressEvent = lambda _ : self.addressLineEdit.selectAll()

            #address bar (history)
            self.addressHistory = QComboBox()
            self.addressHistory.setFont(MASTER_FONT)
            self.addressHistory.setLineEdit(self.addressLineEdit)
            self.addressHistory.setMinimumContentsLength(60)
            self.addressHistory.setCompleter(completer)

            #search Button (toolbar)
            self.searchButton = QPushButton()
            self.searchButton.setText("GO")
            self.searchButton.setFont(MASTER_FONT)
            self.searchButton.clicked.connect(self.goBtn)
        

            #add objects to toolbar
            toolbar.addWidget(self.backButton)
            toolbar.addWidget(self.forwardButton)
            toolbar.addWidget(self.reloadButton)
            toolbar.addWidget(self.homeButton)
            toolbar.addWidget(self.addressHistory)
            toolbar.addWidget(self.searchButton)

            # Creating a QWebEngineView
            self.browser = QWebEngineView()

            #open homepage
            self.browser.setUrl(QUrl(HOMEPAGE))
            self.addressLineEdit.setText(HOMEPAGE)

            #set widgets view
            self.setCentralWidget(self.browser)
            #show the view now
            self.show()

        #Function to execute on go btn press
        def goBtn(self):
            url = self.addressLineEdit.text()
            if (self.addressHistory.findText(url) == -1):
                self.addressHistory.addItem(url)
                self.array_completer.append(url)
            else:
                pass

            self.browser.load(QUrl(url))
            self.addressLineEdit.setFocus()
            self.addressLineEdit.selectAll()

        # back button (previous webpage backwards)
        def backBtn(self):
            self.browser.back()

        # forward button (previouos webpage forward)
        def forwardBtn(self):
            self.browser.forward()

        # Home button (navigates to the home page)
        def homeBtn(self):
            self.browser.load(QUrl(HOMEPAGE))
            self.addressLineEdit.setText(HOMEPAGE)

        # reload button (reload the current webpage)
        def reloadBtn(self):
            self.browser.reload()

    # set application to qapplication
    app = QApplication(sys.argv)
    # window = the app window (browser window)
    window = MainWindow()
    # execute now
    app.exec_()

# execute this first
if __name__ == "__main__":
    # Set homepage
    HOMEPAGE = "https://www.google.com"
    #call main
    main()





