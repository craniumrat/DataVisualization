from PyQt6.QtCore import QObject
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
import csv

##TODO: We will try with QAbstractItemModel later. For now, let's try QStandardItemModel

class Model(QStandardItemModel):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)

    def load(self, file):
        with open(file) as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            self.setHorizontalHeaderLabels(headers)
            for i, row in enumerate(reader):
                items = [
                    QStandardItem(field) for field in row 
                ]

                self.insertRow(i, items)
                
