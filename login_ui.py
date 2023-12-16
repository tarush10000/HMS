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
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        self.resize(screen_width, screen_height)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Set up the layout
        layout = QVBoxLayout()

        # Set up the widget to contain the form elements
        form_widget = QWidget()

        # Set up the background image
        background_label = QLabel(form_widget)
        background_pixmap = QPixmap('design/images/frame1.png')
        background_label.setPixmap(background_pixmap.scaledToHeight(int(screen_height)))
        background_label.setMargin(0)
        background_label.setAlignment(Qt.AlignCenter)

        # Set up the form layout
        form_layout = QVBoxLayout(form_widget)
        form_layout.addWidget(background_label)
        form_layout.setAlignment(Qt.AlignCenter) 

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

        form_layout.addWidget(self.login_heading)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.login_button)
        form_layout.setContentsMargins(int(0.3 * self.width()), 0, int(0.3 * self.width()), int(0.3 * self.height()))

        # Set up the main layout for the whole screen
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(form_widget)

        # Set the main window geometry
        screen_geometry = QApplication.desktop().screenGeometry()
        self.setGeometry(screen_geometry)

        # Ensure that the background label is behind the form elements
        background_label.lower()
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            self.show_error("Username and password are required.")
            return

        user_ver = Database.validate_login(username, password)

        if user_ver == 'Doctor':
            self.app.show_doctor_ui()
        elif user_ver == 'Receptionist':
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
