from PySide6.QtWidgets import QMainWindow

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
        # example change future
        if username == "admin" and password == "admin":
            # login to login
            obj.openPrincipal.emit()
        else:
            obj.message.setText("Error incorrect username or password")
            obj.message.setVisible(True)
            obj.username.setFocus()
            return None
