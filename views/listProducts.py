from PySide6.QtWidgets import QWidget, QPushButton, QDialog, QVBoxLayout, QMainWindow, QDialogButtonBox, QLabel, QComboBox, QLineEdit, QHBoxLayout, QTableWidget, QAbstractItemView, QMessageBox
from PySide6.QtGui import QIcon, QPalette, QColor, Qt, QFont
from PySide6.QtCore import QSize

class FontBold(QFont):
    def __init__(self):
        super().__init__()
        self.setBold(True)

class Dialog(QDialog):
    def __init__(self, parent : QMainWindow):
        super().__init__(parent)
        self.returnValue = None
        self.setWindowTitle("Inventary")
        # para iconos
        icon = QIcon(r"src/icon.ico")
        self.setWindowIcon(icon)
        # valor de la ventana
        self.setFixedSize(QSize(600, 400))
        # agregamos un boton de aceptar y cancelar
        btn = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        self.btnDialog = QDialogButtonBox(btn)
        self.btnDialog.button(QDialogButtonBox.StandardButton.Save).setText("Add")
        self.btnDialog.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.GetItemSelected)
        self.btnDialog.rejected.connect(self.reject)
        # layout vertical
        layoutV = QVBoxLayout()
        layoutV.addWidget(self.LabelCentral())
        layoutV.addSpacing(10)
        # layoout combo, txt, btn
        layoutV.addLayout(self.Searching())
        # dataTable
        self.dataTable = self.Table()
        layoutV.addWidget(self.dataTable, alignment=Qt.AlignmentFlag.AlignHCenter)
        layoutV.addSpacing(20)
        layoutV.addWidget(self.btnDialog, alignment=Qt.AlignmentFlag.AlignHCenter)
        # empaquetar el layout
        self.setLayout(layoutV)

    # label central
    def LabelCentral(self):
        # label
        label = QLabel("List of Product")
        # modificar color
        palette = label.palette()
        palette.setColor(QPalette.WindowText, QColor("black"))
        label.setPalette(palette)
        # modificar el font
        font = label.font()
        font.setFamily("ROBOTO SANS-SERIF")
        font.setPointSize(16)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label
    
    # searching
    def Searching(self):
        # combo
        self.comboBox = QComboBox()
        self.comboBox.addItems(("id", "Name", "Quantity"))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox.setFixedWidth(75)
        self.comboBox.setCurrentIndex(0)
        # textBox
        self.textBox = QLineEdit()
        self.textBox.setPlaceholderText("Search product")
        self.textBox.setFocus()
        self.textBox.setFixedWidth(140)
        # btnSearching
        self.btnSearching = QPushButton("Search")
        self.btnSearching.setFixedWidth(70)
        icon = QIcon(r"src/search.ico").pixmap(60, 60)
        self.btnSearching.setIcon(icon)
        self.btnSearching.setAutoDefault(True)
        # layout horizontal
        layoutH = QHBoxLayout()
        widget = QWidget()
        widget.setFixedWidth(146)
        layoutH.addWidget(self.comboBox)
        layoutH.addWidget(self.textBox)
        layoutH.addWidget(self.btnSearching)
        layoutH.addWidget(widget)
        layoutH.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        return layoutH
    
    # table
    def Table(self):
        dataTable = QTableWidget(0, 3, self)
        headers = ["id", "Name", "Quantity"]
        dataTable.setHorizontalHeaderLabels(headers)
        dataTable.cellDoubleClicked.connect(self.GetItemSelected)
        dataTable.horizontalHeader().setFont(FontBold())
        dataTable.setSortingEnabled(True)
        dataTable.horizontalHeader().setSortIndicator(0, Qt.AscendingOrder)
        dataTable.verticalHeader().setVisible(False)
        dataTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        dataTable.horizontalHeader().setStretchLastSection(True)
        # width
        dataTable.setFixedWidth(450)
        dataTable.setColumnWidth(0, 90)
        dataTable.setColumnWidth(1, 240)
        dataTable.setColumnWidth(2, 90)
        dataTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        dataTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        return dataTable
    
    # get item for id
    def GetItemSelected(self):
        # get id
        if self.dataTable.selectedItems():
            id : int = self.dataTable.selectedIndexes()[0].data()
            name : str = self.dataTable.selectedIndexes()[1].data()
            self.close()
            self.returnValue = [id, name, int()]
        else:
            QMessageBox.warning(self,
                                "Warning",
                                "Please select a product to add to the list",
                                QMessageBox.StandardButton.Ok)
