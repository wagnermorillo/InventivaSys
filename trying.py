from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QFormLayout, QPushButton, QHBoxLayout, QGridLayout, QSizePolicy, QApplication
from PySide6.QtCore import QSize, Qt, QMargins
from PySide6.QtGui import QIcon, QPalette, QColor, QFont
import sys


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class ResizableButtons(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(QSize(1066, 600))
        self.setMinimumSize(QSize(1066,600))
        # grid
        grid = QGridLayout()
        for i in range(3):
            for j in range(3):
                grid.addWidget(Color("red"),i,j)
        # vertical
        vertical = QVBoxLayout()
        vertical.addLayout(grid)
        vertical.addWidget(Color("blue"))
        # contenedor
        container = QWidget()
        container.setLayout(vertical)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResizableButtons()
    window.show()
    sys.exit(app.exec_())
