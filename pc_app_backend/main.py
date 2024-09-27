import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from pc_app_backend.auth import LoginWindow
from pc_app_backend.tables import TablesWindow
from pc_app_backend.menu import MenuWindow
from pc_app_backend.stats import StatsWindow
from pc_app_backend.notifications import NotificationsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Bar/Restaurante")
        self.setGeometry(100, 100, 800, 600)

        self.login_window = LoginWindow()
        self.setCentralWidget(self.login_window)

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        login_action = QAction("Login", self)
        login_action.triggered.connect(self.show_login)
        file_menu.addAction(login_action)

        tables_action = QAction("Mesas y Sectores", self)
        tables_action.triggered.connect(self.show_tables)
        file_menu.addAction(tables_action)

        menu_action = QAction("Menú", self)
        menu_action.triggered.connect(self.show_menu)
        file_menu.addAction(menu_action)

        stats_action = QAction("Estadísticas", self)
        stats_action.triggered.connect(self.show_stats)
        file_menu.addAction(stats_action)

        notifications_action = QAction("Notificaciones", self)
        notifications_action.triggered.connect(self.show_notifications)
        file_menu.addAction(notifications_action)

    def show_login(self):
        self.login_window = LoginWindow()
        self.setCentralWidget(self.login_window)

    def show_tables(self):
        self.tables_window = TablesWindow()
        self.setCentralWidget(self.tables_window)

    def show_menu(self):
        self.menu_window = MenuWindow()
        self.setCentralWidget(self.menu_window)

    def show_stats(self):
        self.stats_window = StatsWindow()
        self.setCentralWidget(self.stats_window)

    def show_notifications(self):
        self.notifications_window = NotificationsWindow()
        self.setCentralWidget(self.notifications_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())