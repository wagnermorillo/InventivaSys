from functools import partial
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize, Qt, QMargins
from PySide6.QtGui import QIcon, QPalette, QColor, QFont
# class of input window
class Input(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventary")
        # valor de la ventana
        self.resize(QSize(1066, 600))
        self.setMinimumSize(QSize(1066,600))
        # para iconos
        icon = QIcon(r"src/icon.ico")
        self.setWindowIcon(icon)