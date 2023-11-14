from functools import partial
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QComboBox, QLineEdit, QTableWidget, QAbstractItemView, QMessageBox 
from PySide6.QtCore import QSize, Qt, QMargins, Signal
from PySide6.QtGui import QIcon, QPalette, QColor, QFont
from controllers.historyContr import Controller
from .historyDetail import Dialog


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
class History(QMainWindow):
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
        self.dataTable.cellDoubleClicked.connect(self.GetItemSelected)
        Controller.LoadData(self.dataTable)
        layoutV.addWidget(self.dataTable,
                          alignment=Qt.AlignmentFlag.AlignHCenter)
        layoutV.addSpacing(10)
        # btnDetail
        self.btnDetail = self._Button("View Details", r"src/detail.svg")
        self.btnDetail.clicked.connect(self.GetItemSelected)
        layoutV.addWidget(self.btnDetail,
                          alignment=Qt.AlignmentFlag.AlignHCenter)
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
        label = QLabel("History")
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
        self.comboBox.addItems(("id", "Comment"))
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
        self.btnSearching.setAutoDefault(True)
        self.btnSearching.clicked.connect(partial(Controller.SearchFilter, self))
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
        headers = ["id", "Type", "Comment", "Create at"]
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
        dataTable.setColumnWidth(2, 300)
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
    
    # get item for id
    def GetItemSelected(self):
        # get id
        if self.dataTable.selectedItems():
            id = self.dataTable.selectedIndexes()[0].data()
            self.dialog = Dialog(self)
            Controller.LoadDataDetail(self.dialog.dataTable, id)
            self.dialog.exec()
        else:
            QMessageBox.warning(self,
                                "Warning",
                                "Please select the record to view details",
                                QMessageBox.StandardButton.Ok)