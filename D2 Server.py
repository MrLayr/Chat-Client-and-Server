'''Сделла небольшую доработку ввиде команд в чате, предполагаю, что их должен видеть не весь чат, а только пользователь который их вводил, до этого пока не додумался =)'''
from flask import Flask, request
import datetime
import time
app = Flask(__name__)
messages = [
    {'username': 'Jhon', 'time': time.time(), 'text': 'Hallo'},
    {'username': 'Mary', 'time': time.time(), 'text': 'Hallo to'},
]
password_storege = {
    'Jhon': '1234',
    'Mary': '4321'

}
command_list = {
    '!online': 'Количество пользователей онлайн',
    '!help': 'Показать весь список команд с описанием'
 }
@app.route("/") #декораторы
def hello():
    return "Hello, World!"
@app.route("/status")
def status():
    my_date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return {
        'status': True,
        'time': my_date,
        'Massege_count': len(messages),
        'Members_count': len(password_storege)


    }
@app.route("/send", methods=['POST'])
def send_view():
    '''
    JSON {'username': str , 'password': str, 'text': str}
    username ,text - не пустые строки
    :return: {'ok': bool}
    '''
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']
    if username not in password_storege:
        password_storege[username] = password

    if not isinstance(username , str) or len(username) == 0:
        return {'ok': False}
    if not isinstance(text , str) or len(text) == 0:
        return {'ok': False}
    if password_storege[username] != password:
        return {'ok': False}
    if text == '!online':
        messages.append({'username': 'System answer for '+username+' request', 'time': time.time(), 'text': 'Now online: '+str(len(password_storege))})
        return {'ok': True}
    if text == '!help':
        messages.append({'username': 'HELP', 'time': time.time(), 'text': command_list})
        return {'ok': True}
    messages.append({'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}

@app.route("/messages")
def messages_method():
    '''
    Param after - отметка времени после которой будут сообщения в результате
    :return: {'messages': [
     {'username': str, 'time': float, 'text': str}
    ]}
    '''
    after = float(request.args['after'])
    filtred_messages = [message for message in messages if message['time'] > after]
    return{'messages': filtred_messages}
if __name__ == '__main__':
    app.run()
