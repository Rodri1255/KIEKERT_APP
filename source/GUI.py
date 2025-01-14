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
        self.layout.addWidget(self.label_sheets)

        self.form_layout = QFormLayout()
        self.sheet_dropdown_fase1 = QComboBox()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()