from PyQt6.QtCore import QAbstractItemModel, QObject
import csv

class Model(QAbstractItemModel):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)

    def load(self):
        with open(self.file) as csvfile:
            reader = csv.reader(csvfile=csvfile)
                

