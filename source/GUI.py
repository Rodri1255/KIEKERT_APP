## IMPORT STATEMENTS
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel, QFormLayout, QComboBox
)
from PySide6.QtCore import Qt
import fase1
import fase2
import fase3
import pandas as pd

## MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Proyecto Kiekert')
        self.setGeometry(300, 100, 600, 400)

        ## MAIN WIDGET
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)


        ## LOADING THE EXCEL FILE
        self.label_file = QLabel('Step 1: Select Excel File')
        self.label_file.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_file)

        self.load_button = QPushButton('Select Excel File')
        self.load_button.clicked.connect(self.load_excel_file)
        self.layout.addWidget(self.load_button)

        ## SHEET NAMES AS DROPDOWNS LOADED WITH THE FILE
        self.label_sheets = QLabel('Step 2: Select Sheets for each stage:')
        self.label_sheets.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_sheets)

        self.form_layout = QFormLayout()
        self.sheet_dropdown_fase1 = QComboBox()
        self.sheet_dropdown_fase2 = QComboBox()
        self.sheet_dropdown_fase3 = QComboBox()
        self.sheet_dropdown_write = QComboBox()


    def load_excel_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, 'Select an Excel file', "", "Excel Files (*.xlsx)")
        if self.file_path:
            try:
                excel_file = pd.ExcelFile(self.file_path)
                availablesheets = excel_file.sheet_names

                self.sheet_dropdown_fase1.addItems(availablesheets)
                self.sheet_dropdown_fase2.addItems(availablesheets)
                self.sheet_dropdown_fase3.addItems(availablesheets)
                self.sheet_dropdown_write.addItems(availablesheets)

                self.label_file.setText(f'Selected File: {self.file_path}')
                self.submit_sheets_button.setEnabled(True)
            except Exception as e:
                self.label_file.setText(f"Error reading Excel file: {str(e)}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()