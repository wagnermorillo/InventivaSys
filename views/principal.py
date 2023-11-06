from functools import partial
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize, Qt, QMargins
from PySide6.QtGui import QIcon, QPalette, QColor, QFont
from controllers.principalContr import Controller

class Color(QWidget):
    def __init__(self, nuevo_color, child : QWidget) -> QWidget:
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)
        # hijo
        layout = QVBoxLayout()
        layout.addWidget(child)
        self.setLayout(layout)

class Font(QFont):
    def __init__(self, n : int):
        super().__init__()
        self.setPointSize(n)
        self.setBold(False)
        self.setFamily("ROBOTO SANS-SERIF")

# class principal of the program
class Principal(QMainWindow):
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
        # layout de grilla
        layout = QGridLayout()
        layout.addLayout(self.LabelCentral(),0,0,1,2,Qt.AlignmentFlag.AlignCenter)
        # btnInput
        self.btnInput = self._Button("Input",r"src/add.ico")
        self.btnInput.clicked.connect(partial(Controller.Input, self))
        layout.addWidget(self.btnInput,1,0)
        layout.addWidget(self._Button("Output", r"src/subtract.ico"),1,1)
        layout.addWidget(self._Button("Inventary", r"src/clipboard.svg"),2,0)
        layout.addWidget(self._Button("Settings", r"src/gear.ico"),2,1)
        layout.setVerticalSpacing(45)
        layout.setHorizontalSpacing(150)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # vertical layout
        layoutV = QVBoxLayout()
        layoutV.addLayout(layout)
        self.btnExit = self._Button("Exit", r"src/exit.ico", 80, 80, 40)
        self.btnExit.clicked.connect(partial(Controller.Exit, self))
        layoutV.addWidget(self.btnExit,alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        # container
        container = QWidget()
        container.setLayout(layoutV)
        self.setCentralWidget(container)

    # label central
    def LabelCentral(self):
        # label
        label = QLabel("Inventary")
        # modificar color
        palette = label.palette()
        palette.setColor(QPalette.WindowText, QColor("black"))
        label.setPalette(palette)
        # modificar el font
        font = label.font()
        font.setFamily("ROBOTO SANS-SERIF")
        font.setPointSize(20)
        label.setFont(font)
        # icono
        icon = QIcon(r"src/black.ico").pixmap(60, 60)
        iconLabel = QLabel()
        iconLabel.setPixmap(icon)
        # contenedor
        container = QVBoxLayout()
        container.setContentsMargins(0,0,0,0)
        container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container.addWidget(iconLabel, alignment=Qt.AlignmentFlag.AlignHCenter)
        container.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        return container
    
    # button
    def _Button(self, text : str = "hola", path : str = r"src/icon.ico", w = 200, h = 150, icon=80):
        # boton 
        btnEntrada = QPushButton()
        btnEntrada.setFixedSize(w,h)
        # label
        label = QLabel(text)
        label.setFont(Font(14))
        # icono
        icon = QIcon(path).pixmap(icon, icon)
        iconLabel = QLabel()
        iconLabel.setPixmap(icon)
        # layout (magia)
        layout = QVBoxLayout()
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.setSpacing(1)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(iconLabel, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label, 0, Qt.AlignmentFlag.AlignCenter)
        btnEntrada.setLayout(layout)
        return btnEntrada