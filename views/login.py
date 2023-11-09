from functools import partial
from controllers.auth import Authetication
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QFormLayout, QPushButton, QHBoxLayout
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QIcon, QPalette, QColor, QFont

class Font(QFont):
    def __init__(self, n : int):
        super().__init__()
        self.setPointSize(n)
        self.setBold(False)

class Componente(QMainWindow):
    # atributos para los signal
    openPrincipal = Signal()
    # constructors
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Inventary")
        # valor fijo de la ventana
        self.setFixedSize(QSize(500, 250))
        # para iconos
        icon = QIcon(r"src/icon.ico")
        self.setWindowIcon(icon)
        # layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.IconCentral(), 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.LabelCentral(), 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch(1)
        layout.addLayout(self.Entry())
        # contenedor
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # labels central
    def LabelCentral(self):
        # label
        label = QLabel("Sign In")
        # modificar color
        palette = label.palette()
        palette.setColor(QPalette.WindowText, QColor("black"))
        label.setPalette(palette)
        # modificar el font
        font = label.font()
        font.setFamily("ROBOTO SANS-SERIF")
        font.setPointSize(20)
        label.setFont(font)
        return label
    
    # icon
    def IconCentral(self):
        icon = QIcon(r"src/black.ico")
        pixmap = icon.pixmap(50, 50)
        container = QLabel()
        container.setPixmap(pixmap)
        return container
    
    # entry
    def Entry(self):
        # username 
        labelUsername = QLabel("Username:")
        labelUsername.setFont(Font(11))
        self.username = QLineEdit()
        self.username.setPlaceholderText("")
        self.username.setFixedWidth(200)
        self.username.setFont(Font(11))
        self.username.setFocus()
        # password
        labelPassword = QLabel("Password:")
        labelPassword.setFont(Font(11))
        self.password = QLineEdit()
        self.password.setFixedWidth(200)
        self.password.setFont(Font(11))
        self.password.setEchoMode(QLineEdit.Password)
        # btn
        self.btnLogin = QPushButton("Sign in")
        self.btnLogin.setFixedSize(QSize(60,30))
        self.btnLogin.setFont(Font(11))
        self.btnLogin.clicked.connect(partial(Authetication.auth, self))
        self.btnLogin.setAutoDefault(True)
        # message
        self.message = QLabel()
        palette = self.message.palette()
        palette.setColor(QPalette.WindowText, QColor("RED"))
        self.message.setPalette(palette)
        self.message.setFont(Font(10))
        self.message.setVisible(False)
        # layout horizontal
        horizontal = QHBoxLayout()
        horizontal.addStretch(1)
        horizontal.addWidget(self.btnLogin)
        horizontal.addStretch(1)
        # layout horizontal message
        horizontalMessage = QHBoxLayout()
        horizontalMessage.addStretch(1)
        horizontalMessage.addWidget(self.message)
        horizontalMessage.addStretch(1)
        #layout
        layout = QFormLayout()
        layout.addRow(labelUsername, self.username)
        layout.addRow(str(), QWidget())
        layout.addRow(labelPassword, self.password)
        layout.addRow(str(), QWidget())
        layout.addRow(horizontalMessage)
        layout.addRow(horizontal)
        # container and center
        container = QHBoxLayout()
        container.addStretch(1)
        container.addLayout(layout)
        container.addStretch(1)
        return container
