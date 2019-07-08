from flask import Flask, render_template, request, redirect, session
from peewee_site import *

app = Flask(__name__)
app.secret_key = 'senha'

@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/enviar")
def enviar():
	m = Mensagem(mensagem = request.args.get("msg"), cod_usuario = session["cod_usuario"]).save()
	return render_template("chat.html")

@app.route("/sala_chat")
def sala_chat():
	session["usuario"] = request.args.get("usuario")
	session["sala"] = request.args.get("sala")
	session["cod_usuario"] = pegar_cod(session["usuario"])

	return render_template("chat.html")

@app.route("/msg_box")
def msg_box():
	msg = pegar_mensagens()
	return render_template("msg_box.html", msg = msg)

if __name__ == "__main__":
	app.run(debug = True)