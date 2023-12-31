from PyQt5.QtGui import QTextCharFormat, QColor, QFont
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

font_path = resource_path('design/Poppins/Poppins-Regular.ttf')

# style for heading
heading_font = QFont()
heading_font.setFamily("Poppins")
heading_font.setPointSize(20)
heading_font.setBold(True)

heading_text_color = QColor(0, 0, 0)

entries_font = QFont()
entries_font.setFamily("Poppins")
entries_font.setPointSize(10)
entries_font.setBold(True)

unit_font = QFont()
unit_font.setFamily("Poppins")
unit_font.setPointSize(10)
unit_font.setBold(False)