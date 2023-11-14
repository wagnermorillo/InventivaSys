from datetime import datetime
from typing import Any, List, Type
from sqlalchemy import ForeignKey, Integer, String, Column, func, Table
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

# clase base
class Base(DeclarativeBase):
    pass

# modelos de las bd
# tabla puente
class RecordProduct(Base):
    # nombre de la tabla
    __tablename__ = "RecordProduct"
    # columna
    Product_id: Mapped[int] = mapped_column(ForeignKey("Products.id"), primary_key=True)
    Record_id: Mapped[int] = mapped_column(ForeignKey("Records.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(default=0)
    product: Mapped["Product"] = relationship()

    def __init__(self, product : Type["Product"], quantity : int):
        self.product = product
        self.quantity = quantity

    def __str__(self) -> str:
        return (
            f"Product_id : {self.Product_id}, "
            f"Record_id : {self.Record_id}, "
            f"quantity: {self.quantity},"
        )

# Products
class Product(Base):
    # nombre de la tabla
    __tablename__ = "Products"
    # columnas
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(String(255))
    quantity: Mapped[int] = mapped_column(default=0)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    isDeleted: Mapped[bool] = mapped_column(default=False)

    def __str__(self) -> str:
        return (
            f"id : {self.id}, "
            f"name : {self.name}, "
            f"description: {self.description},"
            f"quantity : {self.quantity}"
        )
    
    def __init__(self, name : str, description : str, quantity : int):
        self.name = name
        self.description = description
        self.quantity = quantity

# record
class Record(Base):
    # nombre de la tabla
    __tablename__ = "Records"
    # columnas
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[bool] = mapped_column()
    comment: Mapped[str] = mapped_column(String(255), nullable=True)
    products: Mapped[List["RecordProduct"]] = relationship()
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    isDeleted: Mapped[bool] = mapped_column(default=False)

    def __str__(self) -> str:
        return (
            f"id : {self.id}, "
            f"type : {self.type}, "
            f"comment: {self.comment}"
        )
    
    def __init__(self, type : bool, comment : str):
        self.type = type
        self.comment = comment

