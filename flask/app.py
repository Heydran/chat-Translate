from flask import Flask, render_template, request, redirect, session
from peewee_site import *
from tradutor import *
tradutor = Tradutor("pt")
app = Flask(__name__)
app.secret_key = 'senha'
@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/entrar_sala")
def entrar_sala():
	session["sala"] = request.args.get(sala)
	return redirect("/sala_chat")

@app.route("/sala_chat")
def sala_chat():
	return render_template("chat.html", msglog = pedir_mensagens(session["sala"]), usuario = session["usuario"])

def pedir_mensagens(sala):
	global tradutor
	mensagens = pegar_mensagens(sala)
	for i in mensagens:
		i.conteudo = tradutor.traduzir((i.conteudo))
	return mensagens[::-1]

@app.route("/enviar")
def enviar():
	salvar_mensagem((request.args.get("msg")), session["cod_usuario"], session["sala"])
	return render_template("chat.html", msglog = pedir_mensagens(session["sala"]),  usuario = session["usuario"])

@app.route("/form_login")

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
			session["sala"] = request.args.get("sala")
			return redirect("/")
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

@app.route("/form_criar_sala")
def form_criar_sala():
	
	if (not session["logado"]):
		return redirect("/")
	
	return render_template("form_criar_sala.html")

@app.route("/criar_sala")
def criar_sala():

	nome_sala = request.args.get("nome_sala")
	
	if (criar_sala_bd(nome_sala)):
		return redirect("/")

	return redirect("/form_criar_sala", status = "Erro ao criar a sala")

if __name__ == "__main__":
	app.run(debug = True, host ="0.0.0.0")