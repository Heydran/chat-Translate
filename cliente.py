from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
	
#classe para manipular o socket
class Send:
	def __init__(self):
		self.__msg = ''
		self.new = True
		self.con = None
		
	def put(self, msg):
		self.__msg = msg
		if self.con != None:
			#envia um mensagem atravez de uma conexão socket
			self.con.send(str.encode(self.__msg))
	
	def get(self):
		return self.__msg
	
	def loop(self):
		return self.new

class Cliente(object):
	def __init__(self,  idioma, host = "localhost", port = 5014):
		self.idioma = idioma
		self.msg = None
		self.cliente = socket(AF_INET,SOCK_STREAM)
		self.send = Send()
		self.tem_mensagem = False
		self.processo = Thread(target=self.esperar,args=(self.cliente,self.send,host, port)).start()

	def enviar_msg(self, msg):
		self.send.put(msg)


	def esperar(self, tcp, send, host='localhost', port=5010):
		destino = (host,port)
		#conecta a um servidor
		tcp.connect(destino)
			
		while send.loop():
			print('Conectado a ',host,'.')
			#atribui a conexão ao manipulador
			send.con=tcp
			while send.loop():
				#aceita uma mensagem
				self.msg=tcp.recv(1024)
				if not self.msg: break
	def pegar_msg(self):
		if self.msg: 
			return self.msg.decode()

	def resetar(self):
		self.msg = None