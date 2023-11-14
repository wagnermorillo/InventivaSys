from models.models import *
from models.db import session

products = session.query(Product).filter(Product.isDeleted == False).limit(3).all()
print(products[0])

record = Record(True, "Prueba #2")
for product in products:
    record.products.append(RecordProduct(product, 10))

session.add(record)
session.commit()
print("se guardo")


