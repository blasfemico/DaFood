from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from .utils import post

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 280, 80)
        layout = QVBoxLayout()

        self.label = QLabel("Email:")
        layout.addWidget(self.label)
        self.email = QLineEdit()
        layout.addWidget(self.email)

        self.label = QLabel("Password:")
        layout.addWidget(self.label)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        self.button = QPushButton("Login")
        self.button.clicked.connect(self.handle_login)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def handle_login(self):
        email = self.email.text()
        password = self.password.text()
        response = post("users/login", {"email": email, "password": password})
        if "access_token" in response:
            QMessageBox.information(self, "Success", "Login successful!")
            # Redirigir a la pantalla principal
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")