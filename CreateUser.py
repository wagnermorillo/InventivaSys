from models.models import Product, User
from models.db import session

user = User.create_user(session, "admin", "admin")
print(user)