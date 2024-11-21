import time,os
try:

    import pyperclip  #pip install pyperclip
except:
    os.system('pip install pyperclip')
import win32gui
import win32con
import threading
import sys
from PySide6.QtCore import QCoreApplication,QMetaObject, QRect,Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QCheckBox, QLabel
from PySide6.QtWidgets import QApplication, QMainWindow


os.system('color A')
win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MINIMIZE)
def on_key_event(selected_text):
    if selected_text:
        os.system('cls')
        print("Selected Code:\n")
        print(selected_text)
        with open("test_code.py", 'w') as file:
            file.write(f"try:\n")
            new1 = selected_text.splitlines()
            for abhi in new1:
                file.write(f"    {abhi}\n")
            file.write("    abhi_x = input('press enter to close')\n")
            file.write("except Exception as err:\n    print(err)\n")
            file.write("    abhi_x = input('press enter to close')")
    #time.sleep(1)
    os.system('start python test_code.py')


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(172, 23)
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(122, 2, 16, 20))
        self.checkBox.setChecked(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-1, 0, 131, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(76, 255, 178);")
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"PyEcecuter v1.1", None))
    # retranslateUi


class window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.move(0,0)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        
start11 = False
def monitor_clipboard():
    global start11
    last_clipboard_content = None
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != last_clipboard_content:
            if widget.form.checkBox.isChecked():

                if start11 ==True:
                    on_key_event(clipboard_content)
            start11 = True  
            last_clipboard_content = clipboard_content
        time.sleep(1)
threading.Thread(target=monitor_clipboard).start()
os.system('cls')

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    widget = window()
    widget.show()
    print('Just copy the Python code to execute')
    sys.exit(app.exec())