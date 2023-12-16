from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QDesktopWidget
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt
from database import Database
from styles import heading_font

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
        form_widget.setStyleSheet("background-image: url(design/images/login_bg.png); background-repeat: no-repeat; background-position: center; background-color: rgb(255, 255, 255);")
        form_widget.setContentsMargins(0, 0, 0, 0)
        # Set up the form layout
        form_layout = QVBoxLayout(form_widget)
        form_layout.setAlignment(Qt.AlignCenter)
        
        # Create a nested widget to enclose the form elements
        nested_widget = QWidget()
        nested_widget.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 20px; padding: 20px;")

        # Set up the layout for the nested widget
        nested_layout = QVBoxLayout(nested_widget)
        nested_layout.setAlignment(Qt.AlignCenter)

        # Form elements
        self.login_heading = QLabel('LOGIN INTO YOUR ACCOUNT')
        self.login_heading.setFont(heading_font)
        self.login_heading.setAlignment(Qt.AlignCenter)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText('Username')
        self.username_input.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 10pt \"Poppins\"; border: 1px solid rgb(0, 0, 0); border-radius: 20px; padding: 5px;")
        self.username_input.setFixedWidth(int(0.3 * self.width()))

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font: 10pt \"Poppins\"; border: 1px solid rgb(0, 0, 0); border-radius: 20px; padding: 5px;")
        self.password_input.setFixedWidth(int(0.3 * self.width()))
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login')
        self.login_button.setStyleSheet("background-color: rgb(67, 79, 194); color: rgb(255, 255, 255); font: 10pt \"Poppins\"; border-radius: 20px; padding: 5px; max-width: 150px;")
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

        user_ver = Database.validate_login(self.app, username, password)

        if user_ver == 'doctor':
            self.app.show_doctor_ui()
        elif user_ver == 'receptionist':
            self.app.show_receptionist_ui()
        else:
            self.show_error("Invalid credentials")

    def show_error(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.exec_()


if __name__ == '__main__':
    app = QApplication([])
    login_ui = LoginUI(None)
    login_ui.show()
    app.exec_()
