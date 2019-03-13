from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Server(object):
	"""
	"""

	def __init__(self, host, port):
		"""
		"""

		self.host = host
		self.port = port

		self.clientes = []
		self.codificacao = "utf8"

		self.tcp = socket(AF_INET, SOCK_STREAM)
		self.tcp.bind((self.host, self.port))

	def accept_incoming_connections(self):
		"""
		"""

		while 1:
			client, client_address = self.tcp.accept()
			print("%s:%s conectou." % client_address)

			mensagem = "Chat$Você entrou no servidor!"
			client.send(bytes(mensagem, self.codificacao))

			self.clientes.append((client, client_address))

			Thread(target=self.handle_client, args=(client, )).start()


	def handle_client(self, client):
		"""
		"""

		while 1:
			try:
				Thread(target=self.send).start()
				mensagem = client.recv(1024).decode(self.codificacao)
				print(mensagem)

			except RuntimeError as error:
				print(error)


			
			

	def send(self):
		"""
		"""

		while 1:

			prefixo = "Servidor$"
			mensagem = input("")

			self.broadcast(prefixo, mensagem)



	def broadcast(self, prefixo, mensagem):
		"""
		"""

		for sock in self.clientes:
			try:
				sock[0].send(bytes(prefixo + mensagem, self.codificacao))

			except BrokenPipeError as error:
				self.clientes.remove(sock)
				print(sock[1] + "saiu.")
				
			except ConnectionResetError as error:
				self.clientes.remove(sock)
				print(sock[1] + "saiu.")
	

host = "191.52.7.30" #"192.168.0.14"
port = 33333
rodando = False
while not rodando:
	try:
		servidor = Server(host, port)
		servidor.tcp.listen(10)
		rodando = True
	except:
		port += 1
	
	

accept_thread = Thread(target=servidor.accept_incoming_connections)
accept_thread.start()
accept_thread.join()

