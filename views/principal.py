from functools import partial
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize, Qt, QMargins, Signal
from PySide6.QtGui import QIcon, QPalette, QColor, QFont

class Font(QFont):
    def __init__(self, n : int):
        super().__init__()
        self.setPointSize(n)
        self.setBold(False)
        self.setFamily("ROBOTO SANS-SERIF")

# class principal of the program
class Principal(QMainWindow):
    # atributos para los signal
    openInventary = Signal()
    openInput = Signal()
    openExit = Signal()

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
        layout.setVerticalSpacing(45)
        layout.setHorizontalSpacing(150)
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(self.LabelCentral(),0,0,1,2,Qt.AlignmentFlag.AlignCenter)
        # btnInput
        self.btnInput = self._Button("Input",r"src/add.ico")
        self.btnInput.clicked.connect(self.openInput.emit)
        layout.addWidget(self.btnInput,1,0)
        # btnOutput
        layout.addWidget(self._Button("Output", r"src/subtract.ico"),1,1)
        # btnInventary
        self.btnInventary = self._Button("Inventary", r"src/clipboard.svg", icon=90)
        self.btnInventary.clicked.connect(self.openInventary.emit)
        layout.addWidget(self.btnInventary,2,0)
        # settings
        layout.addWidget(self._Button("Settings", r"src/gear.ico"),2,1)
        # vertical layout
        layoutV = QVBoxLayout()
        layoutV.addLayout(layout)
        # btnexit
        self.btnExit = self._Button("Exit", r"src/exit.ico", 80, 80, 40)
        self.btnExit.clicked.connect(self.openExit.emit)
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