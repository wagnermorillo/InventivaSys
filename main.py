import sys
from PySide6.QtWidgets import QApplication
from views.login import Componente
from views.principal import Principal

# ejecutor de la aplicación
if __name__ == "__main__":
    # cuando se  ejecuta
    app = QApplication([])
    ventana = Principal()
    ventana.show()
    # ejecutar la ventana
    sys.exit(app.exec())