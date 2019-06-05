try:
	from googletrans import Translator, LANGUAGES
except:
	import os
	os.system("pip3 install googletrans")
	from googletrans import Translator, LANGUAGES

from threading import Thread

class Tradutor(object):
	def __init__(self, lingua):
		self.translator = Translator()
		#self.usuario = Usuario(lingua)
		self.lingua = lingua

	def traduzir(self, texto):
		tra = self.translator.translate(texto, dest=self.lingua)
		return tra.text

if __name__ == '__main__':
	o = Tradutor("pt")
	print(o.traduzir("hi"))