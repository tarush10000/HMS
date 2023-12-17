from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QDesktopWidget, QStyle
from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtCore import Qt, QObject
from database import Database
import sys, os
from doctor_ui import DoctorUI
from styles import heading_font, heading_text_color


class LoginUI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setFixedSize(1440, 1024)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Set up the widget to contain the form elements
        form_widget = QWidget()
        form_widget.setStyleSheet("background-image: url(design/images/login_bg.png);")
        form_widget.setContentsMargins(0, 0, 0, 0)

        # Set up the form layout
        form_layout = QVBoxLayout(form_widget)
        form_layout.setAlignment(Qt.AlignCenter)

        # Create a nested widget to enclose the form elements
        nested_widget = QWidget()
        nested_widget.setStyleSheet("border-radius: 20px; padding: 20px;")
        nested_widget.setContentsMargins(10, 10, 10, 20)

        # Set up the layout for the nested widget
        nested_layout = QVBoxLayout(nested_widget)
        nested_layout.setAlignment(Qt.AlignCenter)

        # Form elements
        self.login_heading = QLabel('LOGIN INTO YOUR ACCOUNT')
        self.login_heading.setFont(heading_font)
        self.login_heading.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText('Username')
        self.username_input.setStyleSheet("color: rgb(0, 0, 0); font: 10pt \"Poppins\"; border: 1px solid rgb(0, 0, 0); border-radius: 20px; padding: 5px;")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setStyleSheet("color: rgb(0, 0, 0); font: 10pt \"Poppins\"; border: 1px solid rgb(0, 0, 0); border-radius: 20px; padding: 5px;")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login')
        self.login_button.setStyleSheet(
            "color: rgb(67, 79, 194);"
            "font: 10pt \"Poppins\";"
            "border: 1px solid rgb(67, 79, 194);"
            "border-radius: 20px;"
            "padding: 5px;"
            "max-width: 150px;"
        )
        self.setAutoFillBackground(True)

        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.setFlat(True)
        self.login_button.setFixedHeight(40)
        self.login_button.clicked.connect(self.login)

        # Add form elements to the nested widget
        nested_layout.addWidget(self.login_heading)
        nested_layout.addWidget(self.username_input)
        nested_layout.addWidget(self.password_input)
        nested_layout.addWidget(self.login_button)

        # Set the margins for the nested widget
        nested_layout.setContentsMargins(0, 0, 0, 0)

        # Add the nested widget to the form layout
        form_layout.addWidget(nested_widget)
        form_layout.setContentsMargins(int(0.3 * self.width()), int(0.05 * self.height()), int(0.3 * self.width()), 0)

        # Set up the main layout for the whole screen
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(form_widget)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            self.show_error("Username and password are required.")
            return
        db = Database()
        user_ver = db.validate_login(username, password)
        del db
        if user_ver == 'doctor':
            self.show_doctor_ui()
        elif user_ver == 'receptionist':
            self.show_receptionist_ui()
        else:
            self.show_error("Invalid credentials")

    def show_error(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_MessageBoxCritical')))
        error_box.setStyleSheet(
                    "QMessageBox {"
                    "background-color: #F2F2F2;"
                    "}"
                    "QMessageBox QLabel {"
                    "color: #333333;"
                    "font-size: 14px;"
                    "}"
                    "QMessageBox QPushButton {"
                    "background-color: #007ACC;"
                    "color: white;"
                    "border: 1px solid #007ACC;"
                    "border-radius: 10px;"
                    "width: 100px;"
                    "height: 30px;"
                    "}"
                    "QMessageBox QPushButton:hover {"
                    "background-color: #005EAD;"
                    "}"
                )
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.exec_()

    def show_doctor_ui(self):
        self.close()
        self.doctor_ui = DoctorUI(self.app)
        self.doctor_ui.show()

if __name__ == '__main__':
    app = QApplication([])
    login_ui = LoginUI(None)
    login_ui.show()
    app.exec_()
