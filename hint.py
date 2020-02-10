# pip install PyQt5
# pyuic5 MessagerWindow.ui -o design.py
from PyQt5 import QtWidgets
import  clientui
class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow)
    def __init__(self):
        super().__init__()
        self.stupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()

