from typing import List
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from sqlalchemy import String, and_
from sqlalchemy.exc import IntegrityError
from models.models import Record
from models.db import session


# font
class Font(QFont):
    def __init__(self, n: int):
        super().__init__()
        self.setPointSize(n)
        self.setBold(False)

# controller of history
class Controller:
    # load data
    @staticmethod
    def LoadData(dataTable : QTableWidget, dataset : List[Record] = None):
        # si no se pasa el dataset se crea uno
        if dataset is None:
            dataset = session.query(Record).filter(Record.isDeleted == False).order_by(Record.id).all()
        # rellenar el datatable
        dataTable.setRowCount(int(len(dataset)))
        for row ,item in enumerate(dataset):
            # id
            id = QTableWidgetItem()
            id.setData(Qt.DisplayRole, item.id)
            id.setFont(Font(11))
            id.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # Type
            type = QTableWidgetItem()
            type.setFont(Font(11))
            type.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            if item.type:
                type.setText("Input")
            else:
                type.setText("Output")
            # comment
            comment = QTableWidgetItem(item.comment)
            comment.setFont(Font(11))
            comment.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # createAt
            createAt = QTableWidgetItem(item.create_at.strftime("%d/%m/%Y %I:%M %p"))
            createAt.setFont(Font(11))
            createAt.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # insert
            dataTable.setItem(row, 0, id)
            dataTable.setItem(row, 1, type)
            dataTable.setItem(row, 2, comment)
            dataTable.setItem(row, 3, createAt)
    
    # load data detail
    @staticmethod
    def LoadDataDetail(dataTable : QTableWidget, id : int, dataset : List[Record] = None):
        # si no se pasa el dataset se crea uno
        if dataset is None:
            dataset = session.query(Record).get(id).products
        # rellenar el datatable
        dataTable.setRowCount(int(len(dataset)))
        for row ,item in enumerate(dataset):
            # id
            id = QTableWidgetItem()
            id.setData(Qt.DisplayRole, item.Product_id)
            id.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # name
            name = QTableWidgetItem(item.product.name)
            name.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # quantity
            quantity = QTableWidgetItem()
            quantity.setData(Qt.DisplayRole, item.quantity)
            quantity.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # insert
            dataTable.setItem(row, 0, id)
            dataTable.setItem(row, 1, name)
            dataTable.setItem(row, 2, quantity)
    
    # filter
    @staticmethod
    def SearchFilter(obj : QMainWindow):
        index = obj.comboBox.currentIndex()
        filterText = obj.textBox.text().strip()

        # switch case
        match(index):
            # index
            case 0:
                records = session.query(Record).filter(and_(
                    Record.isDeleted == False,
                    Record.id.cast(String).ilike(f"%{filterText}%")
                )).order_by(Record.id).all()
                Controller.LoadData(obj.dataTable, records)
                return None
            
            # description
            case 1:
                records = session.query(Record).filter(and_(
                    Record.isDeleted == False,
                    Record.comment.ilike(f"%{filterText}%")
                )).order_by(Record.id).all()
                Controller.LoadData(obj.dataTable, records)
                return None
            
            # default
            case _:
                return None