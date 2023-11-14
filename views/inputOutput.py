from functools import partial
from typing import List, Union
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTableWidget, QAbstractItemView, QHBoxLayout, QLineEdit, QFormLayout, QTableWidgetItem, QMessageBox, QItemDelegate
from PySide6.QtCore import QSize, Qt, QMargins, Signal
from PySide6.QtGui import QIcon, QPalette, QColor, QFont, QIntValidator
from views.listProducts import Dialog
from controllers.inputOutputContr import Controller

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

class PositiveIntegerItemDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(PositiveIntegerItemDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        editor = super(PositiveIntegerItemDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            validator = QIntValidator(1, 999999)  # Valores entre 1 y 99999 (ajusta según tus necesidades)
            editor.setValidator(validator)
            return editor

# class of input window
class Component(QMainWindow):
    # atributos para los signal
    openPrincipal = Signal()
    # constructor
    def __init__(self, name : str, status : bool):
        self.listItem : List[Union[int, str]]= list()
        self.name = name
        self.status = status
        super().__init__()
        self.setWindowTitle("Inventary")
        # valor de la ventana
        self.resize(QSize(1066, 600))
        self.setMinimumSize(QSize(1066,600))
        # para iconos
        icon = QIcon(r"src/icon.ico")
        self.setWindowIcon(icon)
        # layout vertical
        layoutV = QVBoxLayout()
        layoutV.addWidget(self.LabelCentral())
        layoutV.addSpacing(20)
        layoutV.addLayout(self.LabelList())
        # datatable
        self.dataTable = self.Table()
        layoutV.addWidget(self.dataTable, alignment=Qt.AlignmentFlag.AlignHCenter)
        # layoutH for button
        layoutH = QHBoxLayout()
        # btnAdd
        self.btnAdd = self._Button("Add a Product", r"src/add.svg")
        self.btnAdd.setShortcut(Qt.CTRL | Qt.Key.Key_A)
        self.btnAdd.clicked.connect(self.OpenDialog)
        layoutH.addWidget(self.btnAdd)
        # btnDelete
        self.btnDelete = self._Button("Delete a Product", r"src/delete.svg")
        self.btnDelete.setShortcut(Qt.CTRL | Qt.Key.Key_D)
        self.btnDelete.clicked.connect(self.DeleteProduct)
        layoutH.addWidget(self.btnDelete)
        # btnSave
        self.btnSave = self._Button("Save this Record", r"src/save.svg")
        self.btnSave.clicked.connect(self.Validate)
        layoutH.addWidget(self.btnSave)
        layoutV.addLayout(layoutH)
        layoutV.addSpacing(30)
        # comment
        layoutV.addLayout(self.Comment())
        # btnExit
        self.btnExit = self._Button("Exit", r"src/exit.ico", 80, 80, 40)
        self.btnExit.clicked.connect(self.Exit)
        layoutV.addWidget(
            self.btnExit, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight
        )
        # container
        container = QWidget()
        container.setLayout(layoutV)
        self.setCentralWidget(container)

    # label central
    def LabelCentral(self):
        # label
        label = QLabel(self.name)
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
    
    # label list
    def LabelList(self):
        layoutH = QHBoxLayout()
        layoutH.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label = QLabel("List of products:")
        label.setFont(FontBold())
        widget = QWidget()
        widget.setFixedWidth(630)
        layoutH.addWidget(label)
        layoutH.addWidget(widget)
        return layoutH
    
    # table
    def Table(self):
        dataTable = QTableWidget(0, 3, self)
        headers = ["id", "Name", "Quantity"]
        dataTable.setHorizontalHeaderLabels(headers)
        dataTable.horizontalHeader().setFont(FontBold())
        dataTable.setSortingEnabled(True)
        dataTable.horizontalHeader().setSortIndicator(-1, Qt.AscendingOrder)
        dataTable.verticalHeader().setVisible(False)
        dataTable.horizontalHeader().setStretchLastSection(True)
        # width
        dataTable.setFixedWidth(750)
        dataTable.setColumnWidth(0, 130)
        dataTable.setColumnWidth(1, 480)
        dataTable.setColumnWidth(2, 130)
        delegate = PositiveIntegerItemDelegate(dataTable)
        dataTable.setItemDelegate(delegate)
        dataTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        return dataTable
    
    # button option
    def _Button(self, text: str = "hola", path: str = r"src/icon.ico", w=115, h=55, icon=40):
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
    
    # comment
    def Comment(self):
        self.txtComment = QLineEdit()
        self.txtComment.setFont(Font(11))
        self.txtComment.setFixedWidth(250)
        # label
        label = QLabel("Comment:")
        label.setFont(Font(11))
        # form layout
        layoutForm = QFormLayout()
        layoutForm.addRow(label, self.txtComment)
        return layoutForm
    
    # open dialog list products
    def OpenDialog(self):
        self.dialog = Dialog(self)
        Controller.LoadData(self.dialog.dataTable)
        self.dialog.btnSearching.clicked.connect(partial(Controller.SearchFilter, self.dialog))
        self.dialog.exec()
        self.UpdateQuantity()
        newItem = self.dialog.returnValue
        if newItem:
        # Verificar si el valor ya existe en las tuplas existentes usando filter y map
            exist = any(
                filter(lambda x: x[0] == newItem[0], self.listItem)
            )
            if not exist:
                self.listItem.append(newItem)
                self.loadDataSet()
            else:
                QMessageBox.warning(self,
                                    "Warning",
                                    "Sorry this product already exists in the list",
                                    QMessageBox.StandardButton.Ok)
    
    # loadData
    def loadDataSet(self):
        self.dataTable.setSortingEnabled(False)
        self.dataTable.setRowCount(len(self.listItem))
        for row, item in enumerate(self.listItem):
            # id
            id = QTableWidgetItem()
            id.setFont(Font(11))
            id.setData(Qt.DisplayRole, item[0])
            id.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            id.setFlags(id.flags() & ~Qt.ItemIsEditable)
            # name 
            name = QTableWidgetItem(item[1])
            name.setFont(Font(11))
            name.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            name.setFlags(name.flags() & ~Qt.ItemIsEditable)
            # quantity
            quantity = QTableWidgetItem()
            quantity.setFont(Font(11))
            if item[2] != 0:
                quantity.setData(Qt.DisplayRole, item[2])
            quantity.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            quantity.setFlags(quantity.flags() | Qt.ItemIsEditable)
            self.dataTable.setItem(row, 0, id) 
            self.dataTable.setItem(row, 1, name) 
            self.dataTable.setItem(row, 2, quantity) 
        self.dataTable.setSortingEnabled(True)

    # delete a product of list
    def DeleteProduct(self):
        if self.dataTable.selectedItems():
            self.UpdateQuantity()
            item = self.dataTable.selectedItems()[0]
            item = self.dataTable.item(item.row(), 0)
            id = int(item.text())
            returnValue = tuple(
                filter(lambda x : x[0] == id, self.listItem))
            self.listItem.remove(returnValue[0])
            self.loadDataSet()
        else:
            QMessageBox.warning(self,
                                "Warning",
                                "Please select the product to delete",
                                QMessageBox.StandardButton.Ok)
        
    # refill the list
    def UpdateQuantity(self):
        for row in range(self.dataTable.rowCount()):
            item = self.dataTable.item(row, 2)
            if not item.text() == "":
                self.listItem[row][2] = int(item.text())
    
    # validator to save
    def Validate(self):
        if not self.listItem:
            QMessageBox.critical(self,
                                 "Error",
                                 "The product list is empty",
                                 QMessageBox.StandardButton.Ok)
            return None
        for row in range(self.dataTable.rowCount()):
            item = self.dataTable.item(row, 2)
            if item.text() == "":
                QMessageBox.critical(self,
                                 "Error",
                                 "Some quantity is empty please check",
                                 QMessageBox.StandardButton.Ok)
                return None
        returnValue = QMessageBox.information(self,
                                 "Information",
                                 "Are you sure you want to save?",
                                 QMessageBox.StandardButton.Ok,
                                 QMessageBox.StandardButton.Cancel)
        
        if returnValue == QMessageBox.StandardButton.Ok:
            self.UpdateQuantity()
            Controller.SaveInDB(self, self.status)
    # method to exit
    def Exit(self):
        # logica para salir si la tabla tiene productos
        if self.listItem:
            returnValue = QMessageBox.information(self,
                                "Information",
                                "Are you sure you want to exit?",
                                QMessageBox.StandardButton.Yes,
                                QMessageBox.StandardButton.No)
            if returnValue == QMessageBox.StandardButton.Yes:
                self.openPrincipal.emit()
        else:
            self.openPrincipal.emit()