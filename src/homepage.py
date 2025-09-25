from PyQt5.QtWidgets import QWidget, QLabel

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel("Welcome to Mine Planner 🚀", self)
        self.label.setGeometry(50, 50, 400, 40)