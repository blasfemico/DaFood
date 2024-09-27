import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from .utils import get

class StatsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estadísticas Financieras")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.show_stats_button = QPushButton("Mostrar Estadísticas")
        self.show_stats_button.clicked.connect(self.show_stats)
        layout.addWidget(self.show_stats_button)

        self.setLayout(layout)

    def show_stats(self):
        revenue = get("revenue/")
        order_count = get("order_count/")
        plt.bar(["Revenue"], [revenue["revenue"]])
        plt.show()