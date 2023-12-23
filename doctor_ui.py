from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication, QHBoxLayout, QLineEdit,QComboBox, QMessageBox, QStyle, QTableWidget, QTableWidgetItem, QAbstractItemView, QPlainTextEdit, QScrollArea, QHeaderView, QDateEdit, QTimeEdit, QCompleter
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime
from PyQt5.QtGui import QFont, QPixmap, QIcon
from styles import entries_font, unit_font
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

        content_bottom_layout = QHBoxLayout()
        content_bottom_layout.setAlignment(Qt.AlignVCenter)
        content_bottom_layout.setContentsMargins(10, 10, 10, 10)
        content_bottom_layout.setSpacing(0)
        content_bottom_widget = QWidget()
        content_bottom_widget.setStyleSheet("")
        content_bottom_widget.setContentsMargins(0, 0, 0, 0)
        content_bottom_widget.setLayout(content_bottom_layout)

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

        #content bottom part

        content_bottom_left_layout = QVBoxLayout()
        content_bottom_left_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        content_bottom_left_layout.setContentsMargins(0, 0, 0, 0)
        content_bottom_left_layout.setSpacing(0)
        content_bottom_left_widget = QWidget()
        content_bottom_left_widget.setStyleSheet("")
        content_bottom_left_widget.setContentsMargins(10, 10, 10, 10)
        content_bottom_left_widget.setLayout(content_bottom_left_layout)
        content_bottom_left_widget.setFixedWidth(int(0.45*screen_width))

        content_bottom_right_layout = QVBoxLayout()
        content_bottom_right_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        content_bottom_right_layout.setContentsMargins(0, 0, 0, 0)
        content_bottom_right_layout.setSpacing(0)
        content_bottom_right_widget = QWidget()
        content_bottom_right_widget.setStyleSheet("")
        content_bottom_right_widget.setContentsMargins(10, 10, 10, 10)
        content_bottom_right_widget.setLayout(content_bottom_right_layout)



        filter_layout = QHBoxLayout()
        filter_layout.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        filter_layout.setContentsMargins(0, 0, 0, 0)
        filter_layout.setSpacing(0)
        filter_widget = QWidget()
        filter_widget.setStyleSheet("border-radius: 20px; padding: 5px; padding-right: 20px;")
        filter_widget.setContentsMargins(0, 0, 0, 10)
        filter_widget.setLayout(filter_layout)

        filter_label = QLabel('Filter By:')
        filter_label.setStyleSheet("color: rgb(0, 0, 0); font: 10pt \"Poppins\";")
        filter_label.setFixedHeight(40)
        filter_label.setContentsMargins(0, 0, 0, 0)
        filter_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        filter_label.setFixedWidth(int(0.2*screen_width))

        # dropdown for search options / filters
        filter_options = ['All Patients','This Month','This Week', 'Today', 'Queue',]
        filter_dropdown = QComboBox()
        filter_dropdown.addItems(filter_options)
        filter_dropdown.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-top-left-radius: 20px;"
            "    border-bottom-left-radius: 20px;"
            "    border-top-right-radius: 0px;"
            "    border-bottom-right-radius: 0px;"
            "    margin-right: 0px;"
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
        for i in range(filter_dropdown.count()):
            filter_dropdown.model().item(i).setFont(QFont(filter_dropdown.font().family(), italic=True))
        filter_dropdown.setFixedHeight(40)
        filter_dropdown.setContentsMargins(0, 0, 0, 0)
        filter_dropdown.setCursor(Qt.PointingHandCursor)
        filter_dropdown.setFixedHeight(40)

        filter_go_button = QPushButton('Go')
        filter_go_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245,245,245);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "margin-left: 0px;"
            "border-top-left-radius: 0px;"
            "border-top-right-radius: 20px;"
            "border-bottom-left-radius: 0px;"
            "border-bottom-right-radius: 20px;"
        )
        filter_go_button.setCursor(Qt.PointingHandCursor)
        filter_go_button.setFlat(True)
        filter_go_button.setFixedHeight(40)
        filter_go_button.setContentsMargins(0, 0, 0, 0)
        filter_go_button.setFixedWidth(int(0.03*screen_width))
        filter_go_button.clicked.connect(lambda: self.populate_table(patient_table, filter_parameter = filter_dropdown.currentText()))


        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(filter_dropdown)
        filter_layout.addWidget(filter_go_button)

        #table of patients according to filter
        patient_table = QTableWidget()
        patient_table.setColumnCount(4)
        patient_table.setColumnWidth(0, 150)
        patient_table.setColumnWidth(1, 250)
        patient_table.setColumnWidth(2, 250)
        patient_table.setColumnWidth(3, 200)
        patient_table.setHorizontalHeaderLabels(['Patient ID', 'Patient Name', 'Guardian Name', 'Mobile Number'])
        patient_table.setStyleSheet(
            "QTableWidget {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 0;"
            "}"

            # Hide the box at the side
            "QTableWidget::drop-down {"
            "    border: none;"
            "}"
        )
        patient_table.setContentsMargins(0, 0, 0, 0)
        patient_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        patient_table.setSelectionMode(QAbstractItemView.SingleSelection)
        patient_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        patient_table.itemClicked.connect(lambda item: self.row_single_clicked(item, patient_table, patient_first_name, patient_middle_name,patient_last_name,patient_guardian_name,patient_occupation,patient_number1,patient_number2,patient_gender,patient_address,patient_age,patient_dob,patient_obst_history_text,patient_family_history_text,patient_past_history_text))
        patient_table.itemDoubleClicked.connect(lambda item: self.row_double_clicked(item, patient_table, filter_widget, diagnostic_scroll_area))

        #section for diagnostics and treatment (initially hidden)
        diagnostic_scroll_area = QScrollArea(self)
        diagnostic_scroll_area.setWidgetResizable(True)
        diagnostic_scroll_area.setStyleSheet("background-color: rgb(235, 235, 235); border-radius: 20px; border: none;")
        diagnostic_scroll_area.setContentsMargins(0, 0, 0, 0)
        diagnostic_scroll_area.setFixedWidth(int(0.4*screen_width))
        diagnostic_scroll_area.setFixedHeight(int(0.7*screen_height))
        diagnostic_scroll_area.setVisible(False)

        diagnostics_layout = QVBoxLayout()
        diagnostics_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        diagnostics_layout.setContentsMargins(0, 0, 0, 0)
        diagnostics_layout.setSpacing(0)
        diagnostics_widget = QWidget(diagnostic_scroll_area)
        diagnostics_widget.setStyleSheet("")
        diagnostics_widget.setContentsMargins(10, 10, 10, 10)
        diagnostics_widget.setLayout(diagnostics_layout)

        diagnostics_heading_layout = QHBoxLayout()
        diagnostics_heading_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        diagnostics_heading_layout.setContentsMargins(0, 0, 0, 0)
        diagnostics_heading_layout.setSpacing(0)
        diagnostics_heading_widget = QWidget()
        diagnostics_heading_widget.setStyleSheet("")
        diagnostics_heading_widget.setContentsMargins(0, 0, 0, 0)
        diagnostics_heading_widget.setLayout(diagnostics_heading_layout)
        diagnostics_heading_widget.setFixedHeight(80)
        
        diagnostics_label = QLabel('Diagnostics')
        diagnostics_label.setStyleSheet("color: rgb(0, 0, 0); font: 15pt \"Poppins\"; font-weight: bold;")
        diagnostics_label.setFixedHeight(80)
        diagnostics_label.setContentsMargins(0, 0, 0, 0)
        diagnostics_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        diagnostics_back_button = QPushButton()
        back_button_image_address = resource_path('design/images/back.png')
        back_button_image = QPixmap(back_button_image_address)
        back_button_image = back_button_image.scaledToWidth(30)
        diagnostics_back_button.setIcon(QIcon(back_button_image))
        diagnostics_back_button.setIconSize(back_button_image.rect().size())
        diagnostics_back_button.setCursor(Qt.PointingHandCursor)
        diagnostics_back_button.setFlat(True)
        diagnostics_back_button.clicked.connect(lambda : self.back_button_clicked(patient_table, filter_widget, diagnostic_scroll_area))

        diagnostics_heading_layout.addWidget(diagnostics_back_button)
        diagnostics_heading_layout.addWidget(diagnostics_label)

        clinical_findings_heading = QLabel('Clinical Findings')
        clinical_findings_heading.setStyleSheet("color: rgb(0, 0, 0); font: 12pt \"Poppins\"; font-weight: bold;")
        clinical_findings_heading.setFixedHeight(40)
        clinical_findings_heading.setContentsMargins(0, 0, 0, 0)
        clinical_findings_heading.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        clinical_findings_add_layout = QHBoxLayout()
        clinical_findings_add_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        clinical_findings_add_layout.setContentsMargins(0, 0, 0, 0)
        clinical_findings_add_layout.setSpacing(0)
        clinical_findings_add_widget = QWidget()
        clinical_findings_add_widget.setStyleSheet("")
        clinical_findings_add_widget.setContentsMargins(0, 5, 0, 5)
        clinical_findings_add_widget.setLayout(clinical_findings_add_layout)
        clinical_findings_add_text = QLineEdit(self)
        clinical_findings_add_text.setPlaceholderText('Enter clinical findings')
        clinical_findings_add_text.setStyleSheet(
            "background-color: rgb(230, 230, 230);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
            "margin-right: 5px;"
        )
        clinical_findings_add_text.setFixedHeight(40)
        clinical_findings_add_text.setContentsMargins(0, 0, 0, 0)
        clinical_findings_add_text.setFixedWidth(int(0.3*screen_width))
        clinical_findings_add_text.setFont(QFont(clinical_findings_add_text.font().family(), italic=True))

        file = open(resource_path('design/lists/clinical_findings.txt'), 'r')
        clinical_findings = [line.strip() for line in file]

        completer = QCompleter(clinical_findings, self)
        completer.setCaseSensitivity(False)
        clinical_findings_add_text.setCompleter(completer)
        clinical_findings_add_text.textChanged.connect(lambda: self.update_clinical_findings_file(clinical_findings_add_text))
        
        clinical_findings_add_button = QPushButton()
        clinical_findings_add_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245,245,245);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 10px;"
            "margin-right: 5px;"
        )
        add_button_image_address = resource_path('design/images/add.png')
        add_button_image = QPixmap(add_button_image_address)
        add_button_image = add_button_image.scaledToWidth(30)
        clinical_findings_add_button.setIcon(QIcon(add_button_image))
        clinical_findings_add_button.setIconSize(add_button_image.rect().size())
        clinical_findings_add_button.setCursor(Qt.PointingHandCursor)
        clinical_findings_add_button.setFlat(True)
        clinical_findings_add_button.clicked.connect(lambda : self.add_clinical_findings(clinical_findings_add_text, clinical_findings_add_button, clinical_findings_table))
        clinical_findings_add_button.setVisible(True)

        clinical_findings_add_layout.addWidget(clinical_findings_add_text)
        clinical_findings_add_layout.addWidget(clinical_findings_add_button)

        clinical_findings_table = QTableWidget()
        clinical_findings_table.setFixedHeight(200)
        clinical_findings_table.setFixedWidth(int(0.35*screen_width))
        clinical_findings_table.setViewportMargins(0, 10, 0, 0)
        clinical_findings_table.setContentsMargins(0, 10, 0, 0)
        clinical_findings_table.setFont(QFont(clinical_findings_table.font().family(), italic=True))
        clinical_findings_table.setColumnCount(1)
        clinical_findings_table.setRowCount(0)

        if clinical_findings_table.rowCount() == 0:
            clinical_findings_table.setVisible(False)
        clinical_findings_table.setHorizontalHeaderLabels(['Clinical Findings'])
        
        clinical_findings_table.horizontalHeader().setStyleSheet(
            "QHeaderView {"
            "    background-color: rgb(67, 79, 194);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    border-radius: 20px;"
            "}"
        )
        clinical_findings_table.setStyleSheet(
            "QTableView {"
            "    background-color: rgb(255, 255, 255);"
            "    alternate-background-color: rgb(240, 240, 240);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
        )
        clinical_findings_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    border: 0px;"
            "    background: #f0f0f0;"
            "    width: 10px;"
            "    margin: 0px 0px 0px 0px;"
            "}"

            "QScrollBar::handle:vertical {"
            "    background: #666666;"
            "    min-height: 20px;"
            "}"

            "QScrollBar::add-line:vertical {"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"

            "QScrollBar::sub-line:vertical {"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
            "}"
        )
        clinical_findings_table.horizontalHeader().setFixedHeight(40)
        clinical_findings_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        clinical_findings_table.verticalHeader().hide()
        clinical_findings_table.setShowGrid(False)
        clinical_findings_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        clinical_findings_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        clinical_findings_table.setSelectionMode(QAbstractItemView.SingleSelection)
        clinical_findings_table.setAlternatingRowColors(True)

        clinical_findings_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        clinical_findings_table.setSelectionMode(QAbstractItemView.SingleSelection)
        clinical_findings_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        clinical_findings_table.itemDoubleClicked.connect(lambda item: self.findings_delete(item, clinical_findings_table, filter_widget, diagnostic_scroll_area))

        internal_findings_heading = QLabel('Internal Findings')
        internal_findings_heading.setStyleSheet("color: rgb(0, 0, 0); font: 12pt \"Poppins\"; font-weight: bold;")
        internal_findings_heading.setFixedHeight(40)
        internal_findings_heading.setContentsMargins(0, 0, 0, 0)
        internal_findings_heading.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        internal_findings_input = QPlainTextEdit(self)
        internal_findings_input.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
            "margin: 0px;"
        )
        internal_findings_input.setFixedHeight(80)
        internal_findings_input.setFixedWidth(int(0.35*screen_width))
        internal_findings_input.setContentsMargins(0, 0, 0, 0)
        internal_findings_input.setReadOnly(True)
        
        # add widgets to layouts
        diagnostics_layout.addWidget(diagnostics_heading_widget)
        diagnostics_layout.addWidget(clinical_findings_heading)
        diagnostics_layout.addWidget(clinical_findings_add_widget)
        diagnostics_layout.addWidget(clinical_findings_table)
        diagnostics_layout.addWidget(internal_findings_heading)
        diagnostics_layout.addWidget(internal_findings_input)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: rgb(235, 235, 235); border-radius: 20px; border: none;")
        scroll_area.setContentsMargins(0, 0, 0, 0)
        scroll_area.setFixedWidth(int(0.35*screen_width))
        scroll_area.setFixedHeight(int(0.7*screen_height))

        # section showing patient details
        patient_details_layout = QVBoxLayout()
        patient_details_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        patient_details_layout.setContentsMargins(0, 0, 0, 0)
        patient_details_layout.setSpacing(0)
        patient_details_widget = QWidget(scroll_area)
        patient_details_widget.setContentsMargins(10, 10, 10, 10)
        patient_details_widget.setLayout(patient_details_layout)

        patient_details_heading_layout = QHBoxLayout()
        patient_details_heading_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        patient_details_heading_layout.setContentsMargins(0, 0, 0, 0)
        patient_details_heading_layout.setSpacing(0)
        patient_details_heading_widget = QWidget()
        patient_details_heading_widget.setStyleSheet("")
        patient_details_heading_widget.setContentsMargins(0, 0, 0, 0)
        patient_details_heading_widget.setLayout(patient_details_heading_layout)
        patient_details_heading_widget.setFixedHeight(80)

        patient_details_label = QLabel('Basic Details')
        patient_details_label.setStyleSheet("color: rgb(0, 0, 0); font: 15pt \"Poppins\"; font-weight: bold;")
        patient_details_label.setFixedHeight(80)
        patient_details_label.setContentsMargins(0, 0, 0, 0)
        patient_details_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        patient_details_edit_button = QPushButton()
        edit_button_image_address = resource_path('design/images/edit.png')
        edit_button_image = QPixmap(edit_button_image_address)
        edit_button_image = edit_button_image.scaledToWidth(30)
        patient_details_edit_button.setIcon(QIcon(edit_button_image))
        patient_details_edit_button.setIconSize(edit_button_image.rect().size())
        patient_details_edit_button.setCursor(Qt.PointingHandCursor)
        patient_details_edit_button.setFlat(True)
        patient_details_edit_button.clicked.connect(lambda : self.details_edit(patient_first_name, patient_middle_name, patient_last_name, patient_guardian_name, patient_occupation, patient_gender, patient_number1, patient_number2, patient_address, patient_age, patient_dob, patient_weight, patient_height, patient_details_edit_button, patient_details_save_button))

        patient_details_save_button = QPushButton()
        patient_details_save_button.setVisible(False)
        save_button_image_address = resource_path('design/images/confirm.png')
        save_button_image = QPixmap(save_button_image_address)
        save_button_image = save_button_image.scaledToWidth(30)
        patient_details_save_button.setIcon(QIcon(save_button_image))
        patient_details_save_button.setIconSize(save_button_image.rect().size())
        patient_details_save_button.setCursor(Qt.PointingHandCursor)
        patient_details_save_button.setFlat(True)
        patient_details_save_button.clicked.connect(lambda : self.details_save(patient_first_name, patient_middle_name, patient_last_name, patient_guardian_name, patient_occupation, patient_gender, patient_number1, patient_number2, patient_address, patient_age, patient_dob, patient_weight, patient_height, patient_details_edit_button, patient_details_save_button))

        patient_details_heading_layout.addWidget(patient_details_label)
        patient_details_heading_layout.addWidget(patient_details_edit_button)
        patient_details_heading_layout.addWidget(patient_details_save_button)

        patient_name_layout = QHBoxLayout()
        patient_name_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_name_layout.setContentsMargins(0, 0, 0, 0)
        patient_name_layout.setSpacing(0)
        patient_name_widget = QWidget()
        patient_name_widget.setStyleSheet("")
        patient_name_widget.setContentsMargins(0, 5, 0, 5)
        patient_name_widget.setLayout(patient_name_layout)
        patient_name_label = QLabel('Mrs. ')
        patient_name_label.setFont(entries_font)
        patient_name_label.setFixedHeight(40)
        patient_name_label.setFixedWidth(int(0.06*screen_width))
        patient_name_label.setContentsMargins(0, 0, 0, 0)
        patient_first_name = QLineEdit(self)
        patient_first_name.setReadOnly(True)
        patient_first_name.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "margin-right: 5px;"
        )
        patient_first_name.setFixedHeight(40)
        patient_first_name.setContentsMargins(0, 0, 0, 0)
        patient_first_name.setFont(QFont(patient_first_name.font().family(), italic=True))

        patient_middle_name = QLineEdit(self)
        patient_middle_name.setReadOnly(True)
        patient_middle_name.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "margin-right: 5px;"
        )
        patient_middle_name.setFixedHeight(40)
        patient_middle_name.setContentsMargins(0, 0, 0, 0)
        patient_middle_name.setFont(QFont(patient_middle_name.font().family(), italic=True))

        patient_last_name = QLineEdit(self)
        patient_last_name.setReadOnly(True)
        patient_last_name.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
        )
        patient_last_name.setFixedHeight(40)
        patient_last_name.setContentsMargins(0, 0, 0, 0)
        patient_last_name.setFont(QFont(patient_last_name.font().family(), italic=True))

        patient_name_layout.addWidget(patient_name_label)
        patient_name_layout.addWidget(patient_first_name)
        patient_name_layout.addWidget(patient_middle_name)
        patient_name_layout.addWidget(patient_last_name)

        patient_guardian_layout = QHBoxLayout()
        patient_guardian_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_guardian_layout.setContentsMargins(0, 0, 0, 0)
        patient_guardian_layout.setSpacing(0)
        patient_guardian_widget = QWidget()
        patient_guardian_widget.setStyleSheet("")
        patient_guardian_widget.setContentsMargins(0, 5, 0, 5)
        patient_guardian_widget.setLayout(patient_guardian_layout)
        patient_guardian_label = QLabel('Guardian: ')
        patient_guardian_label.setFont(entries_font)
        patient_guardian_label.setFixedHeight(40)
        patient_guardian_label.setFixedWidth(int(0.06*screen_width))
        patient_guardian_label.setContentsMargins(0, 0, 0, 0)
        patient_guardian_name = QLineEdit(self)
        patient_guardian_name.setReadOnly(True)
        patient_guardian_name.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_guardian_name.setFixedHeight(40)
        patient_guardian_name.setContentsMargins(0, 0, 0, 0)
        patient_guardian_name.setFont(QFont(patient_guardian_name.font().family(), italic=True))

        patient_guardian_layout.addWidget(patient_guardian_label)
        patient_guardian_layout.addWidget(patient_guardian_name)


        patient_occ_gen_layout = QHBoxLayout()
        patient_occ_gen_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_occ_gen_layout.setContentsMargins(0, 0, 0, 0)
        patient_occ_gen_layout.setSpacing(0)
        patient_occ_gen_widget = QWidget()
        patient_occ_gen_widget.setStyleSheet("")
        patient_occ_gen_widget.setContentsMargins(0, 5, 0, 5)
        patient_occ_gen_widget.setLayout(patient_occ_gen_layout)
        patient_occupation_label = QLabel('Occupation: ')
        patient_occupation_label.setFont(entries_font)
        patient_occupation_label.setFixedHeight(40)
        patient_occupation_label.setFixedWidth(int(0.06*screen_width))
        patient_occupation_label.setContentsMargins(0, 0, 0, 0)
        patient_occupation = QLineEdit(self)
        patient_occupation.setReadOnly(True)
        patient_occupation.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "margin-right: 5px;"
        )
        patient_occupation.setFixedHeight(40)
        patient_occupation.setContentsMargins(0, 0, 0, 0)
        patient_occupation.setFont(QFont(patient_occupation.font().family(), italic=True))
        patient_gender_label = QLabel('Gender: ')
        patient_gender_label.setFont(entries_font)
        patient_gender_label.setFixedHeight(40)
        patient_gender_label.setContentsMargins(0, 0, 0, 0)
        patient_gender = QLineEdit(self)
        patient_gender.setReadOnly(True)
        patient_gender.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
        )

        patient_occ_gen_layout.addWidget(patient_occupation_label)
        patient_occ_gen_layout.addWidget(patient_occupation)
        patient_occ_gen_layout.addWidget(patient_gender_label)
        patient_occ_gen_layout.addWidget(patient_gender)


        patient_number1_layout = QHBoxLayout()
        patient_number1_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_number1_layout.setContentsMargins(0, 0, 0, 0)
        patient_number1_layout.setSpacing(0)
        patient_number1_widget = QWidget()
        patient_number1_widget.setStyleSheet("")
        patient_number1_widget.setContentsMargins(0, 5, 0, 5)
        patient_number1_widget.setLayout(patient_number1_layout)
        patient_number1_label = QLabel('Number 1: ')
        patient_number1_label.setFont(entries_font)
        patient_number1_label.setFixedHeight(40)
        patient_number1_label.setFixedWidth(int(0.06*screen_width))
        patient_number1_label.setContentsMargins(0, 0, 0, 0)
        patient_number1 = QLineEdit(self)
        patient_number1.setReadOnly(True)
        patient_number1.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_number1.setFixedHeight(40)
        patient_number1.setContentsMargins(0, 0, 0, 0)
        patient_number1.setFont(QFont(patient_number1.font().family(), italic=True))

        patient_number1_layout.addWidget(patient_number1_label)
        patient_number1_layout.addWidget(patient_number1)

        patient_number2_layout = QHBoxLayout()
        patient_number2_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_number2_layout.setContentsMargins(0, 0, 0, 0)
        patient_number2_layout.setSpacing(0)
        patient_number2_widget = QWidget()
        patient_number2_widget.setStyleSheet("")
        patient_number2_widget.setContentsMargins(0, 5, 0, 5)
        patient_number2_widget.setLayout(patient_number2_layout)
        patient_number2_label = QLabel('Number 2: ')
        patient_number2_label.setFont(entries_font)
        patient_number2_label.setFixedHeight(40)
        patient_number2_label.setFixedWidth(int(0.06*screen_width))
        patient_number2_label.setContentsMargins(0, 0, 0, 0)
        patient_number2 = QLineEdit(self)
        patient_number2.setReadOnly(True)
        patient_number2.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_number2.setFixedHeight(40)
        patient_number2.setContentsMargins(0, 0, 0, 0)
        patient_number2.setFont(QFont(patient_number2.font().family(), italic=True))

        patient_number2_layout.addWidget(patient_number2_label)
        patient_number2_layout.addWidget(patient_number2)
        
        patient_address_layout = QHBoxLayout()
        patient_address_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_address_layout.setContentsMargins(0, 0, 0, 0)
        patient_address_layout.setSpacing(0)
        patient_address_widget = QWidget()
        patient_address_widget.setStyleSheet("")
        patient_address_widget.setContentsMargins(0, 5, 0, 5)
        patient_address_widget.setLayout(patient_address_layout)
        patient_address_label = QLabel('Address: ')
        patient_address_label.setFont(entries_font)
        patient_address_label.setFixedHeight(40)
        patient_address_label.setFixedWidth(int(0.06*screen_width))
        patient_address_label.setContentsMargins(0, 0, 0, 0)
        patient_address = QPlainTextEdit(self)
        patient_address.setReadOnly(True)
        patient_address.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);" 
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
            "margin: 0px;"
        )
        patient_address.setFixedHeight(80)
        patient_address.setContentsMargins(0, 0, 0, 0)

        patient_address_layout.addWidget(patient_address_label)
        patient_address_layout.addWidget(patient_address)
        patient_address_widget.setFixedHeight(100)

        patient_age_layout = QHBoxLayout()
        patient_age_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_age_layout.setContentsMargins(0, 0, 0, 0)
        patient_age_layout.setSpacing(0)
        patient_age_widget = QWidget()
        patient_age_widget.setStyleSheet("")
        patient_age_widget.setContentsMargins(0, 5, 0, 5)
        patient_age_widget.setLayout(patient_age_layout)
        patient_age_label = QLabel('Age: ')
        patient_age_label.setFont(entries_font)
        patient_age_label.setFixedHeight(40)
        patient_age_label.setFixedWidth(int(0.06*screen_width))
        patient_age_label.setContentsMargins(0, 0, 0, 0)
        patient_age = QLineEdit(self)
        patient_age.setReadOnly(True)
        patient_age.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_age.setFixedHeight(40)
        patient_age.setContentsMargins(0, 0, 0, 0)
        patient_age.setFont(QFont(patient_age.font().family(), italic=True))

        patient_dob_label = QLabel('DOB: ')
        patient_dob_label.setFont(entries_font)
        patient_dob_label.setFixedHeight(40)
        patient_dob_label.setContentsMargins(5, 0, 0, 0)
        patient_dob = QLineEdit(self)
        patient_dob.setReadOnly(True)
        patient_dob.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_dob.setFixedHeight(40)
        patient_dob.setContentsMargins(0, 0, 0, 0)
        patient_dob.setFont(QFont(patient_dob.font().family(), italic=True))

        patient_age_layout.addWidget(patient_age_label)
        patient_age_layout.addWidget(patient_age)
        patient_age_layout.addWidget(patient_dob_label)
        patient_age_layout.addWidget(patient_dob)

        patient_weight_height_layout = QHBoxLayout()
        patient_weight_height_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_weight_height_layout.setContentsMargins(0, 0, 0, 0)
        patient_weight_height_layout.setSpacing(0)
        patient_weight_height_widget = QWidget()
        patient_weight_height_widget.setStyleSheet("")
        patient_weight_height_widget.setContentsMargins(0, 5, 0, 5)
        patient_weight_height_widget.setLayout(patient_weight_height_layout)
        patient_weight_label = QLabel('Weight: ')
        patient_weight_label.setFont(entries_font)
        patient_weight_label.setFixedHeight(40)
        patient_weight_label.setFixedWidth(int(0.06*screen_width))
        patient_weight_label.setContentsMargins(0, 0, 0, 0)
        patient_weight = QLineEdit(self)
        patient_weight.setReadOnly(True)
        patient_weight.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_weight.setFixedHeight(40)
        patient_weight.setContentsMargins(0, 0, 0, 0)
        patient_weight.setFont(QFont(patient_weight.font().family(), italic=True))
        patient_weight_unit = QLabel('kg')
        patient_weight_unit.setFont(unit_font)
        patient_weight_unit.setFixedHeight(40)
        patient_weight_unit.setContentsMargins(0, 0, 5, 0)

        patient_height_label = QLabel('Height: ')
        patient_height_label.setFont(entries_font)
        patient_height_label.setFixedHeight(40)
        patient_height_label.setContentsMargins(5, 0, 0, 0)
        patient_height = QLineEdit(self)
        patient_height.setReadOnly(True)
        patient_height.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_height.setFixedHeight(40)
        patient_height.setContentsMargins(0, 0, 0, 0)
        patient_height.setFont(QFont(patient_height.font().family(), italic=True))
        patient_height_unit = QLabel('cm')
        patient_height_unit.setFont(unit_font)
        patient_height_unit.setFixedHeight(40)
        patient_height_unit.setContentsMargins(0, 0, 0, 0)

        patient_weight_height_layout.addWidget(patient_weight_label)
        patient_weight_height_layout.addWidget(patient_weight)
        patient_weight_height_layout.addWidget(patient_weight_unit)
        patient_weight_height_layout.addWidget(patient_height_label)
        patient_weight_height_layout.addWidget(patient_height)
        patient_weight_height_layout.addWidget(patient_height_unit)


        patient_report_heading_layout = QHBoxLayout()
        patient_report_heading_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        patient_report_heading_layout.setContentsMargins(0, 0, 0, 0)
        patient_report_heading_layout.setSpacing(0)
        patient_report_heading_widget = QWidget()
        patient_report_heading_widget.setStyleSheet("")
        patient_report_heading_widget.setContentsMargins(0, 0, 0, 0)
        patient_report_heading_widget.setLayout(patient_report_heading_layout)
        patient_report_heading_widget.setFixedHeight(80)

        patient_report_label = QLabel('Test Results')
        patient_report_label.setStyleSheet("color: rgb(0, 0, 0); font: 15pt \"Poppins\"; font-weight: bold;")
        patient_report_label.setFixedHeight(80)
        patient_report_label.setContentsMargins(0, 0, 0, 0)
        patient_report_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        patient_report_edit_button = QPushButton()
        edit_button_image_address = resource_path('design/images/edit.png')
        edit_button_image = QPixmap(edit_button_image_address)
        edit_button_image = edit_button_image.scaledToWidth(30)
        patient_report_edit_button.setIcon(QIcon(edit_button_image))
        patient_report_edit_button.setIconSize(edit_button_image.rect().size())
        patient_report_edit_button.setCursor(Qt.PointingHandCursor)
        patient_report_edit_button.setFlat(True)
        patient_report_edit_button.clicked.connect(lambda : self.report_edit(patient_blood_group, patient_hb, patient_vdlr, patient_TLC, patient_hiv, patient_plt, patient_hbsag, patient_bsugar, patient_antihcv, patient_gct, patient_igm, patient_gtt, patient_igg, patient_bil, patient_urea, patient_sgot, patient_creat, patient_sgpt, patient_ua, patient_alkphos, patient_dualmar, patient_protein, patient_triplemar, patient_t3t4tsh, patient_quadtest, patient_hba1c, patient_hplc, patient_ict, patient_chestxray, patient_ecg, patient_echo, patient_ptinr, patient_urine, patient_USG, patient_other, patient_report_edit_button, patient_report_save_button))

        patient_report_save_button = QPushButton()
        patient_report_save_button.setVisible(False)
        save_button_image_address = resource_path('design/images/confirm.png')
        save_button_image = QPixmap(save_button_image_address)
        save_button_image = save_button_image.scaledToWidth(30)
        patient_report_save_button.setIcon(QIcon(save_button_image))
        patient_report_save_button.setIconSize(save_button_image.rect().size())
        patient_report_save_button.setCursor(Qt.PointingHandCursor)
        patient_report_save_button.setFlat(True)
        patient_report_save_button.clicked.connect(lambda : self.report_save(patient_blood_group, patient_hb, patient_vdlr, patient_TLC, patient_hiv, patient_plt, patient_hbsag, patient_bsugar, patient_antihcv, patient_gct, patient_igm, patient_gtt, patient_igg, patient_bil, patient_urea, patient_sgot, patient_creat, patient_sgpt, patient_ua, patient_alkphos, patient_dualmar, patient_protein, patient_triplemar, patient_t3t4tsh, patient_quadtest, patient_hba1c, patient_hplc, patient_ict, patient_chestxray, patient_ecg, patient_echo, patient_ptinr, patient_urine, patient_USG, patient_other, patient_report_edit_button, patient_report_save_button))

        patient_report_heading_layout.addWidget(patient_report_label)
        patient_report_heading_layout.addWidget(patient_report_edit_button)
        patient_report_heading_layout.addWidget(patient_report_save_button)

        patient_blood_group_layout = QHBoxLayout()
        patient_blood_group_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_blood_group_layout.setContentsMargins(0, 0, 0, 0)
        patient_blood_group_layout.setSpacing(0)
        patient_blood_group_widget = QWidget()
        patient_blood_group_widget.setStyleSheet("")
        patient_blood_group_widget.setContentsMargins(0, 5, 0, 5)
        patient_blood_group_widget.setLayout(patient_blood_group_layout)
        patient_blood_group_label = QLabel('Blood Group: ')
        patient_blood_group_label.setFont(entries_font)
        patient_blood_group_label.setFixedHeight(40)
        patient_blood_group_label.setFixedWidth(int(0.06*screen_width))
        patient_blood_group_label.setContentsMargins(0, 0, 0, 0)
        patient_blood_group = QLineEdit(self)
        patient_blood_group.setReadOnly(True)
        patient_blood_group.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_blood_group.setFixedHeight(40)
        patient_blood_group.setFixedWidth(int(0.08*screen_width))
        patient_blood_group.setContentsMargins(0, 0, 0, 0)
        patient_blood_group.setFont(QFont(patient_blood_group.font().family(), italic=True))

        patient_hb_label = QLabel('Hb: ')
        patient_hb_label.setFont(entries_font)
        patient_hb_label.setFixedHeight(40)
        patient_hb_label.setFixedWidth(int(0.06*screen_width))
        patient_hb_label.setContentsMargins(30, 0, 0, 0)
        patient_hb = QLineEdit(self)
        patient_hb.setReadOnly(True)
        patient_hb.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_hb.setFixedHeight(40)
        patient_hb.setFixedWidth(int(0.08*screen_width))
        patient_hb.setContentsMargins(0, 0, 0, 0)
        patient_hb.setFont(QFont(patient_hb.font().family(), italic=True))
        patient_hb_unit = QLabel('g/dL')
        patient_hb_unit.setFont(unit_font)
        patient_hb_unit.setFixedHeight(40)
        patient_hb_unit.setContentsMargins(0, 0, 0, 0)

        patient_blood_group_layout.addWidget(patient_blood_group_label)
        patient_blood_group_layout.addWidget(patient_blood_group)
        patient_blood_group_layout.addWidget(patient_hb_label)
        patient_blood_group_layout.addWidget(patient_hb)
        patient_blood_group_layout.addWidget(patient_hb_unit)

        patient_vdlr_TLC_layout = QHBoxLayout()
        patient_vdlr_TLC_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_vdlr_TLC_layout.setContentsMargins(0, 0, 0, 0)
        patient_vdlr_TLC_layout.setSpacing(0)
        patient_vdlr_TLC_widget = QWidget()
        patient_vdlr_TLC_widget.setStyleSheet("")
        patient_vdlr_TLC_widget.setContentsMargins(0, 5, 0, 5)
        patient_vdlr_TLC_widget.setLayout(patient_vdlr_TLC_layout)
        patient_vdlr_label = QLabel('VDRL: ')
        patient_vdlr_label.setFont(entries_font)
        patient_vdlr_label.setFixedHeight(40)
        patient_vdlr_label.setFixedWidth(int(0.06*screen_width))
        patient_vdlr_label.setContentsMargins(0, 0, 0, 0)
        patient_vdlr = QLineEdit(self)
        patient_vdlr.setReadOnly(True)
        patient_vdlr.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_vdlr.setFixedHeight(40)
        patient_vdlr.setFixedWidth(int(0.08*screen_width)) 
        patient_vdlr.setContentsMargins(0, 0, 0, 0)
        patient_vdlr.setFont(QFont(patient_vdlr.font().family(), italic=True))

        patient_TLC_label = QLabel('TLC: ')
        patient_TLC_label.setFont(entries_font)
        patient_TLC_label.setFixedHeight(40)
        patient_TLC_label.setFixedWidth(int(0.06*screen_width))
        patient_TLC_label.setContentsMargins(30, 0, 0, 0)
        patient_TLC = QLineEdit(self)
        patient_TLC.setReadOnly(True)
        patient_TLC.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_TLC.setFixedHeight(40)
        patient_TLC.setFixedWidth(int(0.08*screen_width))
        patient_TLC.setContentsMargins(0, 0, 0, 0)
        patient_TLC.setFont(QFont(patient_TLC.font().family(), italic=True))
        patient_TLC_unit = QLabel('cumm')
        patient_TLC_unit.setFont(unit_font)
        patient_TLC_unit.setFixedHeight(40)
        patient_TLC_unit.setContentsMargins(0, 0, 0, 0)

        patient_vdlr_TLC_layout.addWidget(patient_vdlr_label)
        patient_vdlr_TLC_layout.addWidget(patient_vdlr)
        patient_vdlr_TLC_layout.addWidget(patient_TLC_label)
        patient_vdlr_TLC_layout.addWidget(patient_TLC)
        patient_vdlr_TLC_layout.addWidget(patient_TLC_unit)

        patient_hiv_plt_layout = QHBoxLayout()
        patient_hiv_plt_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_hiv_plt_layout.setContentsMargins(0, 0, 0, 0)
        patient_hiv_plt_layout.setSpacing(0)
        patient_hiv_plt_widget = QWidget()
        patient_hiv_plt_widget.setStyleSheet("")
        patient_hiv_plt_widget.setContentsMargins(0, 5, 0, 5)
        patient_hiv_plt_widget.setLayout(patient_hiv_plt_layout)
        patient_hiv_label = QLabel('HIV: ')
        patient_hiv_label.setFont(entries_font)
        patient_hiv_label.setFixedHeight(40)
        patient_hiv_label.setFixedWidth(int(0.06*screen_width))
        patient_hiv_label.setContentsMargins(0, 0, 0, 0)
        patient_hiv = QLineEdit(self)
        patient_hiv.setReadOnly(True)
        patient_hiv.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_hiv.setFixedHeight(40)
        patient_hiv.setFixedWidth(int(0.08*screen_width))
        patient_hiv.setContentsMargins(0, 0, 0, 0)
        patient_hiv.setFont(QFont(patient_hiv.font().family(), italic=True))

        patient_plt_label = QLabel('Plt. : ')
        patient_plt_label.setFont(entries_font)
        patient_plt_label.setFixedHeight(40)
        patient_plt_label.setFixedWidth(int(0.06*screen_width))
        patient_plt_label.setContentsMargins(30, 0, 0, 0)
        patient_plt = QLineEdit(self)
        patient_plt.setReadOnly(True)
        patient_plt.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_plt.setFixedHeight(40)
        patient_plt.setFixedWidth(int(0.08*screen_width))
        patient_plt.setContentsMargins(0, 0, 0, 0)
        patient_plt.setFont(QFont(patient_plt.font().family(), italic=True))
        patient_plt_unit = QLabel("lac / ul")
        patient_plt_unit.setFont(unit_font)
        patient_plt_unit.setFixedHeight(40)
        patient_plt_unit.setContentsMargins(0, 0, 0, 0)


        patient_hiv_plt_layout.addWidget(patient_hiv_label)
        patient_hiv_plt_layout.addWidget(patient_hiv)
        patient_hiv_plt_layout.addWidget(patient_plt_label)
        patient_hiv_plt_layout.addWidget(patient_plt)
        patient_hiv_plt_layout.addWidget(patient_plt_unit)

        patient_hbsag_bsugar_layout = QHBoxLayout()
        patient_hbsag_bsugar_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_hbsag_bsugar_layout.setContentsMargins(0, 0, 0, 0)
        patient_hbsag_bsugar_layout.setSpacing(0)
        patient_hbsag_bsugar_widget = QWidget()
        patient_hbsag_bsugar_widget.setStyleSheet("")
        patient_hbsag_bsugar_widget.setContentsMargins(0, 5, 0, 5)
        patient_hbsag_bsugar_widget.setLayout(patient_hbsag_bsugar_layout)
        patient_hbsag_label = QLabel('HbsAg: ')
        patient_hbsag_label.setFont(entries_font)
        patient_hbsag_label.setFixedHeight(40)
        patient_hbsag_label.setFixedWidth(int(0.06*screen_width))
        patient_hbsag_label.setContentsMargins(0, 0, 0, 0)
        patient_hbsag = QLineEdit(self)
        patient_hbsag.setReadOnly(True)
        patient_hbsag.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_hbsag.setFixedHeight(40)
        patient_hbsag.setFixedWidth(int(0.08*screen_width))
        patient_hbsag.setContentsMargins(0, 0, 0, 0)
        patient_hbsag.setFont(QFont(patient_hbsag.font().family(), italic=True))

        patient_bsugar_label = QLabel('B. Sugar: ')
        patient_bsugar_label.setFont(entries_font)
        patient_bsugar_label.setFixedHeight(40)
        patient_bsugar_label.setFixedWidth(int(0.06*screen_width))
        patient_bsugar_label.setContentsMargins(30, 0, 0, 0)
        patient_bsugar = QLineEdit(self)
        patient_bsugar.setReadOnly(True)
        patient_bsugar.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_bsugar.setFixedHeight(40)
        patient_bsugar.setFixedWidth(int(0.08*screen_width))
        patient_bsugar.setContentsMargins(0, 0, 0, 0)
        patient_bsugar.setFont(QFont(patient_bsugar.font().family(), italic=True))
        patient_bsugar_unit = QLabel("mg / dl")
        patient_bsugar_unit.setFont(unit_font)
        patient_bsugar_unit.setFixedHeight(40)
        patient_bsugar_unit.setContentsMargins(0, 0, 0, 0)
        
        patient_hbsag_bsugar_layout.addWidget(patient_hbsag_label)
        patient_hbsag_bsugar_layout.addWidget(patient_hbsag)
        patient_hbsag_bsugar_layout.addWidget(patient_bsugar_label)
        patient_hbsag_bsugar_layout.addWidget(patient_bsugar)
        patient_hbsag_bsugar_layout.addWidget(patient_bsugar_unit)

        patient_antihcv_gct_layout = QHBoxLayout()
        patient_antihcv_gct_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_antihcv_gct_layout.setContentsMargins(0, 0, 0, 0)
        patient_antihcv_gct_layout.setSpacing(0)
        patient_antihcv_gct_widget = QWidget()
        patient_antihcv_gct_widget.setStyleSheet("")
        patient_antihcv_gct_widget.setContentsMargins(0, 5, 0, 5)
        patient_antihcv_gct_widget.setLayout(patient_antihcv_gct_layout)
        patient_antihcv_label = QLabel('Anti-HCV: ')
        patient_antihcv_label.setFont(entries_font)
        patient_antihcv_label.setFixedHeight(40)
        patient_antihcv_label.setFixedWidth(int(0.06*screen_width))
        patient_antihcv_label.setContentsMargins(0, 0, 0, 0)
        patient_antihcv = QLineEdit(self)
        patient_antihcv.setReadOnly(True)
        patient_antihcv.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_antihcv.setFixedHeight(40)
        patient_antihcv.setFixedWidth(int(0.08*screen_width))
        patient_antihcv.setContentsMargins(0, 0, 0, 0)
        patient_antihcv.setFont(QFont(patient_antihcv.font().family(), italic=True))

        patient_gct_label = QLabel('GCT: ')
        patient_gct_label.setFont(entries_font)
        patient_gct_label.setFixedHeight(40)
        patient_gct_label.setFixedWidth(int(0.06*screen_width))
        patient_gct_label.setContentsMargins(30, 0, 0, 0)
        patient_gct = QLineEdit(self)
        patient_gct.setReadOnly(True)
        patient_gct.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_gct.setFixedHeight(40)
        patient_gct.setFixedWidth(int(0.08*screen_width))
        patient_gct.setContentsMargins(0, 0, 0, 0)
        patient_gct.setFont(QFont(patient_gct.font().family(), italic=True))
        patient_gct_unit = QLabel("mg / dl")
        patient_gct_unit.setFont(unit_font)
        patient_gct_unit.setFixedHeight(40)
        patient_gct_unit.setContentsMargins(0, 0, 0, 0)

        patient_antihcv_gct_layout.addWidget(patient_antihcv_label)
        patient_antihcv_gct_layout.addWidget(patient_antihcv)
        patient_antihcv_gct_layout.addWidget(patient_gct_label)
        patient_antihcv_gct_layout.addWidget(patient_gct)
        patient_antihcv_gct_layout.addWidget(patient_gct_unit)

        patient_igm_gtt_layout = QHBoxLayout()
        patient_igm_gtt_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_igm_gtt_layout.setContentsMargins(0, 0, 0, 0)
        patient_igm_gtt_layout.setSpacing(0)
        patient_igm_gtt_widget = QWidget()
        patient_igm_gtt_widget.setStyleSheet("")
        patient_igm_gtt_widget.setContentsMargins(0, 5, 0, 5)
        patient_igm_gtt_widget.setLayout(patient_igm_gtt_layout)
        patient_igm_label = QLabel('TORCH IgM: ')
        patient_igm_label.setFont(entries_font)
        patient_igm_label.setFixedHeight(40)
        patient_igm_label.setFixedWidth(int(0.06*screen_width))
        patient_igm_label.setContentsMargins(0, 0, 0, 0)
        patient_igm = QLineEdit(self)
        patient_igm.setReadOnly(True)
        patient_igm.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_igm.setFixedHeight(40)
        patient_igm.setFixedWidth(int(0.08*screen_width))
        patient_igm.setContentsMargins(0, 0, 0, 0)
        patient_igm.setFont(QFont(patient_igm.font().family(), italic=True))

        patient_gtt_label = QLabel('GTT: ')
        patient_gtt_label.setFont(entries_font)
        patient_gtt_label.setFixedHeight(40)
        patient_gtt_label.setFixedWidth(int(0.06*screen_width))
        patient_gtt_label.setContentsMargins(30, 0, 0, 0)
        patient_gtt = QLineEdit(self)
        patient_gtt.setReadOnly(True)
        patient_gtt.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_gtt.setFixedHeight(40)
        patient_gtt.setFixedWidth(int(0.08*screen_width))
        patient_gtt.setContentsMargins(0, 0, 0, 0)
        patient_gtt.setFont(QFont(patient_gtt.font().family(), italic=True))
        
        patient_igm_gtt_layout.addWidget(patient_igm_label)
        patient_igm_gtt_layout.addWidget(patient_igm)
        patient_igm_gtt_layout.addWidget(patient_gtt_label)
        patient_igm_gtt_layout.addWidget(patient_gtt)

        patient_igg_bil_layout = QHBoxLayout()
        patient_igg_bil_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_igg_bil_layout.setContentsMargins(0, 0, 0, 0)
        patient_igg_bil_layout.setSpacing(0)
        patient_igg_bil_widget = QWidget()
        patient_igg_bil_widget.setStyleSheet("")
        patient_igg_bil_widget.setContentsMargins(0, 5, 0, 5)
        patient_igg_bil_widget.setLayout(patient_igg_bil_layout)
        patient_igg_label = QLabel('TORCH IgG: ')
        patient_igg_label.setFont(entries_font)
        patient_igg_label.setFixedHeight(40)
        patient_igg_label.setFixedWidth(int(0.06*screen_width))
        patient_igg_label.setContentsMargins(0, 0, 0, 0)
        patient_igg = QLineEdit(self)
        patient_igg.setReadOnly(True)
        patient_igg.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_igg.setFixedHeight(40)
        patient_igg.setFixedWidth(int(0.08*screen_width))
        patient_igg.setContentsMargins(0, 0, 0, 0)
        patient_igg.setFont(QFont(patient_igg.font().family(), italic=True))

        patient_bil_label = QLabel('Bil: ')
        patient_bil_label.setFont(entries_font)
        patient_bil_label.setFixedHeight(40)
        patient_bil_label.setFixedWidth(int(0.06*screen_width))
        patient_bil_label.setContentsMargins(30, 0, 0, 0)
        patient_bil = QLineEdit(self)
        patient_bil.setReadOnly(True)
        patient_bil.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_bil.setFixedHeight(40)
        patient_bil.setFixedWidth(int(0.08*screen_width))
        patient_bil.setContentsMargins(0, 0, 0, 0)
        patient_bil.setFont(QFont(patient_bil.font().family(), italic=True))

        patient_igg_bil_layout.addWidget(patient_igg_label)
        patient_igg_bil_layout.addWidget(patient_igg)
        patient_igg_bil_layout.addWidget(patient_bil_label)
        patient_igg_bil_layout.addWidget(patient_bil)

        patient_urea_sgot_layout = QHBoxLayout()
        patient_urea_sgot_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_urea_sgot_layout.setContentsMargins(0, 0, 0, 0)
        patient_urea_sgot_layout.setSpacing(0)
        patient_urea_sgot_widget = QWidget()
        patient_urea_sgot_widget.setStyleSheet("")
        patient_urea_sgot_widget.setContentsMargins(0, 5, 0, 5)
        patient_urea_sgot_widget.setLayout(patient_urea_sgot_layout)
        patient_urea_label = QLabel('Urea: ')
        patient_urea_label.setFont(entries_font)
        patient_urea_label.setFixedHeight(40)
        patient_urea_label.setFixedWidth(int(0.06*screen_width))
        patient_urea_label.setContentsMargins(0, 0, 0, 0)
        patient_urea = QLineEdit(self)
        patient_urea.setReadOnly(True)
        patient_urea.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_urea.setFixedHeight(40)
        patient_urea.setFixedWidth(int(0.08*screen_width))
        patient_urea.setContentsMargins(0, 0, 0, 0)
        patient_urea.setFont(QFont(patient_urea.font().family(), italic=True))

        patient_sgot_label = QLabel('SGOT: ')
        patient_sgot_label.setFont(entries_font)
        patient_sgot_label.setFixedHeight(40)
        patient_sgot_label.setFixedWidth(int(0.06*screen_width))
        patient_sgot_label.setContentsMargins(30, 0, 0, 0)
        patient_sgot = QLineEdit(self)
        patient_sgot.setReadOnly(True)
        patient_sgot.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_sgot.setFixedHeight(40)
        patient_sgot.setFixedWidth(int(0.08*screen_width))
        patient_sgot.setContentsMargins(0, 0, 0, 0)
        patient_sgot.setFont(QFont(patient_sgot.font().family(), italic=True))

        patient_urea_sgot_layout.addWidget(patient_urea_label)
        patient_urea_sgot_layout.addWidget(patient_urea)
        patient_urea_sgot_layout.addWidget(patient_sgot_label)
        patient_urea_sgot_layout.addWidget(patient_sgot)

        patient_creat_sgpt_layout = QHBoxLayout()
        patient_creat_sgpt_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_creat_sgpt_layout.setContentsMargins(0, 0, 0, 0)
        patient_creat_sgpt_layout.setSpacing(0)
        patient_creat_sgpt_widget = QWidget()
        patient_creat_sgpt_widget.setStyleSheet("")
        patient_creat_sgpt_widget.setContentsMargins(0, 5, 0, 5)
        patient_creat_sgpt_widget.setLayout(patient_creat_sgpt_layout)
        patient_creat_label = QLabel('Creat.: ')
        patient_creat_label.setFont(entries_font)
        patient_creat_label.setFixedHeight(40)
        patient_creat_label.setFixedWidth(int(0.06*screen_width))
        patient_creat_label.setContentsMargins(0, 0, 0, 0)
        patient_creat = QLineEdit(self)
        patient_creat.setReadOnly(True)
        patient_creat.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_creat.setFixedHeight(40)
        patient_creat.setFixedWidth(int(0.08*screen_width))
        patient_creat.setContentsMargins(0, 0, 0, 0)
        patient_creat.setFont(QFont(patient_creat.font().family(), italic=True))
        
        patient_sgpt_label = QLabel('SGPT: ')
        patient_sgpt_label.setFont(entries_font)
        patient_sgpt_label.setFixedHeight(40)
        patient_sgpt_label.setFixedWidth(int(0.06*screen_width))
        patient_sgpt_label.setContentsMargins(30, 0, 0, 0)
        patient_sgpt = QLineEdit(self)
        patient_sgpt.setReadOnly(True)
        patient_sgpt.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_sgpt.setFixedHeight(40)
        patient_sgpt.setFixedWidth(int(0.08*screen_width))
        patient_sgpt.setContentsMargins(0, 0, 0, 0)
        patient_sgpt.setFont(QFont(patient_sgpt.font().family(), italic=True))
        
        patient_creat_sgpt_layout.addWidget(patient_creat_label)
        patient_creat_sgpt_layout.addWidget(patient_creat)
        patient_creat_sgpt_layout.addWidget(patient_sgpt_label)
        patient_creat_sgpt_layout.addWidget(patient_sgpt)

        patient_ua_alkphos_layout = QHBoxLayout()
        patient_ua_alkphos_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_ua_alkphos_layout.setContentsMargins(0, 0, 0, 0)
        patient_ua_alkphos_layout.setSpacing(0)
        patient_ua_alkphos_widget = QWidget()
        patient_ua_alkphos_widget.setStyleSheet("")
        patient_ua_alkphos_widget.setContentsMargins(0, 5, 0, 5)
        patient_ua_alkphos_widget.setLayout(patient_ua_alkphos_layout)
        patient_ua_label = QLabel('U.A. : ')
        patient_ua_label.setFont(entries_font)
        patient_ua_label.setFixedHeight(40)
        patient_ua_label.setFixedWidth(int(0.06*screen_width))
        patient_ua_label.setContentsMargins(0, 0, 0, 0)
        patient_ua = QLineEdit(self)
        patient_ua.setReadOnly(True)
        patient_ua.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_ua.setFixedHeight(40)
        patient_ua.setFixedWidth(int(0.08*screen_width))
        patient_ua.setContentsMargins(0, 0, 0, 0)
        patient_ua.setFont(QFont(patient_ua.font().family(), italic=True))

        patient_alkphos_label = QLabel('Alk. Phos.: ')
        patient_alkphos_label.setFont(entries_font)
        patient_alkphos_label.setFixedHeight(40)
        patient_alkphos_label.setFixedWidth(int(0.06*screen_width))
        patient_alkphos_label.setContentsMargins(30, 0, 0, 0)
        patient_alkphos = QLineEdit(self)
        patient_alkphos.setReadOnly(True)
        patient_alkphos.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_alkphos.setFixedHeight(40)
        patient_alkphos.setFixedWidth(int(0.08*screen_width))
        patient_alkphos.setContentsMargins(0, 0, 0, 0)
        patient_alkphos.setFont(QFont(patient_alkphos.font().family(), italic=True))

        patient_ua_alkphos_layout.addWidget(patient_ua_label)
        patient_ua_alkphos_layout.addWidget(patient_ua)
        patient_ua_alkphos_layout.addWidget(patient_alkphos_label)
        patient_ua_alkphos_layout.addWidget(patient_alkphos)

        patient_dualmar_protein_layout = QHBoxLayout()
        patient_dualmar_protein_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_dualmar_protein_layout.setContentsMargins(0, 0, 0, 0)
        patient_dualmar_protein_layout.setSpacing(0)
        patient_dualmar_protein_widget = QWidget()
        patient_dualmar_protein_widget.setStyleSheet("")
        patient_dualmar_protein_widget.setContentsMargins(0, 5, 0, 5)
        patient_dualmar_protein_widget.setLayout(patient_dualmar_protein_layout)
        patient_dualmar_label = QLabel('Dual Mar. : ')
        patient_dualmar_label.setFont(entries_font)
        patient_dualmar_label.setFixedHeight(40)
        patient_dualmar_label.setFixedWidth(int(0.06*screen_width))
        patient_dualmar_label.setContentsMargins(0, 0, 0, 0)
        patient_dualmar = QLineEdit(self)
        patient_dualmar.setReadOnly(True)
        patient_dualmar.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 9pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_dualmar.setFixedHeight(40)
        patient_dualmar.setFixedWidth(int(0.08*screen_width))
        patient_dualmar.setContentsMargins(0, 0, 0, 0)
        patient_dualmar.setFont(QFont(patient_dualmar.font().family(), italic=True))

        patient_protein_label = QLabel('Protein: ')
        patient_protein_label.setFont(entries_font)
        patient_protein_label.setFixedHeight(40)
        patient_protein_label.setFixedWidth(int(0.06*screen_width))
        patient_protein_label.setContentsMargins(30, 0, 0, 0)
        patient_protein = QLineEdit(self)
        patient_protein.setReadOnly(True)
        patient_protein.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_protein.setFixedHeight(40)
        patient_protein.setFixedWidth(int(0.08*screen_width))
        patient_protein.setContentsMargins(0, 0, 0, 0)
        patient_protein.setFont(QFont(patient_protein.font().family(), italic=True))
        patient_protein_unit = QLabel("gm / dl")
        patient_protein_unit.setFont(unit_font)
        patient_protein_unit.setFixedHeight(40)
        patient_protein_unit.setContentsMargins(0, 0, 0, 0)

        patient_dualmar_protein_layout.addWidget(patient_dualmar_label)
        patient_dualmar_protein_layout.addWidget(patient_dualmar)
        patient_dualmar_protein_layout.addWidget(patient_protein_label)
        patient_dualmar_protein_layout.addWidget(patient_protein)
        patient_dualmar_protein_layout.addWidget(patient_protein_unit)

        patient_triplemar_t3t4tsh_layout = QHBoxLayout()
        patient_triplemar_t3t4tsh_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_triplemar_t3t4tsh_layout.setContentsMargins(0, 0, 0, 0)
        patient_triplemar_t3t4tsh_layout.setSpacing(0)
        patient_triplemar_t3t4tsh_widget = QWidget()
        patient_triplemar_t3t4tsh_widget.setStyleSheet("")
        patient_triplemar_t3t4tsh_widget.setContentsMargins(0, 5, 0, 5)
        patient_triplemar_t3t4tsh_widget.setLayout(patient_triplemar_t3t4tsh_layout)
        patient_triplemar_label = QLabel('Triple Mar. : ')
        patient_triplemar_label.setFont(entries_font)
        patient_triplemar_label.setFixedHeight(40)
        patient_triplemar_label.setFixedWidth(int(0.06*screen_width))
        patient_triplemar_label.setContentsMargins(0, 0, 0, 0)
        patient_triplemar = QLineEdit(self)
        patient_triplemar.setReadOnly(True)
        patient_triplemar.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_triplemar.setFixedHeight(40)
        patient_triplemar.setFixedWidth(int(0.08*screen_width))
        patient_triplemar.setContentsMargins(0, 0, 0, 0)
        patient_triplemar.setFont(QFont(patient_triplemar.font().family(), italic=True))
        
        patient_t3t4tsh_label = QLabel('T3/T4/TSH: ')
        patient_t3t4tsh_label.setFont(entries_font)
        patient_t3t4tsh_label.setFixedHeight(40)
        patient_t3t4tsh_label.setFixedWidth(int(0.06*screen_width))
        patient_t3t4tsh_label.setContentsMargins(30, 0, 0, 0)
        patient_t3t4tsh = QLineEdit(self)
        patient_t3t4tsh.setReadOnly(True)
        patient_t3t4tsh.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_t3t4tsh.setFixedHeight(40)
        patient_t3t4tsh.setFixedWidth(int(0.08*screen_width))
        patient_t3t4tsh.setContentsMargins(0, 0, 0, 0)
        patient_t3t4tsh.setFont(QFont(patient_t3t4tsh.font().family(), italic=True))

        patient_triplemar_t3t4tsh_layout.addWidget(patient_triplemar_label)
        patient_triplemar_t3t4tsh_layout.addWidget(patient_triplemar)
        patient_triplemar_t3t4tsh_layout.addWidget(patient_t3t4tsh_label)
        patient_triplemar_t3t4tsh_layout.addWidget(patient_t3t4tsh)

        patient_quadtest_hba1c_layout = QHBoxLayout()
        patient_quadtest_hba1c_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_quadtest_hba1c_layout.setContentsMargins(0, 0, 0, 0)
        patient_quadtest_hba1c_layout.setSpacing(0)
        patient_quadtest_hba1c_widget = QWidget()
        patient_quadtest_hba1c_widget.setStyleSheet("")
        patient_quadtest_hba1c_widget.setContentsMargins(0, 5, 0, 5)
        patient_quadtest_hba1c_widget.setLayout(patient_quadtest_hba1c_layout)
        patient_quadtest_label = QLabel('Quad Test: ')
        patient_quadtest_label.setFont(entries_font)
        patient_quadtest_label.setFixedHeight(40)
        patient_quadtest_label.setFixedWidth(int(0.06*screen_width))
        patient_quadtest_label.setContentsMargins(0, 0, 0, 0)
        patient_quadtest = QLineEdit(self)
        patient_quadtest.setReadOnly(True)
        patient_quadtest.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_quadtest.setFixedHeight(40)
        patient_quadtest.setFixedWidth(int(0.08*screen_width))
        patient_quadtest.setContentsMargins(0, 0, 0, 0)
        patient_quadtest.setFont(QFont(patient_quadtest.font().family(), italic=True))

        patient_hba1c_label = QLabel('HbA1c: ')
        patient_hba1c_label.setFont(entries_font)
        patient_hba1c_label.setFixedHeight(40)
        patient_hba1c_label.setFixedWidth(int(0.06*screen_width))
        patient_hba1c_label.setContentsMargins(30, 0, 0, 0)
        patient_hba1c = QLineEdit(self)
        patient_hba1c.setReadOnly(True)
        patient_hba1c.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_hba1c.setFixedHeight(40)
        patient_hba1c.setFixedWidth(int(0.08*screen_width))
        patient_hba1c.setContentsMargins(0, 0, 0, 0)
        patient_hba1c.setFont(QFont(patient_hba1c.font().family(), italic=True))

        patient_quadtest_hba1c_layout.addWidget(patient_quadtest_label)
        patient_quadtest_hba1c_layout.addWidget(patient_quadtest)
        patient_quadtest_hba1c_layout.addWidget(patient_hba1c_label)
        patient_quadtest_hba1c_layout.addWidget(patient_hba1c)

        patient_hplc_ict_layout = QHBoxLayout()
        patient_hplc_ict_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_hplc_ict_layout.setContentsMargins(0, 0, 0, 0)
        patient_hplc_ict_layout.setSpacing(0)
        patient_hplc_ict_widget = QWidget()
        patient_hplc_ict_widget.setStyleSheet("")
        patient_hplc_ict_widget.setContentsMargins(0, 5, 0, 5)
        patient_hplc_ict_widget.setLayout(patient_hplc_ict_layout)
        patient_hplc_label = QLabel('HPLC: ')
        patient_hplc_label.setFont(entries_font)
        patient_hplc_label.setFixedHeight(40)
        patient_hplc_label.setFixedWidth(int(0.06*screen_width))
        patient_hplc_label.setContentsMargins(0, 0, 0, 0)
        patient_hplc = QLineEdit(self)
        patient_hplc.setReadOnly(True)
        patient_hplc.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_hplc.setFixedHeight(40)
        patient_hplc.setFixedWidth(int(0.08*screen_width))
        patient_hplc.setContentsMargins(0, 0, 0, 0)
        patient_hplc.setFont(QFont(patient_hplc.font().family(), italic=True))

        patient_ict_label = QLabel('ICT: ')
        patient_ict_label.setFont(entries_font)
        patient_ict_label.setFixedHeight(40)
        patient_ict_label.setFixedWidth(int(0.06*screen_width))
        patient_ict_label.setContentsMargins(30, 0, 0, 0)
        patient_ict = QLineEdit(self)
        patient_ict.setReadOnly(True)
        patient_ict.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_ict.setFixedHeight(40)
        patient_ict.setFixedWidth(int(0.08*screen_width))
        patient_ict.setContentsMargins(0, 0, 0, 0)
        patient_ict.setFont(QFont(patient_ict.font().family(), italic=True))

        patient_hplc_ict_layout.addWidget(patient_hplc_label)
        patient_hplc_ict_layout.addWidget(patient_hplc)
        patient_hplc_ict_layout.addWidget(patient_ict_label)
        patient_hplc_ict_layout.addWidget(patient_ict)

        patient_chestxray_ecg_layout = QHBoxLayout()
        patient_chestxray_ecg_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_chestxray_ecg_layout.setContentsMargins(0, 0, 0, 0)
        patient_chestxray_ecg_layout.setSpacing(0)
        patient_chestxray_ecg_widget = QWidget()
        patient_chestxray_ecg_widget.setStyleSheet("")
        patient_chestxray_ecg_widget.setContentsMargins(0, 5, 0, 5)
        patient_chestxray_ecg_widget.setLayout(patient_chestxray_ecg_layout)
        patient_chestxray_label = QLabel('Chest X-Ray: ')
        patient_chestxray_label.setFont(entries_font)
        patient_chestxray_label.setFixedHeight(40)
        patient_chestxray_label.setFixedWidth(int(0.06*screen_width))
        patient_chestxray_label.setContentsMargins(0, 0, 0, 0)
        patient_chestxray = QLineEdit(self)
        patient_chestxray.setReadOnly(True)
        patient_chestxray.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_chestxray.setFixedHeight(40)
        patient_chestxray.setFixedWidth(int(0.08*screen_width))
        patient_chestxray.setContentsMargins(0, 0, 0, 0)
        patient_chestxray.setFont(QFont(patient_chestxray.font().family(), italic=True))
        
        patient_ecg_label = QLabel('ECG: ')
        patient_ecg_label.setFont(entries_font)
        patient_ecg_label.setFixedHeight(40)
        patient_ecg_label.setFixedWidth(int(0.06*screen_width))
        patient_ecg_label.setContentsMargins(30, 0, 0, 0)
        patient_ecg = QLineEdit(self)
        patient_ecg.setReadOnly(True)
        patient_ecg.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_ecg.setFixedHeight(40)
        patient_ecg.setFixedWidth(int(0.08*screen_width))
        patient_ecg.setContentsMargins(0, 0, 0, 0)
        patient_ecg.setFont(QFont(patient_ecg.font().family(), italic=True))

        patient_chestxray_ecg_layout.addWidget(patient_chestxray_label)
        patient_chestxray_ecg_layout.addWidget(patient_chestxray)
        patient_chestxray_ecg_layout.addWidget(patient_ecg_label)
        patient_chestxray_ecg_layout.addWidget(patient_ecg)

        patient_echo_ptinr_layout = QHBoxLayout()
        patient_echo_ptinr_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_echo_ptinr_layout.setContentsMargins(0, 0, 0, 0)
        patient_echo_ptinr_layout.setSpacing(0)
        patient_echo_ptinr_widget = QWidget()
        patient_echo_ptinr_widget.setStyleSheet("")
        patient_echo_ptinr_widget.setContentsMargins(0, 5, 0, 5)
        patient_echo_ptinr_widget.setLayout(patient_echo_ptinr_layout)
        patient_echo_label = QLabel('ECHO: ')
        patient_echo_label.setFont(entries_font)
        patient_echo_label.setFixedHeight(40)
        patient_echo_label.setFixedWidth(int(0.06*screen_width))
        patient_echo_label.setContentsMargins(0, 0, 0, 0)
        patient_echo = QLineEdit(self)
        patient_echo.setReadOnly(True)
        patient_echo.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_echo.setFixedHeight(40)
        patient_echo.setFixedWidth(int(0.08*screen_width))
        patient_echo.setContentsMargins(0, 0, 0, 0)
        patient_echo.setFont(QFont(patient_echo.font().family(), italic=True))

        patient_ptinr_label = QLabel('PT/INR: ')
        patient_ptinr_label.setFont(entries_font)
        patient_ptinr_label.setFixedHeight(40)
        patient_ptinr_label.setFixedWidth(int(0.06*screen_width))
        patient_ptinr_label.setContentsMargins(30, 0, 0, 0)
        patient_ptinr = QLineEdit(self)
        patient_ptinr.setReadOnly(True)
        patient_ptinr.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
        )
        patient_ptinr.setFixedHeight(40)
        patient_ptinr.setFixedWidth(int(0.08*screen_width))
        patient_ptinr.setContentsMargins(0, 0, 0, 0)
        patient_ptinr.setFont(QFont(patient_ptinr.font().family(), italic=True))

        patient_echo_ptinr_layout.addWidget(patient_echo_label)
        patient_echo_ptinr_layout.addWidget(patient_echo)
        patient_echo_ptinr_layout.addWidget(patient_ptinr_label)
        patient_echo_ptinr_layout.addWidget(patient_ptinr)

        patient_urine_layout = QHBoxLayout()
        patient_urine_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_urine_layout.setContentsMargins(0, 0, 0, 0)
        patient_urine_layout.setSpacing(0)
        patient_urine_widget = QWidget()
        patient_urine_widget.setStyleSheet("")
        patient_urine_widget.setContentsMargins(0, 5, 0, 5)
        patient_urine_widget.setLayout(patient_urine_layout)
        patient_urine_label = QLabel('Urine: ')
        patient_urine_label.setFont(entries_font)
        patient_urine_label.setFixedHeight(40)
        patient_urine_label.setFixedWidth(int(0.06*screen_width))
        patient_urine_label.setContentsMargins(0, 0, 0, 0)
        patient_urine = QPlainTextEdit(self)
        patient_urine.setReadOnly(True)
        patient_urine.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
            "text-align: center;"
        )
        patient_urine.setFixedHeight(80)
        patient_urine.setFixedWidth(int(0.24*screen_width))
        patient_urine.setContentsMargins(0, 0, 0, 0)
        patient_urine.setFont(QFont(patient_urine.font().family(), italic=True))

        patient_urine_layout.addWidget(patient_urine_label)
        patient_urine_layout.addWidget(patient_urine)

        patient_USG_layout = QHBoxLayout()
        patient_USG_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_USG_layout.setContentsMargins(0, 0, 0, 0)
        patient_USG_layout.setSpacing(0)
        patient_USG_widget = QWidget()
        patient_USG_widget.setStyleSheet("")
        patient_USG_widget.setContentsMargins(0, 5, 0, 5)
        patient_USG_widget.setLayout(patient_USG_layout)
        patient_USG_label = QLabel('USG: ')
        patient_USG_label.setFont(entries_font)
        patient_USG_label.setFixedHeight(40)
        patient_USG_label.setFixedWidth(int(0.06*screen_width))
        patient_USG_label.setContentsMargins(0, 0, 0, 0)
        patient_USG = QPlainTextEdit(self)
        patient_USG.setReadOnly(True)
        patient_USG.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
            "text-align: center;"
        )
        patient_USG.setFixedHeight(80)
        patient_USG.setFixedWidth(int(0.24*screen_width))
        patient_USG.setContentsMargins(0, 0, 0, 0)
        patient_USG.setFont(QFont(patient_USG.font().family(), italic=True))

        patient_USG_layout.addWidget(patient_USG_label)
        patient_USG_layout.addWidget(patient_USG)

        patient_other_layout = QHBoxLayout()
        patient_other_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_other_layout.setContentsMargins(0, 0, 0, 10)
        patient_other_layout.setSpacing(0)
        patient_other_widget = QWidget()
        patient_other_widget.setStyleSheet("")
        patient_other_widget.setContentsMargins(0, 5, 0, 10)
        patient_other_widget.setLayout(patient_other_layout)
        patient_other_label = QLabel('Other: ')
        patient_other_label.setFont(entries_font)
        patient_other_label.setFixedHeight(40)
        patient_other_label.setFixedWidth(int(0.06*screen_width))
        patient_other_label.setContentsMargins(0, 0, 0, 10)
        patient_other = QPlainTextEdit(self)
        patient_other.setReadOnly(True)
        patient_other.setStyleSheet(
            "background-color: rgb(250, 250, 250);"
            "color: rgb(0, 0, 0);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border: none;"
            "border-radius: 20px;"
            "text-align: center;"
        )
        patient_other.setFixedHeight(80)
        patient_other.setFixedWidth(int(0.24*screen_width))
        patient_other.setContentsMargins(0, 0, 0, 0)
        patient_other.setFont(QFont(patient_other.font().family(), italic=True))

        patient_other_layout.addWidget(patient_other_label)
        patient_other_layout.addWidget(patient_other)

        patient_complaint_history_header_layout = QHBoxLayout()
        patient_complaint_history_header_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        patient_complaint_history_header_layout.setContentsMargins(0, 0, 0, 0)
        patient_complaint_history_header_layout.setSpacing(0)
        patient_complaint_history_header_widget = QWidget()
        patient_complaint_history_header_widget.setStyleSheet("")
        patient_complaint_history_header_widget.setContentsMargins(0, 5, 0, 5)
        patient_complaint_history_header_widget.setLayout(patient_complaint_history_header_layout)

        patient_complaints_history_label = QLabel('Complaints History')
        patient_complaints_history_label.setStyleSheet("color: rgb(0, 0, 0); font: 15pt \"Poppins\"; font-weight: bold;")
        patient_complaints_history_label.setFixedHeight(80)
        patient_complaints_history_label.setContentsMargins(0, 0, 0, 0)
        patient_complaints_history_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)


        patient_complaints_edit_button = QPushButton()
        edit_button_image_address = resource_path('design/images/edit.png')
        edit_button_image = QPixmap(edit_button_image_address)
        edit_button_image = edit_button_image.scaledToWidth(30)
        patient_complaints_edit_button.setIcon(QIcon(edit_button_image))
        patient_complaints_edit_button.setIconSize(edit_button_image.rect().size())
        patient_complaints_edit_button.setCursor(Qt.PointingHandCursor)
        patient_complaints_edit_button.setFlat(True)
        patient_complaints_edit_button.clicked.connect(lambda : self.complaints_edit(patient_complaints_add_widget, patient_complaints_text, patient_lmp, patient_pregnant, patient_complaints_edit_button, patient_complaints_save_button))

        patient_complaints_save_button = QPushButton()
        save_button_image_address = resource_path('design/images/confirm.png')
        save_button_image = QPixmap(save_button_image_address)
        save_button_image = save_button_image.scaledToWidth(30)
        patient_complaints_save_button.setIcon(QIcon(save_button_image))
        patient_complaints_save_button.setIconSize(save_button_image.rect().size())
        patient_complaints_save_button.setCursor(Qt.PointingHandCursor)
        patient_complaints_save_button.setFlat(True)
        patient_complaints_save_button.setVisible(False)
        patient_complaints_save_button.clicked.connect(lambda : self.complaints_save(patient_complaints_add_widget, patient_complaints_text, patient_lmp, patient_pregnant, patient_complaints_edit_button, patient_complaints_save_button))

        patient_complaint_history_header_layout.addWidget(patient_complaints_history_label)
        patient_complaint_history_header_layout.addWidget(patient_complaints_edit_button)
        patient_complaint_history_header_layout.addWidget(patient_complaints_save_button)


        patient_complaints_add_layout = QHBoxLayout()
        patient_complaints_add_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_complaints_add_layout.setContentsMargins(0, 0, 0, 0)
        patient_complaints_add_layout.setSpacing(0)
        patient_complaints_add_widget = QWidget()
        patient_complaints_add_widget.setStyleSheet("")
        patient_complaints_add_widget.setContentsMargins(0, 5, 0, 5)
        patient_complaints_add_widget.setLayout(patient_complaints_add_layout)
        patient_complaints_label = QLabel('Complaint: ')
        patient_complaints_label.setFont(entries_font)
        patient_complaints_label.setFixedHeight(40)
        patient_complaints_label.setFixedWidth(int(0.06*screen_width))
        patient_complaints_label.setContentsMargins(0, 0, 0, 0)
        # add patient_complaints_option from a text file or database
        f = open(resource_path('design/lists/complaints.txt'), 'r')
        patient_complaints_options = f.read().split('\n')
        f.close()
        patient_complaints_options.sort()
        patient_complaints_options.append('Other')
        patient_complaints_dropdown = QComboBox()
        patient_complaints_dropdown.addItems(patient_complaints_options)
        patient_complaints_dropdown.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
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
        patient_complaints_dropdown.setFixedHeight(40)
        patient_complaints_dropdown.setFixedWidth(int(0.08*screen_width))
        patient_complaints_dropdown.setContentsMargins(0, 0, 0, 0)
        patient_complaints_dropdown.setFont(QFont(patient_complaints_dropdown.font().family(), italic=True))

        patient_complaints_text = QLineEdit(self)
        patient_complaints_text.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_complaints_text.setVisible(False)
        patient_complaints_text.setFixedHeight(40)
        patient_complaints_text.setFixedWidth(int(0.3*screen_width))
        patient_complaints_text.setContentsMargins(0, 0, 0, 0)
        patient_complaints_text.setFont(QFont(patient_complaints_text.font().family(), italic=True))

        patient_complaint_duration = QLineEdit(self)
        patient_complaint_duration.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_complaint_duration.setFixedHeight(40)
        patient_complaint_duration.setFixedWidth(int(0.08*screen_width))
        patient_complaint_duration.setContentsMargins(0, 0, 0, 0)
        patient_complaint_duration.setFont(QFont(patient_complaint_duration.font().family(), italic=True))
        patient_complaint_duration.setPlaceholderText('Duration')

        patient_complaint_add_button = QPushButton('Add')
        patient_complaint_add_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245, 245, 245);"
            "font: 10pt \"Poppins\";"
            "border-radius: 20px;"
        )
        patient_complaint_add_button.setFixedHeight(40)
        patient_complaint_add_button.setFixedWidth(int(0.08*screen_width))
        patient_complaint_add_button.setContentsMargins(0, 0, 0, 0)
        patient_complaint_add_button.clicked.connect(lambda: self.add_complaint(patient_complaints_table, patient_complaints_dropdown.currentText(), patient_complaint_duration.text(), patient_complaints_text.text(), patient_complaints_options, patient_complaints_dropdown))
        patient_complaints_add_layout.addWidget(patient_complaints_label)
        patient_complaints_add_layout.addWidget(patient_complaints_dropdown)
        patient_complaints_dropdown.currentIndexChanged.connect(lambda: self.complaint_dropdown_changed(patient_complaints_dropdown.currentText(), patient_complaints_text))
        patient_complaints_add_layout.addWidget(patient_complaint_duration)
        patient_complaints_add_layout.addWidget(patient_complaint_add_button)

        patient_complaints_table = QTableWidget()
        patient_complaints_table.setStyleSheet(
            "QTableWidget {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"

            # Hide the box at the side
            "QTableWidget::drop-down {"
            "    border: none;"
            "}"
        )
        patient_complaints_table.setFixedHeight(200)
        patient_complaints_table.setFixedWidth(int(0.24*screen_width))
        patient_complaints_table.setViewportMargins(0, 10, 0, 0)
        patient_complaints_table.setContentsMargins(0, 10, 0, 0)
        patient_complaints_table.setFont(QFont(patient_complaints_table.font().family(), italic=True))
        patient_complaints_table.setColumnCount(2)
        patient_complaints_table.setRowCount(0)
        
        if patient_complaints_table.rowCount() == 0:
            patient_complaints_table.setVisible(False)
        
        patient_complaints_table.setHorizontalHeaderLabels(['Complaint', 'Duration'])
        patient_complaints_table.horizontalHeader().setStyleSheet(
            "QHeaderView {"
            "    background-color: rgb(67, 79, 194);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    border-radius: 20px;"
            "}"
        )
        patient_complaints_table.horizontalHeader().setFixedHeight(40)
        patient_complaints_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        patient_complaints_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        patient_complaints_table.verticalHeader().hide()
        patient_complaints_table.setShowGrid(False)
        patient_complaints_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        patient_complaints_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        patient_complaints_table.setSelectionMode(QAbstractItemView.SingleSelection)
        patient_complaints_table.setAlternatingRowColors(True)
        patient_complaints_table.setStyleSheet(
            "QTableView {"
            "    background-color: rgb(255, 255, 255);"
            "    alternate-background-color: rgb(240, 240, 240);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
        )
        patient_complaints_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    border: 0px;"
            "    background: #f0f0f0;"
            "    width: 10px;"
            "    margin: 0px 0px 0px 0px;"
            "}"

            "QScrollBar::handle:vertical {"
            "    background: #666666;"
            "    min-height: 20px;"
            "}"

            "QScrollBar::add-line:vertical {"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"

            "QScrollBar::sub-line:vertical {"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
            "}"
        )
        patient_complaints_table.itemDoubleClicked.connect(lambda item: self.delete_row(item, patient_complaints_table, patient_complaints_edit_button.isVisible()))

        patient_complaints_add_widget.setVisible(False)

        patient_lmp_layout = QHBoxLayout()
        patient_lmp_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_lmp_layout.setContentsMargins(0, 0, 0, 0)
        patient_lmp_layout.setSpacing(0)
        patient_lmp_widget = QWidget()
        patient_lmp_widget.setStyleSheet("")
        patient_lmp_widget.setContentsMargins(0, 5, 0, 5)
        patient_lmp_widget.setLayout(patient_lmp_layout)
        patient_lmp_label = QLabel('LMP: ')
        patient_lmp_label.setFont(entries_font)
        patient_lmp_label.setFixedHeight(40)
        patient_lmp_label.setFixedWidth(int(0.06*screen_width))
        patient_lmp_label.setContentsMargins(0, 0, 0, 0)
        patient_lmp = QDateEdit(self)
        patient_lmp.setReadOnly(True)
        patient_lmp.setDisplayFormat("dd-MM-yyyy")  # Set the desired date format
        patient_lmp.setStyleSheet("""
            QDateEdit {
                background-color: rgb(255, 255, 255);
                color: rgb(40, 40, 40);
                font: 10pt "Poppins";
                padding: 5px;
                border-radius: 20px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
            }

            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid rgb(40, 40, 40);
            }
        """)
        patient_lmp.setFixedHeight(40)
        patient_lmp.setFixedWidth(int(0.08*screen_width))
        patient_lmp.setContentsMargins(0, 0, 0, 0)

        patient_lmp_layout.addWidget(patient_lmp_label)
        patient_lmp_layout.addWidget(patient_lmp)

        patient_pregnant_layout = QHBoxLayout()
        patient_pregnant_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_pregnant_layout.setContentsMargins(0, 0, 0, 0)
        patient_pregnant_layout.setSpacing(0)
        patient_pregnant_widget = QWidget()
        patient_pregnant_widget.setStyleSheet("")
        patient_pregnant_widget.setContentsMargins(0, 5, 0, 5)
        patient_pregnant_widget.setLayout(patient_pregnant_layout)
        patient_pregnant_label = QLabel('Pregnant: ')
        patient_pregnant_label.setFont(entries_font)
        patient_pregnant_label.setFixedHeight(40)
        patient_pregnant_label.setFixedWidth(int(0.06*screen_width))
        patient_pregnant_label.setContentsMargins(0, 0, 0, 0)
        patient_pregnant = QComboBox()
        patient_pregnant.addItems(['Yes', 'No'])
        patient_pregnant.setEditable(True)
        patient_pregnant.setCurrentText("No")
        patient_pregnant.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
            # Hide the box at the side
            "QComboBox::drop-down {"
            "    border: none;"
            "}"
        )
        patient_pregnant.setFixedHeight(40)
        patient_pregnant.setFixedWidth(int(0.08*screen_width))
        patient_pregnant.setContentsMargins(0, 0, 0, 0)
        patient_pregnant.setFont(QFont(patient_pregnant.font().family(), italic=True))
        patient_pregnant.currentIndexChanged.connect(lambda: self.pregnant_dropdown_changed(patient_pregnant.currentText(), patient_lmp, patient_edd, patient_pog, patient_edd_widget, patient_pog_widget))

        patient_pregnant_layout.addWidget(patient_pregnant_label)
        patient_pregnant_layout.addWidget(patient_pregnant)

        patient_edd_layout = QHBoxLayout()
        patient_edd_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_edd_layout.setContentsMargins(0, 0, 0, 0)
        patient_edd_layout.setSpacing(0)
        patient_edd_widget = QWidget()
        patient_edd_widget.setStyleSheet("")
        patient_edd_widget.setContentsMargins(0, 5, 0, 5)
        patient_edd_widget.setLayout(patient_edd_layout)
        patient_edd_label = QLabel('EDD: ')
        patient_edd_label.setFont(entries_font)
        patient_edd_label.setFixedHeight(40)
        patient_edd_label.setFixedWidth(int(0.06*screen_width))
        patient_edd_label.setContentsMargins(0, 0, 0, 0)
        patient_edd = QDateEdit(self)
        patient_edd.setReadOnly(True)
        patient_edd.setDisplayFormat("dd-MM-yyyy")  # Set the desired date format
        patient_edd.setStyleSheet("""
            QDateEdit {
                background-color: rgb(255, 255, 255);
                color: rgb(40, 40, 40);
                font: 10pt "Poppins";
                padding: 5px;
                border-radius: 20px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
            }
                                  
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid rgb(40, 40, 40);
            }
        """)
        patient_edd.setFixedHeight(40)
        patient_edd.setFixedWidth(int(0.08*screen_width))
        patient_edd.setContentsMargins(0, 0, 0, 0)
        
        patient_edd_layout.addWidget(patient_edd_label)
        patient_edd_layout.addWidget(patient_edd)
        patient_edd_widget.setVisible(False)

        patient_pog_layout = QHBoxLayout()  
        patient_pog_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_pog_layout.setContentsMargins(0, 0, 0, 0)
        patient_pog_layout.setSpacing(0)
        patient_pog_widget = QWidget()
        patient_pog_widget.setStyleSheet("")
        patient_pog_widget.setContentsMargins(0, 5, 0, 5)
        patient_pog_widget.setLayout(patient_pog_layout)
        patient_pog_label = QLabel('POG: ')
        patient_pog_label.setFont(entries_font)
        patient_pog_label.setFixedHeight(40)
        patient_pog_label.setFixedWidth(int(0.06*screen_width))
        patient_pog_label.setContentsMargins(0, 0, 0, 0)
        patient_pog = QLineEdit(self)
        patient_pog.setReadOnly(True)
        patient_pog.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_pog.setFixedHeight(40)
        patient_pog.setFixedWidth(int(0.1*screen_width))
        patient_pog.setContentsMargins(0, 0, 0, 0)
        patient_pog.setFont(QFont(patient_pog.font().family(), italic=True))

        patient_pog_layout.addWidget(patient_pog_label)
        patient_pog_layout.addWidget(patient_pog)
        patient_pog_widget.setVisible(False)

        patient_history_header_layout = QHBoxLayout()
        patient_history_header_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        patient_history_header_layout.setContentsMargins(0, 0, 0, 0)
        patient_history_header_layout.setSpacing(0)
        patient_history_header_widget = QWidget()
        patient_history_header_widget.setStyleSheet("")
        patient_history_header_widget.setContentsMargins(0, 5, 0, 5)
        patient_history_header_widget.setLayout(patient_history_header_layout)

        patient_history_label = QLabel('History')
        patient_history_label.setStyleSheet("color: rgb(0, 0, 0); font: 15pt \"Poppins\"; font-weight: bold;")
        patient_history_label.setFixedHeight(80)
        patient_history_label.setContentsMargins(0, 0, 0, 0)
        patient_history_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        patient_history_edit_button = QPushButton()
        edit_button_image_address = resource_path('design/images/edit.png')
        edit_button_image = QPixmap(edit_button_image_address)
        edit_button_image = edit_button_image.scaledToWidth(30)
        patient_history_edit_button.setIcon(QIcon(edit_button_image))
        patient_history_edit_button.setIconSize(edit_button_image.rect().size())
        patient_history_edit_button.setCursor(Qt.PointingHandCursor)
        patient_history_edit_button.setFlat(True)
        patient_history_edit_button.clicked.connect(lambda : self.history_edit(patient_obst_history_add_widget, patient_family_history_add_widget, patient_past_history_add_widget, patient_history_edit_button, patient_history_save_button))

        patient_history_save_button = QPushButton()
        save_button_image_address = resource_path('design/images/confirm.png')
        save_button_image = QPixmap(save_button_image_address)
        save_button_image = save_button_image.scaledToWidth(30)
        patient_history_save_button.setIcon(QIcon(save_button_image))
        patient_history_save_button.setIconSize(save_button_image.rect().size())
        patient_history_save_button.setCursor(Qt.PointingHandCursor)
        patient_history_save_button.setFlat(True)
        patient_history_save_button.setVisible(False)
        patient_history_save_button.clicked.connect(lambda : self.history_save(patient_obst_history_add_widget, patient_family_history_add_widget, patient_past_history_add_widget, patient_history_edit_button, patient_history_save_button))

        patient_history_header_layout.addWidget(patient_history_label)
        patient_history_header_layout.addWidget(patient_history_edit_button)
        patient_history_header_layout.addWidget(patient_history_save_button)

        patient_obst_history_layout = QVBoxLayout()
        patient_obst_history_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_obst_history_layout.setContentsMargins(0, 0, 0, 0)
        patient_obst_history_layout.setSpacing(0)
        patient_obst_history_widget = QWidget()
        patient_obst_history_widget.setStyleSheet("")
        patient_obst_history_widget.setContentsMargins(0, 5, 0, 5)
        patient_obst_history_widget.setLayout(patient_obst_history_layout)
        patient_obst_history_label = QLabel('Obstetric History: ')
        patient_obst_history_label.setFont(entries_font)
        patient_obst_history_label.setFixedHeight(40)
        patient_obst_history_label.setContentsMargins(0, 0, 0, 0)
        patient_obst_history_add = QHBoxLayout()
        patient_obst_history_add.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_obst_history_add.setContentsMargins(0, 0, 0, 0)
        patient_obst_history_add.setSpacing(0)
        patient_obst_history_add_widget = QWidget()
        patient_obst_history_add_widget.setStyleSheet("")
        patient_obst_history_add_widget.setContentsMargins(0, 5, 0, 5)
        patient_obst_history_add_widget.setLayout(patient_obst_history_add)
        patient_obst_history_text = QLineEdit(self)
        patient_obst_history_text.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_obst_history_text.setFixedHeight(40)
        patient_obst_history_text.setFixedWidth(int(0.24*screen_width))
        patient_obst_history_text.setContentsMargins(0, 0, 0, 0)
        patient_obst_history_text.setFont(QFont(patient_obst_history_text.font().family(), italic=True))

        patient_obst_history_add_button = QPushButton('Add')
        patient_obst_history_add_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245, 245, 245);"
            "font: 10pt \"Poppins\";"
            "border-radius: 20px;"
        )
        patient_obst_history_add_button.setFixedHeight(40)
        patient_obst_history_add_button.setFixedWidth(int(0.08*screen_width))
        patient_obst_history_add_button.setContentsMargins(0, 0, 0, 0)
        patient_obst_history_add_button.clicked.connect(lambda: self.add_obst_history(patient_obst_history_table, patient_obst_history_text.text()))
        
        patient_obst_history_layout.addWidget(patient_obst_history_label)
        patient_obst_history_add.addWidget(patient_obst_history_text)
        patient_obst_history_add.addWidget(patient_obst_history_add_button)
        patient_obst_history_add_widget.setVisible(False)

        patient_obst_history_table = QTableWidget()
        patient_obst_history_table.setFixedHeight(200)
        patient_obst_history_table.setFixedWidth(int(0.24*screen_width))
        patient_obst_history_table.setViewportMargins(0, 10, 0, 0)
        patient_obst_history_table.setContentsMargins(0, 10, 0, 0)
        patient_obst_history_table.setFont(QFont(patient_obst_history_table.font().family(), italic=True))
        patient_obst_history_table.setColumnCount(1)
        patient_obst_history_table.setRowCount(0)

        if patient_obst_history_table.rowCount() == 0:
            patient_obst_history_table.setVisible(False)

        patient_obst_history_table.setHorizontalHeaderLabels(['Obstetric History'])
        patient_obst_history_table.horizontalHeader().setStyleSheet(
            "QHeaderView {"
            "    background-color: rgb(67, 79, 194);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    border-radius: 20px;"
            "}"
        )
        patient_obst_history_table.horizontalHeader().setFixedHeight(40)
        patient_obst_history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        patient_obst_history_table.verticalHeader().hide()
        patient_obst_history_table.setShowGrid(False)
        patient_obst_history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        patient_obst_history_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        patient_obst_history_table.setSelectionMode(QAbstractItemView.SingleSelection)
        patient_obst_history_table.setAlternatingRowColors(True)
        patient_obst_history_table.setStyleSheet(
            "QTableView {"
            "    background-color: rgb(255, 255, 255);"
            "    alternate-background-color: rgb(240, 240, 240);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
        )
        patient_obst_history_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    border: 0px;"
            "    background: #f0f0f0;"
            "    width: 10px;"
            "    margin: 0px 0px 0px 0px;"
            "}"

            "QScrollBar::handle:vertical {"
            "    background: #666666;"
            "    min-height: 20px;"
            "}"

            "QScrollBar::add-line:vertical {"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"

            "QScrollBar::sub-line:vertical {"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
            "}"
        )
        patient_obst_history_table.itemDoubleClicked.connect(lambda item: self.delete_obst_row(item, patient_obst_history_table, patient_history_edit_button.isVisible()))

        patient_family_history_layout = QHBoxLayout()
        patient_family_history_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_family_history_layout.setContentsMargins(0, 0, 0, 0)
        patient_family_history_layout.setSpacing(0)
        patient_family_history_widget = QWidget()
        patient_family_history_widget.setStyleSheet("")
        patient_family_history_widget.setContentsMargins(0, 5, 0, 5)
        patient_family_history_widget.setLayout(patient_family_history_layout)
        patient_family_history_label = QLabel('Family History: ')
        patient_family_history_label.setFont(entries_font)
        patient_family_history_label.setFixedHeight(40)
        patient_family_history_label.setContentsMargins(0, 0, 0, 0)
        patient_family_history_add = QHBoxLayout()
        patient_family_history_add.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_family_history_add.setContentsMargins(0, 0, 0, 0)
        patient_family_history_add.setSpacing(0)
        patient_family_history_add_widget = QWidget()
        patient_family_history_add_widget.setStyleSheet("")
        patient_family_history_add_widget.setContentsMargins(0, 5, 0, 5)
        patient_family_history_add_widget.setLayout(patient_family_history_add)
        patient_family_history_text = QLineEdit(self)
        patient_family_history_text.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_family_history_text.setFixedHeight(40)
        patient_family_history_text.setFixedWidth(int(0.24*screen_width))
        patient_family_history_text.setContentsMargins(0, 0, 0, 0)
        patient_family_history_text.setFont(QFont(patient_family_history_text.font().family(), italic=True))

        patient_family_history_add_button = QPushButton('Add')
        patient_family_history_add_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245, 245, 245);"
            "font: 10pt \"Poppins\";"
            "border-radius: 20px;"
        )
        patient_family_history_add_button.setFixedHeight(40)
        patient_family_history_add_button.setFixedWidth(int(0.08*screen_width))
        patient_family_history_add_button.setContentsMargins(0, 0, 0, 0)
        patient_family_history_add_button.clicked.connect(lambda: self.add_family_history(patient_family_history_table, patient_family_history_text.text()))

        patient_family_history_layout.addWidget(patient_family_history_label)
        patient_family_history_add.addWidget(patient_family_history_text)
        patient_family_history_add.addWidget(patient_family_history_add_button)
        patient_family_history_add_widget.setVisible(False)

        patient_family_history_table = QTableWidget()
        patient_family_history_table.setFixedHeight(200)
        patient_family_history_table.setFixedWidth(int(0.24*screen_width))
        patient_family_history_table.setViewportMargins(0, 10, 0, 0)
        patient_family_history_table.setContentsMargins(0, 10, 0, 0)
        patient_family_history_table.setFont(QFont(patient_family_history_table.font().family(), italic=True))
        patient_family_history_table.setColumnCount(1)
        patient_family_history_table.setRowCount(0)

        if patient_family_history_table.rowCount() == 0:
            patient_family_history_table.setVisible(False)

        patient_family_history_table.setHorizontalHeaderLabels(['Family History'])
        patient_family_history_table.horizontalHeader().setStyleSheet(
            "QHeaderView {"
            "    background-color: rgb(67, 79, 194);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    border-radius: 20px;"
            "}"
        )
        patient_family_history_table.horizontalHeader().setFixedHeight(40)
        patient_family_history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        patient_family_history_table.verticalHeader().hide()
        patient_family_history_table.setShowGrid(False)
        patient_family_history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        patient_family_history_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        patient_family_history_table.setSelectionMode(QAbstractItemView.SingleSelection)
        patient_family_history_table.setAlternatingRowColors(True)
        patient_family_history_table.setStyleSheet(
            "QTableView {"
            "    background-color: rgb(255, 255, 255);"
            "    alternate-background-color: rgb(240, 240, 240);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
        )
        patient_family_history_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    border: 0px;"
            "    background: #f0f0f0;"
            "    width: 10px;"
            "    margin: 0px 0px 0px 0px;"
            "}"

            "QScrollBar::handle:vertical {"
            "    background: #666666;"
            "    min-height: 20px;"
            "}"

            "QScrollBar::add-line:vertical {"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"

            "QScrollBar::sub-line:vertical {"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
            "}"
        )
        patient_family_history_table.itemDoubleClicked.connect(lambda item: self.delete_family_row(item, patient_family_history_table, patient_history_edit_button.isVisible()))

        patient_past_history_layout = QHBoxLayout()
        patient_past_history_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_past_history_layout.setContentsMargins(0, 0, 0, 0)
        patient_past_history_layout.setSpacing(0)
        patient_past_history_widget = QWidget()
        patient_past_history_widget.setStyleSheet("")
        patient_past_history_widget.setContentsMargins(0, 5, 0, 5)
        patient_past_history_widget.setLayout(patient_past_history_layout)
        patient_past_history_label = QLabel('Past History: ')
        patient_past_history_label.setFont(entries_font)
        patient_past_history_label.setFixedHeight(40)
        patient_past_history_label.setContentsMargins(0, 0, 0, 0)
        patient_past_history_add = QHBoxLayout()
        patient_past_history_add.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_past_history_add.setContentsMargins(0, 0, 0, 0)
        patient_past_history_add.setSpacing(0)
        patient_past_history_add_widget = QWidget()
        patient_past_history_add_widget.setStyleSheet("")
        patient_past_history_add_widget.setContentsMargins(0, 5, 0, 5)
        patient_past_history_add_widget.setLayout(patient_past_history_add)
        patient_past_history_text = QLineEdit(self)
        patient_past_history_text.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_past_history_text.setFixedHeight(40)
        patient_past_history_text.setFixedWidth(int(0.24*screen_width))
        patient_past_history_text.setContentsMargins(0, 0, 0, 0)
        patient_past_history_text.setFont(QFont(patient_past_history_text.font().family(), italic=True))

        patient_past_history_add_button = QPushButton('Add')
        patient_past_history_add_button.setStyleSheet(
            "background-color: rgb(67, 79, 194);"
            "color: rgb(245, 245, 245);"
            "font: 10pt \"Poppins\";"
            "border-radius: 20px;"
        )
        patient_past_history_add_button.setFixedHeight(40)
        patient_past_history_add_button.setFixedWidth(int(0.08*screen_width))
        patient_past_history_add_button.setContentsMargins(0, 0, 0, 0)
        patient_past_history_add_button.clicked.connect(lambda: self.add_past_history(patient_past_history_table, patient_past_history_text.text()))

        patient_past_history_layout.addWidget(patient_past_history_label)
        patient_past_history_add.addWidget(patient_past_history_text)
        patient_past_history_add.addWidget(patient_past_history_add_button)
        patient_past_history_add_widget.setVisible(False)

        patient_past_history_table = QTableWidget()
        patient_past_history_table.setFixedHeight(200)
        patient_past_history_table.setFixedWidth(int(0.24*screen_width))
        patient_past_history_table.setViewportMargins(0, 10, 0, 0)
        patient_past_history_table.setContentsMargins(0, 10, 0, 0)
        patient_past_history_table.setFont(QFont(patient_past_history_table.font().family(), italic=True))
        patient_past_history_table.setColumnCount(1)
        patient_past_history_table.setRowCount(0)

        if patient_past_history_table.rowCount() == 0:
            patient_past_history_table.setVisible(False)

        patient_past_history_table.setHorizontalHeaderLabels(['Past History'])
        patient_past_history_table.horizontalHeader().setStyleSheet(
            "QHeaderView {"
            "    background-color: rgb(67, 79, 194);"
            "    color: rgb(0, 0, 0);"
            "    font: 10pt \"Poppins\";"
            "    border-radius: 20px;"
            "}"
        )
        patient_past_history_table.horizontalHeader().setFixedHeight(40)
        patient_past_history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        patient_past_history_table.verticalHeader().hide()
        patient_past_history_table.setShowGrid(False)
        patient_past_history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        patient_past_history_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        patient_past_history_table.setSelectionMode(QAbstractItemView.SingleSelection)
        patient_past_history_table.setAlternatingRowColors(True)
        patient_past_history_table.setStyleSheet(
            "QTableView {"
            "    background-color: rgb(255, 255, 255);"
            "    alternate-background-color: rgb(240, 240, 240);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
        )
        patient_past_history_table.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    border: 0px;"
            "    background: #f0f0f0;"
            "    width: 10px;"
            "    margin: 0px 0px 0px 0px;"
            "}"

            "QScrollBar::handle:vertical {"
            "    background: #666666;"
            "    min-height: 20px;"
            "}"

            "QScrollBar::add-line:vertical {"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"

            "QScrollBar::sub-line:vertical {"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
            "}"
        )
        patient_past_history_table.itemDoubleClicked.connect(lambda item: self.delete_past_row(item, patient_past_history_table, patient_history_edit_button.isVisible()))

        patient_payment_header_layout = QHBoxLayout()
        patient_payment_header_layout.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        patient_payment_header_layout.setContentsMargins(0, 0, 0, 0)
        patient_payment_header_layout.setSpacing(0)
        patient_payment_header_widget = QWidget()
        patient_payment_header_widget.setStyleSheet("")
        patient_payment_header_widget.setContentsMargins(0, 5, 0, 5)
        patient_payment_header_widget.setLayout(patient_payment_header_layout)

        patient_payment_label = QLabel('Payment')
        patient_payment_label.setStyleSheet("color: rgb(0, 0, 0); font: 15pt \"Poppins\"; font-weight: bold;")
        patient_payment_label.setFixedHeight(80)
        patient_payment_label.setContentsMargins(0, 0, 0, 0)
        patient_payment_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        patient_payment_edit_button = QPushButton()
        edit_button_image_address = resource_path('design/images/edit.png')
        edit_button_image = QPixmap(edit_button_image_address)
        edit_button_image = edit_button_image.scaledToWidth(30)
        patient_payment_edit_button.setIcon(QIcon(edit_button_image))
        patient_payment_edit_button.setIconSize(edit_button_image.rect().size())
        patient_payment_edit_button.setCursor(Qt.PointingHandCursor)
        patient_payment_edit_button.setFlat(True)
        patient_payment_edit_button.clicked.connect(lambda : self.payment_edit(patient_payment, patient_payment_mode, patient_payment_edit_button, patient_payment_save_button))

        patient_payment_save_button = QPushButton()
        save_button_image_address = resource_path('design/images/confirm.png')
        save_button_image = QPixmap(save_button_image_address)
        save_button_image = save_button_image.scaledToWidth(30)
        patient_payment_save_button.setIcon(QIcon(save_button_image))
        patient_payment_save_button.setIconSize(save_button_image.rect().size())
        patient_payment_save_button.setCursor(Qt.PointingHandCursor)
        patient_payment_save_button.setFlat(True)
        patient_payment_save_button.setVisible(False)
        patient_payment_save_button.clicked.connect(lambda : self.payment_save(patient_payment, patient_payment_mode, patient_payment_edit_button, patient_payment_save_button))

        patient_payment_header_layout.addWidget(patient_payment_label)
        patient_payment_header_layout.addWidget(patient_payment_edit_button)
        patient_payment_header_layout.addWidget(patient_payment_save_button)

        patient_payment_layout = QHBoxLayout()
        patient_payment_layout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        patient_payment_layout.setContentsMargins(0, 0, 0, 0)
        patient_payment_layout.setSpacing(0)
        patient_payment_widget = QWidget()
        patient_payment_widget.setStyleSheet("")
        patient_payment_widget.setContentsMargins(0, 5, 0, 5)
        patient_payment_widget.setLayout(patient_payment_layout)
        patient_payment_label = QLabel('Payment: ')
        patient_payment_label.setFont(entries_font)
        patient_payment_label.setFixedHeight(40)
        patient_payment_label.setFixedWidth(int(0.06*screen_width))
        patient_payment_label.setContentsMargins(0, 0, 0, 0)
        patient_payment = QLineEdit(self)
        patient_payment.setReadOnly(True)
        patient_payment.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
            "color: rgb(40, 40, 40);"
            "font: 10pt \"Poppins\";"
            "padding: 5px;"
            "border-radius: 20px;"
        )
        patient_payment.setFixedHeight(40)
        patient_payment.setFixedWidth(int(0.08*screen_width))
        patient_payment.setContentsMargins(0, 0, 0, 0)
        patient_payment.setFont(QFont(patient_payment.font().family(), italic=True))

        patient_payment_mode_label = QLabel('By: ')
        patient_payment_mode_label.setFont(entries_font)
        patient_payment_mode_label.setFixedHeight(40)
        patient_payment_mode_label.setFixedWidth(int(0.06*screen_width))
        patient_payment_mode_label.setContentsMargins(0, 0, 0, 0)
        patient_payment_mode = QComboBox()
        patient_payment_mode.addItems(['Cash', 'UPI'])
        patient_payment_mode.setEditable(True)
        patient_payment_mode.setCurrentText("Cash")
        patient_payment_mode.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
            # Hide the box at the side
            "QComboBox::drop-down {"
            "    border: none;"
            "}"
        )
        patient_payment_mode.setFixedHeight(40)
        patient_payment_mode.setFixedWidth(int(0.08*screen_width))
        patient_payment_mode.setContentsMargins(0, 0, 0, 0)
        patient_payment_mode.setFont(QFont(patient_payment_mode.font().family(), italic=True))
        
        patient_payment_layout.addWidget(patient_payment_label)
        patient_payment_layout.addWidget(patient_payment)
        patient_payment_layout.addWidget(patient_payment_mode_label)
        patient_payment_layout.addWidget(patient_payment_mode)



        patient_details_layout.addWidget(patient_details_heading_widget)
        patient_details_layout.addWidget(patient_name_widget)
        patient_details_layout.addWidget(patient_guardian_widget)
        patient_details_layout.addWidget(patient_occ_gen_widget)
        patient_details_layout.addWidget(patient_number1_widget)
        patient_details_layout.addWidget(patient_number2_widget)
        patient_details_layout.addWidget(patient_address_widget)
        patient_details_layout.addWidget(patient_age_widget)
        patient_details_layout.addWidget(patient_weight_height_widget)
        patient_details_layout.addWidget(patient_report_heading_widget)
        patient_details_layout.addWidget(patient_blood_group_widget)
        patient_details_layout.addWidget(patient_vdlr_TLC_widget)
        patient_details_layout.addWidget(patient_hiv_plt_widget)
        patient_details_layout.addWidget(patient_hbsag_bsugar_widget)
        patient_details_layout.addWidget(patient_antihcv_gct_widget)
        patient_details_layout.addWidget(patient_igm_gtt_widget)
        patient_details_layout.addWidget(patient_igg_bil_widget)
        patient_details_layout.addWidget(patient_urea_sgot_widget)
        patient_details_layout.addWidget(patient_creat_sgpt_widget)
        patient_details_layout.addWidget(patient_ua_alkphos_widget)
        patient_details_layout.addWidget(patient_dualmar_protein_widget)
        patient_details_layout.addWidget(patient_triplemar_t3t4tsh_widget)
        patient_details_layout.addWidget(patient_quadtest_hba1c_widget)
        patient_details_layout.addWidget(patient_hplc_ict_widget)
        patient_details_layout.addWidget(patient_chestxray_ecg_widget)
        patient_details_layout.addWidget(patient_echo_ptinr_widget)
        patient_details_layout.addWidget(patient_urine_widget)
        patient_details_layout.addWidget(patient_USG_widget)
        patient_details_layout.addWidget(patient_other_widget)
        patient_details_layout.addWidget(patient_complaint_history_header_widget)
        patient_details_layout.addWidget(patient_complaints_add_widget)
        patient_details_layout.addWidget(patient_complaints_text)
        patient_details_layout.addWidget(patient_complaints_table)
        patient_details_layout.addWidget(patient_lmp_widget)
        patient_details_layout.addWidget(patient_pregnant_widget)
        patient_details_layout.addWidget(patient_edd_widget)
        patient_details_layout.addWidget(patient_pog_widget)
        patient_details_layout.addWidget(patient_history_header_widget)
        patient_details_layout.addWidget(patient_obst_history_widget)
        patient_details_layout.addWidget(patient_obst_history_add_widget)
        patient_details_layout.addWidget(patient_obst_history_table)
        patient_details_layout.addWidget(patient_family_history_widget)
        patient_details_layout.addWidget(patient_family_history_add_widget)
        patient_details_layout.addWidget(patient_family_history_table)
        patient_details_layout.addWidget(patient_past_history_widget)
        patient_details_layout.addWidget(patient_past_history_add_widget)
        patient_details_layout.addWidget(patient_past_history_table)
        patient_details_layout.addWidget(patient_payment_header_widget)
        patient_details_layout.addWidget(patient_payment_widget)

        


        scroll_area.setWidget(patient_details_widget)

        scroll_bar = scroll_area.verticalScrollBar()
        scroll_bar.setStyleSheet(
            "QScrollBar:vertical {"
            "    border: 0px;"
            "    background: #f0f0f0;"
            "    width: 10px;"
            "    margin: 0px 0px 0px 0px;"
            "}"

            "QScrollBar::handle:vertical {"
            "    background: #666666;"
            "    min-height: 20px;"
            "}"

            "QScrollBar::add-line:vertical {"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"

            "QScrollBar::sub-line:vertical {"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
            "}"
        )


        content_top_layout.addWidget(welcome_label)
        content_top_layout.addWidget(search_widget)
        content_top_layout.addWidget(logout_button)

        content_bottom_left_layout.addWidget(filter_widget)
        content_bottom_left_layout.addWidget(patient_table)
        content_bottom_left_layout.addWidget(diagnostic_scroll_area)

        content_bottom_right_layout.addWidget(scroll_area)

        content_bottom_layout.addWidget(content_bottom_left_widget)
        content_bottom_layout.addWidget(content_bottom_right_widget)

        content_layout.addWidget(content_top_widget)
        content_layout.addWidget(content_bottom_widget)

        layout.addWidget(menu_widget)
        layout.addWidget(content_widget)

        self.setLayout(layout)

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

    def populate_table(self, table, filter_parameter):
        # Fetch data from the database
        data = Database().table_filtered_data(filter_parameter)

        # Clear existing data from the table
        table.clearContents()
        table.setRowCount(len(data))
        
        # Assuming your data has the same number of columns for each row
        if data:
            table.setColumnCount(len(data[0]))
            table.verticalHeader().setVisible(False)
            # Populate the table with the fetched data
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    table.setItem(row_idx, col_idx, item)

    def row_single_clicked(self, item, patient_table, first_name,middle_name, last_name, guardian, occupation, phone_num1, phone_num2,
                           sex,address1,age, dob,obstretic_his, family_his, past_his):
        db = Database()
        row = item.row()
        patient_id = patient_table.item(row, 0).text()
        print(f"Row {row} clicked once. Patient ID: {patient_id}")
        first_name.setText(patient_table.item(row, 1).text())
        middle_name.setText(db.get_middleName(row+1))
        last_name.setText(db.get_lastName(row+1))
        guardian.setText(db.get_guardian(row+1))
        occupation.setText(db.get_occupation(row+1))
        phone_num1.setText(db.get_phoneNum1(row+1))
        phone_num2.setText(db.get_phoneNum2(row+1))
        sex.setText(db.get_sex(row+1))
        address1.setPlainText(f"{db.get_address1(row+1)}\n{db.get_address2(row+1)}")
        dob.setText(db.get_dob(row+1).strftime("%d/%m/%Y"))
        print(f"{type(db.get_dob(row+1))} dob")
        age.setText(str(db.get_age(row+1)))
        # blood_group.setText(db.get_blood_group(row+1))
        obstretic_his.setText(db.get_obstetricHis(row+1))
        family_his.setText(db.get_familyHis(row+1))
        past_his.setText(db.get_pastHis(row+1))
        # notes.setText(db.get_notes(row+1))


    def row_double_clicked(self, item, patient_table, filter, diagnostics):
        row = item.row()
        patient_id = patient_table.item(row, 0).text()
        print(f"Row {row} double-clicked. Patient ID: {patient_id}")
        patient_table.setVisible(False)
        filter.setVisible(False)
        diagnostics.setVisible(True)

    def back_button_clicked(self, patient_table, filter_widget, diagnostic_scroll_area):
        patient_table.setVisible(True)
        filter_widget.setVisible(True)
        diagnostic_scroll_area.setVisible(False)

    def update_clinical_findings_file(self,text):
        completer = text.completer()
        if completer:
            model = completer.model()
            clinical_findings = [model.data(model.index(i, 0), Qt.DisplayRole) for i in range(model.rowCount())]

    def add_clinical_findings(self, clinical_findings_add_text, clinical_findings_add_button, clinical_findings_table):
        clinical_findings_table.setVisible(True)
        clinical_findings_table.insertRow(clinical_findings_table.rowCount())
        clinical_findings_table.setItem(clinical_findings_table.rowCount()-1, 0, QTableWidgetItem(clinical_findings_add_text.text()))
        clinical_findings_add_text.setText(clinical_findings_add_text.text().strip())
        file = open(resource_path('design/lists/clinical_findings.txt'), 'r')
        file_text = file.read()
        if clinical_findings_add_text.text().strip() not in file_text:
            file = open(resource_path('design/lists/clinical_findings.txt'), 'a')
            file.write(f"\n{clinical_findings_add_text.text()}")
        file.close()

    def complaint_dropdown_changed(self, complaint, text):
        if complaint == 'Other':
            text.setVisible(True)
        else:
            text.setVisible(False)

    def add_complaint(self, table, complaint, duration, other, options, dropdown):

        if complaint == 'Other' and other == '':
            self.show_error("Please enter a valid complaint")
            return
        elif duration == '':
            self.show_error("Please enter a valid duration")
            return
        
        table.setVisible(True)
        table.insertRow(table.rowCount())
        if complaint == 'Other':
            table.setItem(table.rowCount()-1, 0, QTableWidgetItem(other))
            if other not in options:
                other = other.strip()
                other = other[0].upper() + other[1:].lower()
                f = open(resource_path('design/lists/complaints.txt'), 'a')
                f.write(f"{other}\n")
                f.close()
                f = open(resource_path('design/lists/complaints.txt'), 'r')
                options = f.read().splitlines()
                options.sort()
                options.append('Other')
                f.close()
                dropdown.clear()
                dropdown.addItems(options)
        else:
            table.setItem(table.rowCount()-1, 0, QTableWidgetItem(complaint))
        table.setItem(table.rowCount()-1, 1, QTableWidgetItem(duration))

    def delete_row(self, item, table, edit_button_visible):
        if edit_button_visible:
            return
        row = item.row()
        table.removeRow(row)
        if table.rowCount() == 0:
            table.setVisible(False)

    def details_edit(self, first_name, middle_name, last_name, guardian_name, occupation, gender, number1, number2, address, age, dob, weight, height, details_edit_button, details_save_button):
        first_name.setReadOnly(False)
        middle_name.setReadOnly(False)
        last_name.setReadOnly(False)
        guardian_name.setReadOnly(False)
        occupation.setReadOnly(False)
        gender.setReadOnly(False)
        number1.setReadOnly(False)
        number2.setReadOnly(False)
        address.setReadOnly(False)
        age.setReadOnly(False)
        dob.setReadOnly(False)
        weight.setReadOnly(False)
        height.setReadOnly(False)
        details_edit_button.setVisible(False)
        details_save_button.setVisible(True)

    def details_save(self, first_name, middle_name, last_name, guardian_name, occupation, gender, number1, number2, address, age, dob, weight, height, details_edit_button, details_save_button):
        first_name.setReadOnly(True)
        middle_name.setReadOnly(True)
        last_name.setReadOnly(True)
        guardian_name.setReadOnly(True)
        occupation.setReadOnly(True)
        gender.setReadOnly(True)
        number1.setReadOnly(True)
        number2.setReadOnly(True)
        address.setReadOnly(True)
        age.setReadOnly(True)
        dob.setReadOnly(True)
        weight.setReadOnly(True)
        height.setReadOnly(True)
        details_edit_button.setVisible(True)
        details_save_button.setVisible(False)

    def report_edit(self, blood_group, hb, vdlr, TLC, hiv, plt, hbsag, bsugar, antihcv, gct, igm, gtt, igg, bil, urea, sgot, creat, sgpt, ua, alkphos, dualmar, protein, triplemar, t3t4tsh, quadtest, hba1c, hplc, ict, chestxray, ecg, echo, ptinr, urine, USG, other, report_edit_button, report_save_button):
        blood_group.setReadOnly(False)
        hb.setReadOnly(False)
        vdlr.setReadOnly(False)
        TLC.setReadOnly(False)
        hiv.setReadOnly(False)
        plt.setReadOnly(False)
        hbsag.setReadOnly(False)
        bsugar.setReadOnly(False)   
        antihcv.setReadOnly(False)
        gct.setReadOnly(False)
        igm.setReadOnly(False)
        gtt.setReadOnly(False)
        igg.setReadOnly(False)
        bil.setReadOnly(False)
        urea.setReadOnly(False)
        sgot.setReadOnly(False)
        creat.setReadOnly(False)
        sgpt.setReadOnly(False)
        ua.setReadOnly(False)
        alkphos.setReadOnly(False)
        dualmar.setReadOnly(False)
        protein.setReadOnly(False)
        triplemar.setReadOnly(False)
        t3t4tsh.setReadOnly(False)
        quadtest.setReadOnly(False)
        hba1c.setReadOnly(False)
        hplc.setReadOnly(False)
        ict.setReadOnly(False)
        chestxray.setReadOnly(False)
        ecg.setReadOnly(False)
        echo.setReadOnly(False)
        ptinr.setReadOnly(False)
        urine.setReadOnly(False)
        USG.setReadOnly(False)
        other.setReadOnly(False)
        report_edit_button.setVisible(False)
        report_save_button.setVisible(True)

    def report_save(self, blood_group, hb, vdlr, TLC, hiv, plt, hbsag, bsugar, antihcv, gct, igm, gtt, igg, bil, urea, sgot, creat, sgpt, ua, alkphos, dualmar, protein, triplemar, t3t4tsh, quadtest, hba1c, hplc, ict, chestxray, ecg, echo, ptinr, urine, USG, other, report_edit_button, report_save_button):
        blood_group.setReadOnly(True)
        hb.setReadOnly(True)
        vdlr.setReadOnly(True)
        TLC.setReadOnly(True)
        hiv.setReadOnly(True)
        plt.setReadOnly(True)
        hbsag.setReadOnly(True)
        bsugar.setReadOnly(True)   
        antihcv.setReadOnly(True)
        gct.setReadOnly(True)
        igm.setReadOnly(True)
        gtt.setReadOnly(True)
        igg.setReadOnly(True)
        bil.setReadOnly(True)
        urea.setReadOnly(True)
        sgot.setReadOnly(True)
        creat.setReadOnly(True)
        sgpt.setReadOnly(True)
        ua.setReadOnly(True)
        alkphos.setReadOnly(True)
        dualmar.setReadOnly(True)
        protein.setReadOnly(True)
        triplemar.setReadOnly(True)
        t3t4tsh.setReadOnly(True)
        quadtest.setReadOnly(True)
        hba1c.setReadOnly(True)
        hplc.setReadOnly(True)
        ict.setReadOnly(True)
        chestxray.setReadOnly(True)
        ecg.setReadOnly(True)
        echo.setReadOnly(True)
        ptinr.setReadOnly(True)
        urine.setReadOnly(True)
        USG.setReadOnly(True)
        other.setReadOnly(True)
        report_edit_button.setVisible(True)
        report_save_button.setVisible(False)

    def complaints_edit(self, complaints_add_widget, complaints_text, lmp, pregnant, complaints_edit_button, complaints_save_button):
        complaints_add_widget.setVisible(True)
        lmp.setReadOnly(False)
        pregnant.setEditable(False)
        complaints_edit_button.setVisible(False)
        complaints_save_button.setVisible(True)

    def complaints_save(self, complaints_add_widget, complaints_text, lmp, pregnant,complaints_edit_button, complaints_save_button):
        complaints_add_widget.setVisible(False)
        if complaints_text.isVisible():
            complaints_text.setVisible(False)
        lmp.setReadOnly(True)
        pregnant.setEditable(True)
        pregnant.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
            # Hide the box at the side
            "QComboBox::drop-down {"
            "    border: none;"
            "}"
        )
        complaints_edit_button.setVisible(True)
        complaints_save_button.setVisible(False)

    def pregnant_dropdown_changed(self, pregnant, lmp_widget, edd_widget, pog_widget, edd_widget_vis, pog_widget_vis):
        if pregnant == 'Yes':
            edd_widget_vis.setVisible(True)
            pog_widget_vis.setVisible(True)
        else:
            edd_widget_vis.setVisible(False)
            pog_widget_vis.setVisible(False)

        lmp_date = lmp_widget.date().addDays(280)  # Assuming 280 days for a standard pregnancy
        pog_days = lmp_widget.date().daysTo(QDateTime.currentDateTime().date())
        pog_weeks = pog_days // 7
        pog_remainder_days = pog_days % 7

        # Update the widgets
        edd_widget.setDate(lmp_date)
        pog_widget.setText(f"{pog_weeks} weeks {pog_remainder_days} days")

    def history_edit(self, obst_history_add, family_history_add, past_history_add, history_edit_button, history_save_button):
        obst_history_add.setVisible(True)
        family_history_add.setVisible(True)
        past_history_add.setVisible(True)
        history_edit_button.setVisible(False)
        history_save_button.setVisible(True)

    def history_save(self, obst_history_add, family_history_add, past_history_add, history_edit_button, history_save_button):
        obst_history_add.setVisible(False)
        family_history_add.setVisible(False)
        past_history_add.setVisible(False)
        history_edit_button.setVisible(True)
        history_save_button.setVisible(False)

    def add_obst_history(self, obst_history_table, obst_history_text):
        if obst_history_text == '':
            self.show_error("Please enter a valid obstetric history")
            return
        obst_history_table.setVisible(True)
        obst_history_table.insertRow(obst_history_table.rowCount())
        obst_history_table.setItem(obst_history_table.rowCount()-1, 0, QTableWidgetItem(obst_history_text))

    def delete_obst_row(self, item, patient_obst_history_table, edit_button_visible):
        if edit_button_visible:
            return
        row = item.row()
        patient_obst_history_table.removeRow(row)
        if patient_obst_history_table.rowCount() == 0:
            patient_obst_history_table.setVisible(False)

    def add_family_history(self, family_history_table, family_history_text):
        if family_history_text == '':
            self.show_error("Please enter a valid family history")
            return
        family_history_table.setVisible(True)
        family_history_table.insertRow(family_history_table.rowCount())
        family_history_table.setItem(family_history_table.rowCount()-1, 0, QTableWidgetItem(family_history_text))

    def delete_family_row(self, item, patient_family_history_table, edit_button_visible):
        if edit_button_visible:
            return
        row = item.row()
        patient_family_history_table.removeRow(row)
        if patient_family_history_table.rowCount() == 0:
            patient_family_history_table.setVisible(False)

    def add_past_history(self, past_history_table, past_history_text):
        if past_history_text == '':
            self.show_error("Please enter a valid past history")
            return
        past_history_table.setVisible(True)
        past_history_table.insertRow(past_history_table.rowCount())
        past_history_table.setItem(past_history_table.rowCount()-1, 0, QTableWidgetItem(past_history_text))

    def delete_past_row(self, item, patient_past_history_table, edit_button_visible):
        if edit_button_visible:
            return
        row = item.row()
        patient_past_history_table.removeRow(row)
        if patient_past_history_table.rowCount() == 0:
            patient_past_history_table.setVisible(False)

    def payment_edit(self, payment, payment_mode, payment_edit_button, payment_save_button):
        payment.setReadOnly(False)
        payment_mode.setEditable(False)
        payment_edit_button.setVisible(False)
        payment_save_button.setVisible(True)

    def payment_save(self, payment, payment_mode, payment_edit_button, payment_save_button):
        payment.setReadOnly(True)
        payment_mode.setEditable(True)
        payment_mode.setStyleSheet(
            "QComboBox {"
            "    background-color: rgb(255, 255, 255);"
            "    color: rgb(40, 40, 40);"
            "    font: 10pt \"Poppins\";"
            "    padding: 5px;"
            "    border-radius: 20px;"
            "}"
            # Hide the box at the side
            "QComboBox::drop-down {"
            "    border: none;"
            "}"
        )
        payment_edit_button.setVisible(True)
        payment_save_button.setVisible(False)


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
