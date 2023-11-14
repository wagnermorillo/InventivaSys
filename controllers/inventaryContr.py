from typing import List
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from sqlalchemy import String, and_
from sqlalchemy.exc import IntegrityError
from models.models import Product
from models.db import session

# font
class Font(QFont):
    def __init__(self, n: int):
        super().__init__()
        self.setPointSize(n)
        self.setBold(False)

# controller of inventary
class Controller:
    # load data
    @staticmethod
    def LoadData(dataTable : QTableWidget, dataset : List[Product] = None):
        # si no se pasa el dataset se crea uno
        if dataset is None:
            dataset = session.query(Product).filter(Product.isDeleted == False).order_by(Product.id).all()
        # rellenar el datatable
        dataTable.setRowCount(int(len(dataset)))
        for row ,item in enumerate(dataset):
            # id
            id = QTableWidgetItem()
            id.setData(Qt.DisplayRole, item.id)
            id.setFont(Font(11))
            id.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # name
            name = QTableWidgetItem(item.name)
            name.setFont(Font(11))
            name.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # description
            description = QTableWidgetItem(item.description)
            description.setFont(Font(11))
            description.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # quantity
            quantity = QTableWidgetItem()
            quantity.setData(Qt.DisplayRole, item.quantity)
            quantity.setFont(Font(11))
            quantity.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # insert
            dataTable.setItem(row, 0, id)
            dataTable.setItem(row, 1, name)
            dataTable.setItem(row, 2, description)
            dataTable.setItem(row, 3, quantity)

    # filter
    @staticmethod
    def SearchFilter(obj : QMainWindow):
        index = obj.comboBox.currentIndex()
        filterText = obj.textBox.text().strip()

        # switch case
        match(index):
            # index
            case 0:
                products = session.query(Product).filter(and_(
                    Product.isDeleted == False,
                    Product.id.cast(String).ilike(f"%{filterText}%")
                )).order_by(Product.id).all()
                Controller.LoadData(obj.dataTable, products)
                return None

            # name
            case 1:
                products = session.query(Product).filter(and_(
                    Product.isDeleted == False,
                    Product.name.ilike(f"%{filterText}%")
                )).order_by(Product.id).all()
                Controller.LoadData(obj.dataTable, products)
                return None
            
            # description
            case 2:
                products = session.query(Product).filter(and_(
                    Product.isDeleted == False,
                    Product.description.ilike(f"%{filterText}%")
                )).order_by(Product.id).all()
                Controller.LoadData(obj.dataTable, products)
                return None
            
            # quantity
            case 3:
                products = session.query(Product).filter(and_(
                    Product.isDeleted == False,
                    Product.quantity.cast(String).ilike(f"%{filterText}%")
                )).order_by(Product.id).all()
                Controller.LoadData(obj.dataTable, products)
                return None
            
            # default
            case _:
                return None

    # create/update product
    @staticmethod
    def CreateUpdate(dialog : QDialog, status : bool, id : int = None):
        # recolectar los campos del dialog
        name = dialog.txtName.text().strip()
        description = dialog.txtDescription.toPlainText().strip()
        # si el true es create
        if status:
            product = Product(name, description, 0)
            session.add(product)
            try:
                session.commit()
                QMessageBox.information(
                    dialog,
                    "Information",
                    "The product was added successfully",
                    QMessageBox.StandardButton.Ok
                )
                dialog.close()
                return None
            except IntegrityError:
                session.rollback()
                QMessageBox.critical(
                    dialog, 
                    "Error",
                    "There is already a product with this name",
                    QMessageBox.StandardButton.Ok
                    )
                return None
        # en caso de false es update
        else:
            product = session.query(Product).get(id)
            try:
                product.name = name
                product.description = description
                session.commit()
                formato_deseado = "%d/%m/%Y %I:%M %p"
                time = product.update_at.strftime(formato_deseado)
                print(time)
                QMessageBox.information(
                    dialog,
                    "Information",
                    "The product was edited successfully",
                    QMessageBox.StandardButton.Ok
                )
                dialog.close()
                return None
            except IntegrityError:
                session.rollback()
                QMessageBox.critical(
                    dialog, 
                    "Error",
                    "There is already a product with this name",
                    QMessageBox.StandardButton.Ok
                    )
                return None
            
    # delete a product
    @staticmethod
    def Delete(obj : QMainWindow,id : int):
        dialog = QMessageBox(obj)
        dialog.setWindowTitle("Warning")
        dialog.setText("Are you sure you want delete this product?")
        # agregar los botones de las respuestas 
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        # agregar un icono
        dialog.setIcon(QMessageBox.Warning)
        returnValue = dialog.exec()        
        if returnValue == QMessageBox.StandardButton.Yes:
            product = session.query(Product).get(id)
            product.isDeleted = True
            session.commit()
            Controller.LoadData(obj.dataTable)
            QMessageBox.information(
                        obj,
                        "Information",
                        "The product was deleted successfully",
                        QMessageBox.StandardButton.Ok
            )