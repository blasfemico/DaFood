import asyncio
import websockets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class NotificationsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notificaciones")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.notifications_label = QLabel("Notificaciones:")
        layout.addWidget(self.notifications_label)

        self.setLayout(layout)
        asyncio.run(self.listen_notifications())

    async def listen_notifications(self):
        uri = "ws://localhost:8000/ws"
        async with websockets.connect(uri) as websocket:
            while True:
                message = await websocket.recv()
                self.notifications_label.setText(message)