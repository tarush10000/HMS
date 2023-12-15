from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from database import Database
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class ReceptionistUI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hospital Management System - Receptionist Dashboard')
        layout = QVBoxLayout()

        welcome_label = QLabel(f"Welcome, Receptionist {Database.get_receptionist_name()}")
        # Replace get_receptionist_name() with a method that retrieves the receptionist's name from the database

        patient_label = QLabel('Patient Registration:')
        patient_name_label = QLabel('Name:')
        patient_name_input = QLineEdit(self)
        patient_age_label = QLabel('Age:')
        patient_age_input = QLineEdit(self)
        patient_register_button = QPushButton('Register Patient')
        patient_register_button.clicked.connect(self.register_patient)

        logout_button = QPushButton('Logout')
        logout_button.clicked.connect(self.logout)

        layout.addWidget(welcome_label)
        layout.addWidget(patient_label)
        layout.addWidget(patient_name_label)
        layout.addWidget(patient_name_input)
        layout.addWidget(patient_age_label)
        layout.addWidget(patient_age_input)
        layout.addWidget(patient_register_button)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def register_patient(self):
        # Implement patient registration logic here
        # You can retrieve patient name and age from the corresponding QLineEdit widgets
        pass

    def logout(self):
        self.app.show_login_ui()
        self.close()
