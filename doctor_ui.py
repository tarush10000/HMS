from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from database import Database
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class DoctorUI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hospital Management System - Doctor Dashboard')
        layout = QVBoxLayout()

        welcome_label = QLabel(f"Welcome, Doctor {Database.get_doctor_name()}")
        # Replace get_doctor_name() with a method that retrieves the doctor's name from the database

        logout_button = QPushButton('Logout')
        logout_button.clicked.connect(self.logout)

        layout.addWidget(welcome_label)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def logout(self):
        self.app.show_login_ui()
        self.close()
