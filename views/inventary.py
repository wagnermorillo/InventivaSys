from functools import partial
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QComboBox, QLineEdit, QTableWidget, QHeaderView, QAbstractItemView, QDialogButtonBox, QMessageBox, QSizePolicy 
from PySide6.QtCore import QSize, Qt, QMargins, Signal
from PySide6.QtGui import QIcon, QPalette, QColor, QFont
from controllers.inventaryContr import Controller
from .productDetails import Dialog

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
        self.setPointSize(11)
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
        layoutV.addSpacing(40)
        layoutV.addLayout(self.Searching())
        # dataTable
        self.dataTable = self.Table()
        Controller.LoadData(self.dataTable)
        layoutV.addWidget(self.dataTable,
                          alignment=Qt.AlignmentFlag.AlignHCenter)
        # layoutH for button
        layoutH = QHBoxLayout()
        # btnAdd
        self.btnAdd = self._Button("Add Product", r"src/add.svg")
        self.btnAdd.clicked.connect(partial(self.OpenDialog, "Add Product", True))
        layoutH.addWidget(self.btnAdd)
        # btnEdit
        self.btnEdit = self._Button("Edit Product", r"src/edit.svg")
        self.btnEdit.clicked.connect(partial(self.GetItemSelected, True))
        layoutH.addWidget(self.btnEdit)
        # btnDelete
        self.btnDelete = self._Button("Delete Product", r"src/delete.svg")
        self.btnDelete.clicked.connect(self.GetItemSelected)
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
        self.comboBox.addItems(("id", "Name", "Description", "Quantity"))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox.setFixedWidth(150)
        self.comboBox.setCurrentIndex(0)
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
        self.btnSearching.clicked.connect(partial(Controller.SearchFilter, self))
        self.btnSearching.setAutoDefault(True)
        # layout horizontal
        widget = QWidget()
        widget.setFixedWidth(482)
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.comboBox)
        layoutH.addWidget(self.textBox)
        layoutH.addWidget(self.btnSearching)
        layoutH.addWidget(widget)
        layoutH.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        return layoutH

    # table
    def Table(self):
        dataTable = QTableWidget(0, 4, self)
        headers = ["id", "Name", "Description", "Quantity"]
        dataTable.setHorizontalHeaderLabels(headers)
        dataTable.horizontalHeader().setFont(FontBold())
        dataTable.setSortingEnabled(True)
        dataTable.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        dataTable.verticalHeader().setVisible(False)
        dataTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        dataTable.horizontalHeader().setStretchLastSection(True)
        # width
        dataTable.setFixedWidth(1000)
        dataTable.setColumnWidth(0, 100)
        dataTable.setColumnWidth(1, 300)
        dataTable.setColumnWidth(2, 480)
        dataTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        dataTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
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

    # open add/edit product
    def OpenDialog(self, title : str, status: bool, name : str = None, description : str = None, id : int = None):
        # instancia
        self.dialog = Dialog(self, title, name, description)
        self.dialog.btnDialog.button(
            QDialogButtonBox.StandardButton.Save).clicked.connect(partial(
                Controller.CreateUpdate, self.dialog, status, id
            ))
        self.dialog.exec()
        Controller.LoadData(self.dataTable)

    # get item for id
    def GetItemSelected(self, status : bool = False):
        # get id
        if self.dataTable.selectedItems():
            id = self.dataTable.selectedIndexes()[0].data()
            name = self.dataTable.selectedIndexes()[1].data()
            description = self.dataTable.selectedIndexes()[2].data()
            if status:
                self.OpenDialog("Edit Product", False, name, description, id)
            else:
                Controller.Delete(self, id)
        else:
            QMessageBox.warning(self,
                                "Warning",
                                "Please select the product to edit",
                                QMessageBox.StandardButton.Ok)
                    
