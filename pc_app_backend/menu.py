from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
from .utils import get, post
from PyQt5.QtWidgets import QMessageBox

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión del Menú")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.menu_list = QListWidget()
        layout.addWidget(self.menu_list)

        self.add_item_button = QPushButton("Añadir Plato")
        self.add_item_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_item_button)

        self.setLayout(layout)
        self.load_menu()

    def load_menu(self):
        menu_items = get("menu_items/")
        if isinstance(menu_items, list):
            for item in menu_items:
                if isinstance(item, dict) and "name" in item:
                    self.menu_list.addItem(item["name"])
                else:
                    QMessageBox.warning(self, "Error", "Formato de elemento de menú inválido")
        else:
            QMessageBox.warning(self, "Error", "Respuesta de la API inválida")

    def add_item(self):
        # Lógica para añadir un plato
        pass