#This is the base application to visualize data.
#Goals are:
#0. Work with CSV data.
#1. Provide a pivot table function.
#2. Provide options to visualize time series data.

import typing
from PyQt6.QtWidgets import QApplication, QTableView, QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from model import Model
from main_view import MainView
from main_controller import MainController
import sys

class App(QApplication):
    def __init__(self, argv: typing.List[str]) -> None:
        super(App, self).__init__(argv)
        self.model = Model(None)
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller, None, Qt.WindowType.Window)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())

