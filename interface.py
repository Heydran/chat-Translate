import cliente
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as GTK
from gi.repository import Gdk

class Window(GTK.Window):
	def __init__(self, cliente):
		GTK.Window.__init__(self, title = "Chat Auto Tradutor")

	def criar_janela(self):
			self.box = GTK.Box()
			self.Vbox1 = GTK.VBox()


			self.lCaixaTexto = GTK.Label(label = "")

			self.connect("key-release-event", self.tecla_solta)
			
			self.eMsg = GTK.Entry()

			self.bMus1 = GTK.Button(label = "Play")

			self.Vbox1.add(self.lCaixaTexto)
			self.Vbox1.add(self.eMsg)

			self.box.add(self.Vbox1)
			self.add(self.box)

	def tecla_solta(self, widget, ev):
		if ev.keyval == Gdk.KEY_Return:
			self.eMsg.set_text("")

	def receber_mensagem(self):
		pass#self.lCaixaTexto.set_text(self.lCaixaTexto.get_text() + "\n" + self.eMsg.get_text())

if __name__ == '__main__':
	cliente = cliente.Cliente("pt")
	window = Window(cliente)
	window.criar_janela()
	window.connect("destroy", GTK.main_quit)
	window.show_all()
	GTK.main()	