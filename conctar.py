from socket import *

ip = '0.0.0.0'
port= 33334

server = socket(AF_INET, SOCK_STREAM)

server.bind((ip,port))

server.listen(5)

obj, cliente = server.accept()

print(cliente)