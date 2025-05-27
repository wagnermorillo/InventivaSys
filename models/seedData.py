from sqlalchemy.orm import Session
from .models import Product, Record, RecordProduct

def SeedData(session):
    # Verifica si ya existen productos
    if not session.query(Product).first():
        productos = [
            Product(name="Outdoor Adventure Kit", description="Kit de aventura al aire libre", quantity=20),
            Product(name="Granulated Sugar", description="Azúcar granulada refinada", quantity=100),
            Product(name="Digital Thermostat", description="Termostato digital inteligente", quantity=15),
            Product(name="Sriracha Honey Glaze", description="Glaseado de miel y sriracha", quantity=40),
            Product(name="Fitness Balance Ball", description="Pelota de balance para ejercicios", quantity=25),
            Product(name="Car Phone Mount", description="Soporte para celular de auto", quantity=60),
            Product(name="Wire Shelving Unit", description="Estantería metálica de 4 niveles", quantity=10),
            Product(name="Mechanical Pencil Set", description="Set de lápices mecánicos", quantity=80),
            Product(name="Dish Rack", description="Escurridor de platos cromado", quantity=35),
            Product(name="Sweet Corn Fritters", description="Tortitas de maíz dulce listas para freír", quantity=50)
        ]
        session.add_all(productos)
        session.commit()

    # Verifica si ya existen registros
    if not session.query(Record).first():
        record = Record(type=True, comment="Ingreso inicial de productos")
        session.add(record)
        session.commit()
        print("Registro inicial insertado.")

    # Obtener productos y registro
    productos = session.query(Product).all()
    record = session.query(Record).first()

    # Vincular productos al registro
    for producto in productos:
        existe = session.query(RecordProduct).filter_by(Product_id=producto.id, Record_id=record.id).first()
        if not existe:
            rp = RecordProduct(product=producto, quantity=5)
            rp.Record_id = record.id
            session.add(rp)

    session.commit()
