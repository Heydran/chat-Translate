from peewee import *

db = SqliteDatabase("Mensagens.db")
db.connect()

class Modelo(Model):
	class Meta:
		database = db

class Usuario(Modelo):
	cod_usuario = AutoField(primary_key = True)
	nom_usuario =  CharField()
	senha = CharField()
	login = CharField()

class Mensagem(Modelo):
	cod_mensagem = AutoField(primary_key = True)
	conteudo = CharField()
	usuario = ForeignKeyField(Usuario, column_name = "cod_usuario")

def salvar_mensagem(conteudo, cod_usuario):
	Mensagem(conteudo = conteudo, usuario = cod_usuario).save()

def pegar_cod(login):
	return Usuario.select().where(Usuario.login == login)[0].cod_usuario

def pegar_nome(login):
	return Usuario.select().where(Usuario.login == login)[0].nom_usuario

def pegar_senha(login):
	return Usuario.select().where(Usuario.login == login)[0].senha

def pegar_mensagens():
	return Mensagem.select()

def cadastrar_usuario(login, senha, nome):
	Usuario(nom_usuario = nome, senha = senha, login = login).save()

if __name__ == '__main__':
	
	db.create_tables([Usuario, Mensagem])

	u1 = Usuario(nom_usuario = "administrador2", senha = "admin", login = "admin").save()
	#m1 = Mensagem(mensagem = "teste", usuario = 1).save()
	#usuario = "admin"
	#print(Usuario.select().where(Usuario.nom_usuario == usuario)[0].senha)
	Usuario(nom_usuario = "nome", senha = "senha", login = "login").save()
	

	for i in Usuario.select():
		print(i.login)
	