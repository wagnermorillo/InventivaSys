from PySide6.QtWidgets import QMainWindow
from models.models import User
from models.db import session

# controllers for login
class Authetication:
    # atributos
    # auth of user
    @staticmethod
    def auth(obj: QMainWindow) -> None:
        username = obj.username.text()
        password = obj.password.text()
        # if the textbox is empty
        if not username or not password:
            obj.message.setText("Please fill out the fields!")
            obj.message.setVisible(True)
            obj.username.setFocus()
            return None
        auth = User.authenticate(session, username, password)
        if auth:
            # login to principal
            obj.openPrincipal.emit()
        else:
            obj.message.setText("Error incorrect username or password")
            obj.message.setVisible(True)
            obj.username.setFocus()
            return None
