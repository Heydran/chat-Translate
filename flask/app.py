from flask import Flask, render_template, request, redirect, session
from peewee_site import *
from tradutor import *
tradutor = Tradutor("pt")
app = Flask(__name__)
app.secret_key = 'senha'

@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/sala_chat")
def sala_chat():
	session["usuario"] = request.args.get("usuario")
	session["sala"] = request.args.get("sala")
	try:
		session["cod_usuario"] = pegar_cod(session["usuario"])
	except:
		Usuario(nom_usuario = session["usuario"]).save()
		session["cod_usuario"] = pegar_cod(session["usuario"])
	global tradutor
	tradutor = Tradutor("pt")

	return render_template("chat.html", msglog = pegar_mensagens(), user = session["usuario"])

@app.route("/enviar")
def enviar():
	global tradutor
	Mensagem(mensagem = tradutor.traduzir(request.args.get("msg")), usuario = session["cod_usuario"]).save()
	return render_template("chat.html", msglog = pegar_mensagens())

if __name__ == "__main__":
	app.run(debug = True, host ="0.0.0.0")