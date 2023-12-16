from PyQt5.QtGui import QTextCharFormat, QColor, QFont
import sys, os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

font_path = resource_path('design/Poppins/Poppins-Regular.ttf')

heading_font = QFont()
heading_font.setFamily("Poppins")
heading_font.setPointSize(10)
heading_font.setBold(True)

heading_text_color = QColor(0, 0, 0)
