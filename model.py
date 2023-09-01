from typing import Any
from PyQt6.QtCore import QModelIndex, QObject, QAbstractTableModel, Qt
import pandas as pd

class Model(QAbstractTableModel):
    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.df = pd.DataFrame()

    def load(self, file):
        self.df = pd.read_csv(file)

        topLeft = self.index(0, 0)
        bottomRight = self.index(self.df.shape[0] - 1, self.df.shape[1] - 1)
        self.modelReset.emit()

    def rowCount(self, parent: QModelIndex = ...) -> int:
         return self.df.shape[0]
    
    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self.df.shape[1]

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            return str(self.df.iat[index.row(), index.column()])

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.df.columns.values