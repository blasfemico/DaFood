from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from .utils import post, get, put, delete

class TablesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionar Mesas y Sectores")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.sector_name = QLineEdit()
        self.sector_name.setPlaceholderText("Nombre del Sector")
        layout.addWidget(self.sector_name)

        self.add_sector_button = QPushButton("Agregar Sector")
        self.add_sector_button.clicked.connect(self.add_sector)
        layout.addWidget(self.add_sector_button)

        self.update_sector_button = QPushButton("Actualizar Sector")
        self.update_sector_button.clicked.connect(self.update_sector)
        layout.addWidget(self.update_sector_button)

        self.delete_sector_button = QPushButton("Eliminar Sector")
        self.delete_sector_button.clicked.connect(self.delete_sector)
        layout.addWidget(self.delete_sector_button)

        self.table_number = QLineEdit()
        self.table_number.setPlaceholderText("Número de Mesa")
        layout.addWidget(self.table_number)

        self.add_table_button = QPushButton("Agregar Mesa")
        self.add_table_button.clicked.connect(self.add_table)
        layout.addWidget(self.add_table_button)

        self.update_table_button = QPushButton("Actualizar Mesa")
        self.update_table_button.clicked.connect(self.update_table)
        layout.addWidget(self.update_table_button)

        self.delete_table_button = QPushButton("Eliminar Mesa")
        self.delete_table_button.clicked.connect(self.delete_table)
        layout.addWidget(self.delete_table_button)

        self.setLayout(layout)

    def add_sector(self):
        name = self.sector_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Error", "El nombre del sector es obligatorio")
            return

        data = {"nombre": name}
        response = post("sectores/create_sectores", data)
        if "id" in response:
            QMessageBox.information(self, "Éxito", "Sector agregado con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo agregar el sector")

    def update_sector(self):
        name = self.sector_name.text().strip()
        sector_id = self.get_sector_id(name)
        if not name or not sector_id:
            QMessageBox.warning(self, "Error", "El nombre del sector es obligatorio")
            return

        data = {"nombre": name}
        response = put(f"sectores/{sector_id}/update_sector", data)
        if "id" in response:
            QMessageBox.information(self, "Éxito", "Sector actualizado con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar el sector")

    def delete_sector(self):
        name = self.sector_name.text().strip()
        sector_id = self.get_sector_id(name)
        if not name or not sector_id:
            QMessageBox.warning(self, "Error", "El nombre del sector es obligatorio")
            return

        response = delete(f"sectores/{sector_id}/delete_sector")
        if response.get("success"):
            QMessageBox.information(self, "Éxito", "Sector eliminado con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el sector")

    def add_table(self):
        number = self.table_number.text().strip()
        sector_id = self.get_sector_id()
        if not number or not sector_id:
            QMessageBox.warning(self, "Error", "El número de la mesa y el sector son obligatorios")
            return

        data = {"numero": number}
        response = post(f"sectores/{sector_id}/create_mesas", data)
        if "id" in response:
            QMessageBox.information(self, "Éxito", "Mesa agregada con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo agregar la mesa")

    def update_table(self):
        number = self.table_number.text().strip()
        sector_id = self.get_sector_id()
        if not number or not sector_id:
            QMessageBox.warning(self, "Error", "El número de la mesa y el sector son obligatorios")
            return

        data = {"numero": number}
        response = put(f"sectores/{sector_id}/update_mesas/{number}", data)
        if response.get("success"):
            QMessageBox.information(self, "Éxito", "Mesa actualizada con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar la mesa")

    def delete_table(self):
        number = self.table_number.text().strip()
        sector_id = self.get_sector_id()
        if not number or not sector_id:
            QMessageBox.warning(self, "Error", "El número de la mesa y el sector son obligatorios")
            return

        response = delete(f"sectores/{sector_id}/delete_mesas/{number}")
        if response.get("success"):
            QMessageBox.information(self, "Éxito", "Mesa eliminada con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar la mesa")

    def get_sector_id(self, sector_name):
        # Implementa la lógica para obtener el ID del sector basado en el nombre del sector
        # Esto puede implicar una llamada a la API para obtener los sectores y encontrar el ID correspondiente
        response = get("sectores/get_sectores")
        if isinstance(response, list):
            for sector in response:
                if sector.get("nombre") == sector_name:
                    return sector.get("id")
        return None