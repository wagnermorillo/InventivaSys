from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String, Column, func, Table
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

# clase base
class Base(DeclarativeBase):
    pass

# modelos de las bd
# tabla puente
RecordProduct = Table(
    # nombre de la tabla
    "RecordProduct",
    Base.metadata,
    Column("Record_id", ForeignKey("Records.id"), primary_key=True),
    Column("Product_id", ForeignKey("Products.id"), primary_key=True),
    Column("quantity", Integer)
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
    
    def __init__(self, name, description, quantity):
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
    comment: Mapped[str] = mapped_column(String(255))
    products: Mapped["Record"] = relationship(secondary=RecordProduct)
    create_at: Mapped[datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    isDeleted: Mapped[bool] = mapped_column(default=False)

    def __str__(self) -> str:
        return (
            f"id : {self.id}, "
            f"type : {self.type}, "
            f"comment: {self.comment},"
        )
    
    def __init__(self, type, comment):
        self.type = type
        self.comment = comment
