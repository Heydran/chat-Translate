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
		self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.server.bind((self.host, self.port))
		while True:
			self.server.listen(-1)
			self.con, self.cliente = self.server.accept()
			self.send.con.append(self.con)

			Thread(target = self.enviar, args = (self.con,)).start()

	def enviar(self, con):
		while True:
			#aceita uma mensagem
			msg=con.recv(1024)
			if not msg: break
			print(str(msg.decode()))
			self.send.put(str(msg.decode()))

servidor = Server("191.52.7.39",5014)
#while True:
#	pass