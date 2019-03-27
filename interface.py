from threading import Thread
from cliente import Cliente, Send
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as GTK
from gi.repository import Gdk

class Window(GTK.Window):

	def __init__(self, cliente):

		GTK.Window.__init__(self, title = "Chat Auto Tradutor")
		self.set_default_size(800, 600)
		self.cliente = cliente
		Thread(target = self.receber_mensagem).start()

	def criar_janela(self):

			self.box = GTK.Box()
			self.Vbox1 = GTK.VBox()
			self.Hbox1 = GTK.HBox()
			
			
			self.scrolled = GTK.ScrolledWindow()
			self.scrolled.set_policy(GTK.PolicyType.NEVER, GTK.PolicyType.AUTOMATIC)

			self.but = GTK.Button(label = "Enviar")

			self.lCaixaTexto = GTK.Label()

			self.connect("key-release-event", self.tecla_solta)
			
			self.eMsg = GTK.Entry()
			self.eMsg.set_property("width-request", 750)

			self.scrolled.add(self.lCaixaTexto)
			self.Vbox1.add(self.scrolled)
			self.Hbox1.pack_start(self.eMsg,  False, True, 0)
			self.Hbox1.add(self.but)
			self.Vbox1.pack_start(self.Hbox1, False, True, 0)
			self.box.add(self.Vbox1)
			self.add(self.box)


	def tecla_solta(self, widget, ev):

		if ev.keyval == Gdk.KEY_Return:
			self.cliente.enviar_msg(self.eMsg.get_text())
			self.eMsg.set_text("")

	def receber_mensagem(self):

		while True:
			msg = self.cliente.pegar_msg()
			if msg:
				self.lCaixaTexto.set_text(self.lCaixaTexto.get_text() + "\n" + msg)
				self.cliente.resetar()

if __name__ == '__main__':

	cliente = Cliente("pt", "191.52.7.39")
	window = Window(cliente)
	window.criar_janela()
	window.connect("destroy", GTK.main_quit)
	window.show_all()
	GTK.main()