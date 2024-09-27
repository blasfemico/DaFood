from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QLineEdit, QDialog, QDialogButtonBox, QMessageBox
from .utils import get, post

class AddSectorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Añadir Sector")
        self.setGeometry(100, 100, 280, 80)
        layout = QVBoxLayout()

        self.label = QLabel("Nombre del Sector:")
        layout.addWidget(self.label)
        self.sector_name = QLineEdit()
        layout.addWidget(self.sector_name)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_sector_name(self):
        return self.sector_name.text()

class TablesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Mesas y Sectores")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.sector_list = QListWidget()
        layout.addWidget(self.sector_list)

        self.add_sector_button = QPushButton("Añadir Sector")
        self.add_sector_button.clicked.connect(self.add_sector)
        layout.addWidget(self.add_sector_button)

        self.setLayout(layout)
        self.load_sectors()

    def load_sectors(self):
        sectors = get("sectores/get_sectores")
        for sector in sectors:
            self.sector_list.addItem(sector["nombre"])

    def add_sector(self):
        dialog = AddSectorDialog()
        if dialog.exec_() == QDialog.Accepted:
            sector_name = dialog.get_sector_name()
            response = post("sectores/create_sectores", {"nombre": sector_name})
            if "id" in response:
                self.sector_list.addItem(response["nombre"])
            else:
                QMessageBox.warning(self, "Error", "No se pudo añadir el sector")