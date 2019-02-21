from googletrans import Translator, LANGUAGES
translator = Translator()
print(LANGUAGES)
print()

class Usuario(object):
	def __init__(self, lingua):
		self.lingua = lingua
			

class Tradutor(object):
	def __init__(self):
		self.translator = Translator()

	def pt_en(self, texto):
		tra = self.translator.translate(texto, dest="pt")
		return tra.text

	def en_pt(self, texto):
		tra = self.translator.translate(texto, dest="en")
		return tra.text