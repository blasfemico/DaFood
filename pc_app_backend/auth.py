from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from .utils import post_form

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 280, 100)
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

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.open_registration_page)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def handle_login(self):
        email = self.email.text().strip()
        password = self.password.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Both fields are required")
            return

        data = {"username": email, "password": password}
        response = post_form("users/login", data)

        if "access_token" in response:
            QMessageBox.information(self, "Success", "Login successful!")
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")

    def open_registration_page(self):
        # Open the registration page URL in the default web browser
        QDesktopServices.openUrl(QUrl("http://localhost:8081/register"))