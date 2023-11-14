from typing import List, Type
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from sqlalchemy import String, and_
from sqlalchemy.exc import IntegrityError
from models.models import Product, Record, RecordProduct
from models.db import session

# class controllers
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
            id.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            # name
            name = QTableWidgetItem(item.name)
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
            
            # quantity
            case 2:
                products = session.query(Product).filter(and_(
                    Product.isDeleted == False,
                    Product.quantity.cast(String).ilike(f"%{filterText}%")
                )).order_by(Product.id).all()
                Controller.LoadData(obj.dataTable, products)
                return None
            
            # default
            case _:
                return None
            
    # save in DB
    @staticmethod
    def SaveInDB(obj : Type[QMainWindow], status : bool):
        listID = tuple((x[0] for x in obj.listItem))
        listOrder = sorted(obj.listItem, key= lambda x : x[0])
        listQuantity = tuple((x[2] for x in listOrder))
        comment = obj.txtComment.text()
        # si es true es input
        if status:
            # obtener el listado de los productos por id
            products = session.query(Product).filter(
                Product.id.in_(listID)
            ).order_by(Product.id).all()
            # instanciar un record
            record = Record(status, comment)
            # recorrer ordenados los productos con su respectiva cantidad
            for product, quantity in zip(products, listQuantity):
                # agregar a tabla puente
                record.products.append(RecordProduct(product, quantity))
                # actualizar la nueva cantidad existente
                product.quantity += quantity
            
            # guardar 
            session.add(record)
            session.commit()
            QMessageBox.information(obj,
                                    "Information",
                                    "The record was successfully saved",
                                    QMessageBox.StandardButton.Ok)
            obj.listItem = list()
            obj.loadDataSet()
        
        # si es false es output
        else:
            # obtener el listado de los productos por id
            products = session.query(Product).filter(
                Product.id.in_(listID)
            ).order_by(Product.id).all()
            # instanciar un record
            record = Record(status, comment)
            # recorrer ordenados los productos con su respectiva cantidad
            for product, quantity in zip(products, listQuantity):
                # agregar a tabla puente
                record.products.append(RecordProduct(product, quantity))
                # verificar que la cantidad a restar es menor que la actual
                if quantity > product.quantity:
                    QMessageBox.critical(obj,
                                         "Error",
                                         f"{product.name}, Output quantity is greater than stock quantity",
                                         QMessageBox.StandardButton.Ok)
                    return None
            # guardar 
            session.add(record)
            session.commit()
            QMessageBox.information(obj,
                                    "Information",
                                    "The record was successfully saved",
                                    QMessageBox.StandardButton.Ok)
            obj.listItem = list()
            obj.loadDataSet()

                
