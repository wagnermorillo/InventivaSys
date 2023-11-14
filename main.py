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
        self.principal.openOutput.connect(self.PrincipalToOutput)
        self.principal.show()
        # esta
        #self.login.close()
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
        self.input = Component("Input", True)
        self.input.openPrincipal.connect(self.InputToPrincipal)
        self.input.show()
        self.principal.close()
        self.principal = None
    
    # de principal a output
    def PrincipalToOutput(self):
        self.output = Component("Output", False)
        self.output.openPrincipal.connect(self.OutputToPrincipal)
        self.output.show()
        self.principal.close()
        self.principal = None
    
    # de principal a inventary
    def PrincipalToInventary(self):
        self.inventary = Inventary()
        self.inventary.openPrincipal.connect(self.InventaryToPrincipal)
        self.inventary.show()
        # esta
        self.principal.close()
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
        self.principal.openOutput.connect(self.PrincipalToOutput)
        self.principal.show()
        self.inventary.close()
        self.inventary = None
    
    ########################################
    #           input
    #########################################
    # input to principal
    def InputToPrincipal(self):
        self.principal = Principal()
        self.principal.openInput.connect(self.PrincipalToInput)
        self.principal.openExit.connect(partial(self.PrincipalToExit, self.principal))
        self.principal.openInventary.connect(self.PrincipalToInventary)
        self.principal.openOutput.connect(self.PrincipalToOutput)
        self.principal.show()
        self.input.close()
        self.input = None
    
    ########################################
    #           output
    #########################################
    # output to principal
    def OutputToPrincipal(self):
        self.principal = Principal()
        self.principal.openInput.connect(self.PrincipalToInput)
        self.principal.openExit.connect(partial(self.PrincipalToExit, self.principal))
        self.principal.openInventary.connect(self.PrincipalToInventary)
        self.principal.openOutput.connect(self.PrincipalToOutput)
        self.principal.show()
        self.output.close()
        self.output = None
    
    # run app
    def RunApp(self):
        self.LoginToPrincipal()
        sys.exit(self.app.exec())

# ejecutor de la aplicación
if __name__ == "__main__":
    # cuando se  ejecuta
    ventana = App()
    ventana.RunApp()