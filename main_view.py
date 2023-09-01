from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolBar, QStyle, QTableView
from PyQt6.QtGui import QAction

from model import Model
from main_controller import MainController

class MainView(QMainWindow):
    def __init__(self, model: Model, controller: MainController, parent: QMainWindow | None = ..., flags:  QtCore.Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.model = model
        self.controller = controller

        screen = self.screen()
        self.resize(screen.availableSize() * .7)
        self.setWindowTitle("Data Visualization")

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QtCore.QSize(16, 16))
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)

        openAction = QAction("Open", self)
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_DirOpenIcon')
        icon = self.style().standardIcon(pixmapi)
        openAction.setIcon(icon)
        openAction.triggered.connect(self.controller.onOpenActionTriggered)
        toolbar.addAction(openAction)
        

        self.addToolBar(toolbar)

        layout = QVBoxLayout()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.centralWidget().setLayout(layout)

        ##Add a File > Open menu to create a file select box. This will load the CSV file.
        ##Create the QStandardItemModel using the CSV data.
        
        ##Show the data using QTableView in the main application.
        tableview = QTableView(self)
        tableview.setModel(self.model)
        layout.addWidget(tableview)


