from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from database import Database
import sys, os

class DoctorUI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Doctor Dashboard')
        screen_height = self.app.desktop().screenGeometry().height()
        screen_width = self.app.desktop().screenGeometry().width()
        self.setFixedSize(screen_width, screen_height)
        self.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.showMaximized()

        layout = QVBoxLayout()

        # welcome_label = QLabel(f"Welcome, Dr. {Database.get_username(self.app)}")
        welcome_label = QLabel(f"Welcome, Dr.")

        logout_button = QPushButton('Logout')
        logout_button.clicked.connect(self.logout)

        layout.addWidget(welcome_label)
        layout.addWidget(logout_button)

        self.setLayout(layout)

    def logout(self):
        from login_ui import LoginUI
        self.close()
        self.login_ui = LoginUI(self.app)
        self.login_ui.show()

if __name__ == '__main__':
    app = QApplication([])
    doctor_ui = DoctorUI(app)
    doctor_ui.show()
    app.exec_()
