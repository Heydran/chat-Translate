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
	global tradutor
	tradutor = Tradutor("pt")

	return render_template("chat.html", msglog = pegar_mensagens(), usuario = session["usuario"])

@app.route("/enviar")
def enviar():
	global tradutor
	salvar_mensagem(tradutor.traduzir(request.args.get("msg")), session["cod_usuario"])
	return render_template("chat.html", msglog = pegar_mensagens(),  usuario = session["usuario"])

@app.route("/login")
def login():
	login = request.args.get("login")
	senha = request.args.get("senha")

	if (login != None) and (senha != None):
		if  senha == pegar_senha(login):
			session["logado"] = True
			session["usuario"] = pegar_nome(login)
			session["login"] = login
			session["cod_usuario"] = pegar_cod(login)
			return redirect("/sala_chat")
	return render_template("login_incorreto.html")

@app.route("/form_cadastrar")
def form_cadastrar():
	return render_template("form_cadastrar.html")

@app.route("/cadastrar")
def cadastrar():
	login = request.args.get("login")
	senha = request.args.get("senha")
	nome = request.args.get("nome")

	cadastrar_usuario(login, senha, nome)

	return redirect("/")

@app.route("/logout")
def logout():
	session["logado"] = False
	session["usuario"] = None
	session["login"] = None
	session["cod_usuario"] = None
	return redirect("/")
			

if __name__ == "__main__":
	app.run(debug = True, host ="0.0.0.0")