import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from homepage import HomePage  # Import HomePage


class MinePlanner(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mine Planning Software")
        self.setGeometry(200, 200, 1000, 700)

        # Set HomePage as central widget
        self.home_page = HomePage(self)
        self.setCentralWidget(self.home_page)

        self._createMenuBar()

    def _createMenuBar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        import_action = QAction("Import Data", self)
        import_action.triggered.connect(self.import_data)
        file_menu.addAction(import_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def import_data(self):
        file_dialog = QFileDialog.getOpenFileName(self, "Select a Data File", "", "All Files (*.*)")
        if file_dialog[0]:
            data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
            os.makedirs(data_folder, exist_ok=True)
            dest_path = os.path.join(data_folder, os.path.basename(file_dialog[0]))
            shutil.copy(file_dialog[0], dest_path)
            self.home_page.label.setText(f"Imported: {dest_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinePlanner()
    window.show()
    sys.exit(app.exec_())
