import datetime
import time
import threading
import requests
from PyQt5 import QtWidgets
import design


class MesseangerApp(QtWidgets.QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send)
        thread = threading.Thread(target=self.receiv)
        thread.start()

    def send(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.plainTextEdit.toPlainText()
        if not username or not password or not text:
            return
        try:
            requests.post('http://127.0.0.1:5000/send', json={'username': username, 'password': password, 'text': text})
        except requests.exceptions.ConnectionError:
            pass
        self.plainTextEdit.clear()
    def receiv(self):
        last_received = 0
        while True:
            response = requests.get('http://127.0.0.1:5000/messages',
                        params={'after': last_received}
            )
            if response.status_code == 200:
                messages = response.json()['messages']
                for message in messages:
                    username = message['username']
                    time_1 = datetime.datetime.fromtimestamp(message['time'])
                    time_str = time_1.strftime('%Y-%m-%d %H:%M:%S')
                    text = message['text']
                    self.textBrowser_2.append(f'{username} {time_str}')
                    self.textBrowser_2.append(text)
                    self.textBrowser_2.append('')
                    last_received = message['time']
            time.sleep(1)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MesseangerApp()
    window.show()
    app.exec_()
