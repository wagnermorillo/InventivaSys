from functools import partial
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from views.principal import Principal
from views.inputOutput import Component
from views.inventary import Inventary
from views.login import Componente
# controlador que se encarga de abrir y cerrar ventanas
class App:
    def __init__(self) -> None:
        # atributos
        self.app = QApplication([])
        self.input = Component()

    ########################################
    #           login
    #########################################
    # abiri el login
    def OpenLogin(self):
        self.login = Componente()
        self.login.openPrincipal.connect(self.LoginToPrincipal)
        self.login.show()

    # login to principal
    def LoginToPrincipal(self):
        self.principal = Principal()
        self.principal.openInput.connect(self.PrincipalToInput)
        self.principal.openExit.connect(partial(self.PrincipalToExit, self.principal))
        self.principal.openInventary.connect(self.PrincipalToInventary)
        self.principal.show()
        #                       self.login.close()
        self.login = None
     
    ########################################
    #           principal
    #########################################
    # principal to exit
    def PrincipalToExit(self, obj : QMainWindow):
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
    
    # de principal a input
    def PrincipalToInput(self):
        self.input = Component()
        self.input.show()
        self.principal.close()
        self.principal = None
    
    # de principal a inventary
    def PrincipalToInventary(self):
        self.inventary = Inventary()
        self.inventary.openPrincipal.connect(self.InventaryToPrincipal)
        self.inventary.show()
        #                self.principal.close()
        self.principal = None
    
    ########################################
    #           inventary
    #########################################
    # inventary to principal
    def InventaryToPrincipal(self):
        self.principal = Principal()
        self.principal.openInput.connect(self.PrincipalToInput)
        self.principal.openExit.connect(partial(self.PrincipalToExit, self.principal))
        self.principal.openInventary.connect(self.PrincipalToInventary)
        self.principal.show()
        self.inventary.close()
        self.inventary = None
    
    # run app
    def RunApp(self):
        self.PrincipalToInventary()
        sys.exit(self.app.exec())

# ejecutor de la aplicación
if __name__ == "__main__":
    # cuando se  ejecuta
    ventana = App()
    ventana.RunApp()