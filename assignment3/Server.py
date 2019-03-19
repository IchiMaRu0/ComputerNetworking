from socket import *

serverPort = 12000
serverName = '192.168.1.101'
BUFFSIZE = 1024
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)

print('Waiting for connection...')
connectionSocket, addr = serverSocket.accept()
print('Connection from client: ', addr)

while True:
    data = connectionSocket.recv(BUFFSIZE).decode()
    if len(data) > 0 and data != 'quit':
        connectionSocket.send(('Message received').encode())
    else:
        break

connectionSocket.close()
print('Connection closed')