import requests
'''response = requests.get('http://127.0.0.1/messages')
print(response.status_code)
print(response.text)
print(response.json())'''
print('Input username')
username = input()
print('Input password')
password = input()
while True:
    text = input()
    response = requests.post('http://127.0.0.1:5000/send',
                             json={'username': username, 'password': password, 'text': text}
                             )
    if response.status_code == 200:
        print('Message sent')
        print('For help send !help')
        print()
