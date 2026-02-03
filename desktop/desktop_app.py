import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QFileDialog, QMessageBox
)

API_URL = "http://127.0.0.1:8000/api/upload/"

class ChemicalEquipmentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setGeometry(300, 200, 400, 350)

        self.layout = QVBoxLayout()

        self.title = QLabel("<h2>Chemical Equipment Visualizer</h2>")
        self.layout.addWidget(self.title)

        self.file_label = QLabel("No file selected")
        self.layout.addWidget(self.file_label)

        self.select_btn = QPushButton("Select CSV File")
        self.select_btn.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_btn)

        self.upload_btn = QPushButton("Upload & Analyze")
        self.upload_btn.clicked.connect(self.upload_file)
        self.layout.addWidget(self.upload_btn)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
        self.file_path = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )
        if file_path:
            self.file_path = file_path
            self.file_label.setText(f"Selected: {file_path.split('/')[-1]}")

    def upload_file(self):
        if not self.file_path:
            QMessageBox.warning(self, "Error", "Please select a CSV file first")
            return

        try:
            with open(self.file_path, "rb") as f:
                response = requests.post(
                    API_URL,
                    files={"file": f}
                )

            if response.status_code != 200:
                QMessageBox.critical(self, "Error", "Failed to analyze file")
                return

            data = response.json()
            result_text = (
                f"Total Equipment: {data['total_equipment']}\n"
                f"Avg Flowrate: {data['avg_flowrate']}\n"
                f"Avg Pressure: {data['avg_pressure']}\n"
                f"Avg Temperature: {data['avg_temperature']}"
            )
            self.result_label.setText(result_text)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChemicalEquipmentApp()
    window.show()
    sys.exit(app.exec_())
