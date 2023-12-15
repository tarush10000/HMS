from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from database import Database, UserRole

class LoginUI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hospital Management System - Login')
        layout = QVBoxLayout()

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        self.role_label = QLabel('Select Role:')
        self.role_dropdown = QComboBox(self)
        self.role_dropdown.addItem("Doctor")
        self.role_dropdown.addItem("Receptionist")

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_dropdown)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        selected_role = self.role_dropdown.currentText()

        if not username or not password:
            self.show_error("Username and password are required.")
            return

        user_role = Database.validate_login(username, password)

        if user_role == UserRole.DOCTOR and selected_role == "Doctor":
            self.app.show_doctor_ui()
        elif user_role == UserRole.RECEPTIONIST and selected_role == "Receptionist":
            self.app.show_receptionist_ui()
        else:
            self.show_error("Invalid credentials or role selected.")

    def show_error(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.exec_()
