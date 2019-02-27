from socket import *
class Server(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port

		self.clientes = []
		self.codificacao = "utf8"

		self.tcp = socket(AF_INET, SOCK_STREAM)
		self.tcp.bind((self.host, self.port))










servidor = Server('0.0.0.0',33335)
servidor.tcp.listen(10)
cliente, ipcliente = servidor.tcp.accept()
print('conectou')