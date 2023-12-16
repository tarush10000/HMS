from PyQt5.QtWidgets import QApplication
from login_ui import LoginUI
from doctor_ui import DoctorUI
from receptionist_ui import ReceptionistUI
from database import Database
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class HospitalManagementApp:
    def __init__(self):
        self.app = QApplication([])
        self.database = Database()
        self.login_ui = LoginUI(self.app)
        self.login_ui.login_button.clicked.connect(self.handle_login)
        self.login_ui.show()

    def handle_login(self):
        username = self.login_ui.username_input.text()
        password = self.login_ui.password_input.text()

        user_role = self.database.validate_login(username, password)
        if user_role == 'Doctor':
            self.show_doctor_ui()
        elif user_role == 'Receptionist':
            self.show_receptionist_ui()

    def show_doctor_ui(self):
        self.login_ui.close()
        self.doctor_ui = DoctorUI()
        self.doctor_ui.show()

    def show_receptionist_ui(self):
        self.login_ui.close()
        self.receptionist_ui = ReceptionistUI()
        self.receptionist_ui.show()

    def run(self):
        self.app.exec_()

if __name__ == "__main__":
    hospital_app = HospitalManagementApp()
    hospital_app.run()
