from socket import *

serverPort = 12000
serverName = '192.168.1.101'
BUFFSIZE = 1024

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Connect successfully')

while True:
    data = input('Please input the sending message: ')
    if len(data) > 0:
        clientSocket.send(data.encode())
    else:
        break
    data = clientSocket.recv(BUFFSIZE).decode()
    if len(data) > 0:
        print('From server: ', data)
    else:
        break

clientSocket.close()
print('Connection closed')
