from googletrans import Translator, LANGUAGES
from socket import socket
from threading import Thread
#print(LANGUAGES)

class Tradutor(object):
	def __init__(self, lingua):
		self.translator = Translator()
		self.usuario = Usuario(lingua)
		self.lingua = lingua

	def traduzir(self, texto, lingua):
		tra = self.translator.translate(texto, dest=self.lingua)
		return tra.text

