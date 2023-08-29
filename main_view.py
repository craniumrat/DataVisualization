from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QToolBar, QPushButton, QStyle
from PyQt6.QtGui import QScreen

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

        openButton = QPushButton("Open")
        pixmapi = getattr(QStyle.StandardPixmap, 'SP_DirOpenIcon')
        icon = self.style().standardIcon(pixmapi)
        openButton.setIcon(icon)
        toolbar.addWidget(openButton)

        self.addToolBar(toolbar)

        layout = QVBoxLayout()
        self.setLayout(layout)

        ##Add a File > Open menu to create a file select box. This will load the CSV file.
        ##Create the QStandardItemModel using the CSV data.
        
        ##Show the data using QTableView in the main application.

        label = QLabel("Data Visualizaation")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)


