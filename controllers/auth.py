from PySide6.QtWidgets import QMainWindow
from views.principal import Principal

# controllers for login
class Authetication:
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
        # example change future
        if username == "admin" and password == "admin":
            obj.principal = Principal()
            obj.principal.show()
            obj.close()
            return None
        else:
            obj.message.setText("Error incorrect username or password")
            obj.message.setVisible(True)
            obj.username.setFocus()
            return None
