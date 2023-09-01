from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QFileDialog

class MainController(object):
    def __init__(self, model) -> None:
        self.model = model

    #@pyqtSlot(bool)
    def onOpenActionTriggered(self, value: bool):
        fname = QFileDialog.getOpenFileName(None, "Open Data File", None, "All files (*)")
        print(fname[0])
        self.model.load(fname[0])
