from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.input import Input
# class controllers of Principal (Menu)
class Controller:
    # method exit
    @staticmethod
    def Exit(obj : QMainWindow):
        dialog = QMessageBox(obj)
        dialog.setWindowTitle("Dialog")
        dialog.setText("Are you sure you want to exit?")
        # agregar los botones de las respuestas 
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.No)
        # agregar un icono
        dialog.setIcon(QMessageBox.Question)
        returnValue = dialog.exec()        
        if returnValue == QMessageBox.StandardButton.Yes:
            obj.close()
            return None
        return None
    
    # method input
    @staticmethod
    def Input(obj : QMainWindow):
        obj.input = Input()
        obj.input.show()
        obj.close()
        return None