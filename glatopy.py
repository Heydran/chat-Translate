import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("gtk glade.glade")
window = builder.get_object("janela")
window.show_all()