from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout, QHBoxLayout, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import QSize, Qt, QMargins, Signal
from PySide6.QtGui import QIcon, QPalette, QColor, QFont

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

class Font(QFont):
    def __init__(self, n: int):
        super().__init__()
        self.setPointSize(n)
        self.setBold(False)

class FontBold(QFont):
    def __init__(self):
        super().__init__()
        self.setBold(True)

# class of inventary window
class Inventary(QMainWindow):
    # atributos para los signal
    openPrincipal = Signal()

    # constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventary")
        # valor de la ventana
        self.resize(QSize(1066, 600))
        self.setMinimumSize(QSize(1066, 600))
        # para iconos
        icon = QIcon(r"src/icon.ico")
        self.setWindowIcon(icon)
        # layout vertical
        layoutV = QVBoxLayout()
        layoutV.addWidget(self.LabelCentral())
        layoutV.addLayout(self.Searching())
        # dataTable
        self.dataTable = self.Table()
        self._DataTest()
        layoutV.addWidget(self.dataTable)
        # layoutH for button
        layoutH = QHBoxLayout()
        # btnAdd
        self.btnAdd = self._Button("Add Product", r"src/add.svg")
        layoutH.addWidget(self.btnAdd)
        # btnEdit
        self.btnEdit = self._Button("Edit Product", r"src/edit.svg")
        layoutH.addWidget(self.btnEdit)
        # btnDelete
        self.btnDelete = self._Button("Delete Product", r"src/delete.svg")
        layoutH.addWidget(self.btnDelete)
        layoutV.addLayout(layoutH)
        # btnExit
        self.btnExit = self._Button("Exit", r"src/exit.ico", 80, 80, 40)
        self.btnExit.clicked.connect(self.openPrincipal.emit)
        layoutV.addWidget(
            self.btnExit, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
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
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label

    # searching
    def Searching(self):
        # combo
        self.comboBox = QComboBox()
        self.comboBox.addItems(("Name", "Description", "Quantity"))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox.setFixedWidth(150)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.setFont(Font(11))
        self.comboBox.setFixedHeight(30)
        # textBox
        self.textBox = QLineEdit()
        self.textBox.setPlaceholderText("Search product")
        self.textBox.setFocus()
        self.textBox.setFixedWidth(200)
        self.textBox.setFont(Font(11))
        self.textBox.setFixedHeight(30)
        # btnSearching
        self.btnSearching = QPushButton("Search")
        self.btnSearching.setFixedWidth(150)
        icon = QIcon(r"src/search.ico").pixmap(60, 60)
        self.btnSearching.setIcon(icon)
        self.btnSearching.setFont(Font(11))
        self.btnSearching.setFixedHeight(30)
        # layout horizontal
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.comboBox)
        layoutH.addWidget(self.textBox)
        layoutH.addWidget(self.btnSearching)
        layoutH.setAlignment(Qt.AlignmentFlag.AlignLeft |
                             Qt.AlignmentFlag.AlignVCenter)
        return layoutH

    # table
    def Table(self):
        dataTable = QTableWidget(0, 3)
        headers = ["Name", "Description", "Quantity"]
        dataTable.setHorizontalHeaderLabels(headers)
        dataTable.horizontalHeader().setFont(FontBold())
        dataTable.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        dataTable.setSortingEnabled(True)
        dataTable.verticalHeader().setVisible(False)
        dataTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        dataTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        return dataTable

    # button option
    def _Button(self, text: str = "hola", path: str = r"src/icon.ico", w=110, h=55, icon=40):
        # boton
        btnGeneric = QPushButton()
        btnGeneric.setFixedSize(w, h)
        # label
        label = QLabel(text)
        label.setFont(Font(11))
        # icono
        icon = QIcon(path).pixmap(icon, icon)
        iconLabel = QLabel()
        iconLabel.setPixmap(icon)
        # layout (magia)
        layout = QVBoxLayout()
        layout.setContentsMargins(QMargins(0, 0, 0, 0))
        layout.setSpacing(1)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(iconLabel, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label, 0, Qt.AlignmentFlag.AlignCenter)
        btnGeneric.setLayout(layout)
        return btnGeneric

    # data test
    def _DataTest(self):
        for i in range(3):
            self.dataTable.insertRow(self.dataTable.rowCount())
            self.dataTable.setItem(self.dataTable.rowCount(
            ) - 1, 0, QTableWidgetItem("Item {}".format(self.dataTable.rowCount())))
            self.dataTable.setItem(self.dataTable.rowCount(
            ) - 1, 1, QTableWidgetItem("Description {}".format(self.dataTable.rowCount())))
            self.dataTable.setItem(
                self.dataTable.rowCount() - 1, 2, QTableWidgetItem("1"))
