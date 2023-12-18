from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QHBoxLayout, QLineEdit,QComboBox, QMessageBox, QStyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
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

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        menu_layout = QVBoxLayout()
        menu_layout.setAlignment(Qt.AlignTop)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(0)
        menu_widget = QWidget()
        menu_widget.setStyleSheet("background-color: rgba(255, 68, 0,0.35);")
        menu_widget.setContentsMargins(0, 0, 0, 0)
        menu_widget.setFixedWidth(int(0.15*screen_width))
        menu_widget.setFixedHeight(screen_height)
        menu_widget.setLayout(menu_layout)

        content_layout = QVBoxLayout()
        content_layout.setAlignment(Qt.AlignTop)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: rgb(245, 245, 245);")
        content_widget.setContentsMargins(0, 0, 0, 0)
        content_widget.setFixedHeight(screen_height)
        content_widget.setLayout(content_layout)

        content_top_layout = QHBoxLayout()
        content_top_layout.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        content_top_layout.setContentsMargins(10, 10, 10, 10)
        content_top_layout.setSpacing(0)
        content_top_widget = QWidget()
        content_top_widget.setStyleSheet("")
        content_top_widget.setContentsMargins(0, 0, 0, 0)
        content_top_widget.setLayout(content_top_layout)

        # welcome_label = QLabel(f"Welcome, Dr. {Database.get_username(self.app)}")
        welcome_label = QLabel(f"Welcome, Dr.")
        welcome_label.setStyleSheet("color: rgb(0, 0, 0); font: 14pt \"Poppins\"; font-weight: bold;")
        welcome_label.setFixedHeight(40)
        welcome_label.setContentsMargins(0, 0, 0, 0)
        welcome_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        welcome_label.setFixedWidth(int(0.2*screen_width))

        search_layout = QHBoxLayout()
        search_layout.setAlignment(Qt.AlignVCenter)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(0)
        search_widget = QWidget()
        search_widget.setStyleSheet("border-radius: 20px; padding: 5px; padding-right: 20px;")
        search_widget.setContentsMargins(0, 0, 0, 0)
        search_widget.setLayout(search_layout)
        search_widget.setFixedWidth(int(0.55*screen_width))
        search_input = QLineEdit(self)
        search_input.setPlaceholderText('Enter details to search')
        search_input.setStyleSheet(
            "background-color: rgb(230, 230, 230);"
            "color: rgb(0, 0, 0);" 
            "font: 8pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-top-left-radius: 20px;"
            "border-bottom-left-radius: 20px;"
            "border-top-right-radius: 0px;"
            "border-bottom-right-radius: 0px;"
        )
        search_input.setFixedHeight(40)
        search_input.setContentsMargins(0, 0, 0, 0)
        search_input.setFixedWidth(int(0.3*screen_width))
        search_input.setFont(QFont(search_input.font().family(), italic=True))
        
        # dropdown for search options / filters
        search_options = ['Search Using','Patient ID', 'Patient Name', 'Patient Phone', 'Patient Email', 'Patient Address']
        search_dropdown = QComboBox()
        search_dropdown.addItems(search_options)
        search_dropdown.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 0;"
            "}"

            # Set the hover and pressed states
            "QComboBox:hover {"
            "    background-color: rgb(240, 240, 240);"
            "}"
            "QComboBox:pressed {"
            "    background-color: rgb(220, 220, 220);"
            "}"

            # Hide the box at the side
            "QComboBox::drop-down {"
            "    border: none;"
            "}"
        )
        search_dropdown.setFixedWidth(int(0.1*screen_width))
        search_dropdown.setCurrentText("Search Using")
        for i in range(search_dropdown.count()):
            search_dropdown.model().item(i).setFont(QFont(search_dropdown.font().family(), italic=True))
        search_dropdown.setFixedHeight(40)
        search_dropdown.setContentsMargins(0, 0, 0, 0)
        search_dropdown.setCursor(Qt.PointingHandCursor)
        search_dropdown.setFixedHeight(40)
        search_dropdown.currentIndexChanged.connect(lambda index, sd=search_dropdown: self.handle_search_dropdown_change(sd))


        search_button = QPushButton('Search')
        search_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245,245,245);"
            "font: 10pt \"Poppins\";"
            "border-top-left-radius: 0px;"
            "border-top-right-radius: 20px;"
            "border-bottom-left-radius: 0px;"
            "border-bottom-right-radius: 20px;"  
        )
        search_button.setCursor(Qt.PointingHandCursor)
        search_button.setFlat(True)
        search_button.setFixedHeight(40)
        search_button.setContentsMargins(0, 0, 0, 0)
        search_button.setFixedWidth(int(0.05*screen_width))
        search_button.clicked.connect(lambda: self.search(search_input.text(), search_dropdown.currentText()))

        search_layout.addWidget(search_input)
        search_layout.addWidget(search_dropdown)
        search_layout.addWidget(search_button)



        logout_button = QPushButton('Logout')
        logout_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245,245,245);"
            "font: 10pt \"Poppins\";"
            "border-radius: 20px;"
            "padding: 5px;"
            "margin-left: 20px;"
        )
        logout_button.setCursor(Qt.PointingHandCursor)
        logout_button.setFlat(True)
        logout_button.setFixedHeight(40)
        logout_button.setContentsMargins(0, 0, 0, 0)
        logout_button.setFixedWidth(int(0.1*screen_width))
        logout_button.clicked.connect(self.logout)

        content_top_layout.addWidget(welcome_label)
        content_top_layout.addWidget(search_widget)
        content_top_layout.addWidget(logout_button)

        content_layout.addWidget(content_top_widget)

        layout.addWidget(menu_widget)
        layout.addWidget(content_widget)

        self.setLayout(layout)

    def handle_search_dropdown_change(self, search_dropdown):
        pass

    def search(self, search_input, selected_item):
        if search_input == '':
            self.show_error("Please enter a search query")
            return
        elif selected_item == 'Search Using':
            self.show_error("Please select a search filter")
            return
        
        if selected_item == 'Patient ID':
            if not search_input.isdigit():
                self.show_error("Please enter a valid patient ID")
                return
        elif selected_item == 'Patient Name':
            if not search_input.isalpha():
                self.show_error("Please enter a valid patient name")
                return
        elif selected_item == 'Patient Phone':
            if not search_input.isdigit():
                self.show_error("Please enter a valid patient phone number")
                return
        elif selected_item == 'Patient Email':
            if '@' not in search_input:
                self.show_error("Please enter a valid patient email")
                return
        elif selected_item == 'Patient Address':
            if not search_input.isalnum():
                self.show_error("Please enter a valid patient address")
                return
    
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
