from socket import *
from threading import Thread

class Send:
	def __init__(self):
		self.__msg=''
		self.new=True
		self.con= []
	def put(self,msg):
		self.__msg=msg
		if self.con != None:
			#envia um mensagem atravez de uma conexão socket
			for i in self.con:
				i.send(str.encode(self.__msg))
	def get(self):
		return self.__msg
	def loop(self):
		return self.new

class Server(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.send = Send()

		self.listaClientes = []
		self.codificacao = "utf8"

		self.server = socket(AF_INET, SOCK_STREAM)
		self.server.bind((self.host, self.port))
		while True:
			self.server.listen(-1)
			self.con, self.cliente = self.server.accept()
			self.send.con.append(self.con)

			Thread(target = self.enviar)

	def enviar(self):
		while True:
			for i in send.con:
				#aceita uma mensagem
				msg=i.recv(1024)
				if not msg: break
				print(str(self.cliente, msg,'utf-8'))
				send.put(str(self.cliente, msg, 'utf-8'))







servidor = Server('0.0.0.0',5001)
#while True:
#	pass