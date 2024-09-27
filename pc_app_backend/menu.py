from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from .utils import post, put, delete

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionar Menú")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.item_name = QLineEdit()
        self.item_name.setPlaceholderText("Nombre del Producto")
        layout.addWidget(self.item_name)

        self.item_price = QLineEdit()
        self.item_price.setPlaceholderText("Precio del Producto")
        layout.addWidget(self.item_price)

        self.add_item_button = QPushButton("Agregar Producto")
        self.add_item_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_item_button)

        self.update_item_button = QPushButton("Actualizar Producto")
        self.update_item_button.clicked.connect(self.update_item)
        layout.addWidget(self.update_item_button)

        self.delete_item_button = QPushButton("Eliminar Producto")
        self.delete_item_button.clicked.connect(self.delete_item)
        layout.addWidget(self.delete_item_button)

        self.setLayout(layout)

    def add_item(self):
        name = self.item_name.text().strip()
        price = self.item_price.text().strip()
        if not name or not price:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        data = {"name": name, "price": price}
        response = post("menu/add", data)
        if response.get("success"):
            QMessageBox.information(self, "Éxito", "Producto agregado con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo agregar el producto")

    def update_item(self):
        name = self.item_name.text().strip()
        price = self.item_price.text().strip()
        if not name or not price:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        data = {"name": name, "price": price}
        response = put(f"menu/update/{name}", data)
        if response.get("success"):
            QMessageBox.information(self, "Éxito", "Producto actualizado con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo actualizar el producto")

    def delete_item(self):
        name = self.item_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Error", "El nombre del producto es obligatorio")
            return

        response = delete(f"menu/delete/{name}")
        if response.get("success"):
            QMessageBox.information(self, "Éxito", "Producto eliminado con éxito")
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el producto")
