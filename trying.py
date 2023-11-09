from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

class MyTable(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.setHorizontalHeaderLabels(["Name", "Description", "Quantity"])
        self.setHorizontalHeader()
        self.initUI()

    def initUI(self):
        self.cellChanged.connect(self.on_cell_changed)
        self.add_data(3)  # Agregamos 3 filas de ejemplo
        self.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)  # Establecer columna inicial de ordenación

        # Habilitar ordenación
        self.setSortingEnabled(True)

    def add_data(self, num_rows):
        for i in range(num_rows):
            self.insertRow(self.rowCount())
            self.setItem(self.rowCount() - 1, 0, QTableWidgetItem("Item {}".format(self.rowCount())))
            self.setItem(self.rowCount() - 1, 1, QTableWidgetItem("Description {}".format(self.rowCount())))
            self.setItem(self.rowCount() - 1, 2, QTableWidgetItem("1"))

    def on_cell_changed(self, row, col):
        item = self.item(row, col)
        if item is not None:
            print("Valor en fila {}, columna {}: {}".format(row, col, item.text()))

if __name__ == "__main__":
    import sys
"""
    app = QApplication(sys.argv)
    window = QMainWindow()
    table = MyTable(0, 3)
    window.setCentralWidget(table)
    window.show()
    sys.exit(app.exec_())
"""

from models.models import Product
from models.db import session

with session:
    product = session.query(Product).all()
    print(f"trage el producto: {product[0]} len: {len(product)}")
