from PySide6.QtWidgets import QDialog, QMainWindow, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QTextEdit, QDialogButtonBox, QDialogButtonBox
from PySide6.QtGui import QIcon, QPalette, QColor, Qt
from PySide6.QtCore import QSize

# este es el dialog 
class Dialog(QDialog):
    def __init__(self, parent : QMainWindow, title : str, name : str = None, description : str = None):
        super().__init__(parent)
        self.title = title
        self.name = name
        self.description = description
        self.setWindowTitle("Inventary")
        # para iconos
        icon = QIcon(r"src/icon.ico")
        self.setWindowIcon(icon)
        # valor de la ventana
        self.setFixedSize(QSize(300, 250))
        # agregamos un boton de aceptar y cancelar
        btn = QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        self.btnDialog = QDialogButtonBox(btn)
        self.btnDialog.rejected.connect(self.reject)
        # layout vertical
        layoutV = QVBoxLayout()
        layoutV.addWidget(self.LabelCentral())
        layoutV.addLayout(self.Form())
        layoutV.addWidget(self.btnDialog, alignment=Qt.AlignmentFlag.AlignHCenter)
        # empaquetar el layout
        self.setLayout(layoutV)

    # label central
    def LabelCentral(self):
        # label
        label = QLabel(self.title)
        # modificar color
        palette = label.palette()
        palette.setColor(QPalette.WindowText, QColor("black"))
        label.setPalette(palette)
        # modificar el font
        font = label.font()
        font.setFamily("ROBOTO SANS-SERIF")
        font.setPointSize(16)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label
    
    # form 
    def Form(self):
        # name
        self.txtName = QLineEdit()
        self.txtName.setText(self.name)
        self.txtName.setFixedWidth(200)
        # description
        self.txtDescription = QTextEdit()
        self.txtDescription.setText(self.description)
        self.txtDescription.setFixedSize(QSize(200,75))
        # layout
        layoutForm = QFormLayout()
        layoutForm.addRow("Name:", self.txtName)
        layoutForm.addRow("Description:", self.txtDescription)
        return layoutForm
    