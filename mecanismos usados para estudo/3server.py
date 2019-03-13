from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
	
#classe para manipular o socket
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

class ClientHandler():

	def __init__(self, tcp, send, host='', port=5000):
		self.con = None
		self.cliente = None
		self.tcp = tcp
		self.send = send
		self.host = host
		self.port = port
		self.lista_threads = []

	#função esperar - Thread
	def esperar(self):
		self.origem=(self.host,self.port)
		#cria um vinculo
		self.tcp.bind(self.origem)
		#deixa em espera
		self.tcp.listen(-1)
		while True:
			#aceita um conexão
			self.con, self.cliente=tcp.accept()
			print('Cliente ', self.cliente, ' conectado!')
			#atribui a conexão ao manipulador
			send.con.append(self.con)
			
			thread = Thread(target=self.receber)
			self.lista_threads.append(thread)
			thread.start()

	def receber(self):

		while True:
			for i in send.con:
				#aceita uma mensagem
				msg=i.recv(1024)
				if not msg: break
				print(str(msg,'utf-8'))
				send.put(str(msg, 'utf-8'))
	

if __name__ == '__main__':
	#cria um socket
	tcp = socket(AF_INET,SOCK_STREAM)
	send = Send()
	#cria um Thread e usa a função esperar com dois argumentos
	CH = ClientHandler(tcp,send)
	processo = Thread(target=CH.esperar)
	processo.start()
		
	print('Iniciando o servidor de chat!')
	print('Aguarde alguém conectar!')
		
	
	while True:
		send.put(input())
		
		
	processo.join()
	tcp.close()
	exit()