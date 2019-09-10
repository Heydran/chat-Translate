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

class Sala(Modelo):

	cod_sala = AutoField(primary_key = True)
	nome = CharField(unique=True)

class Mensagem(Modelo):

	cod_mensagem = AutoField(primary_key = True)
	conteudo = CharField()
	usuario = ForeignKeyField(Usuario, column_name = "cod_usuario")
	sala = ForeignKeyField(Sala)


def salvar_mensagem(conteudo, cod_usuario, sala):
	Mensagem(conteudo = conteudo, usuario = cod_usuario, sala = sala).save()


def pegar_cod_sala(nome_sala):
	try:
		return Sala.select().where(Sala.nome == nome_sala)[0].cod_sala
	except:
		return None

def pegar_cod(login):
	try:
		return Usuario.select().where(Usuario.login == login)[0].cod_usuario
	except:
		return None

def pegar_nome(login):
	try:
		return Usuario.select().where(Usuario.login == login)[0].nom_usuario
	except:
		return None

def pegar_senha(login):
	try:
		return Usuario.select().where(Usuario.login == login)[0].senha
	except:
		return None

def criar_sala_bd(nome_sala):

	if (nome_sala == "" and nome_sala == None):
		return None

	print(nome_sala)

	Sala(nome = nome_sala).save()

	return True

def pegar_mensagens(sala):
	return Mensagem.select().join(Sala).where(Sala.cod_sala == Mensagem.sala).order_by(Mensagem.cod_mensagem.desc()).limit(10)

def cadastrar_usuario(login, senha, nome):
	Usuario(nom_usuario = nome, senha = senha, login = login).save()

db.create_tables([Usuario, Mensagem, Sala])

if __name__ == '__main__':
	
	db.create_tables([Usuario, Mensagem, Sala])

	#u1 = Usuario(nom_usuario = "administrador2", senha = "admin", login = "admin").save()
	#m1 = Mensagem(mensagem = "teste", usuario = 1).save()
	#usuario = "admin"
	#print(Usuario.select().where(Usuario.nom_usuario == usuario)[0].senha)
	Usuario(nom_usuario = "nome", senha = "senha", login = "login").save()

	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()
	Mensagem(conteudo = "conteudo", usuario = 1, sala = 1).save()

	#Sala.select().join(Mensagens).where(Sala.nome == sala).order_by(Mensagem.cod_mensagem.desc()).limit(10)
	query = Mensagem.select().join(Sala).where(Sala.cod_sala == Mensagem.sala).order_by(Mensagem.cod_mensagem.desc()).limit(10)
	print(query)
	for i in query:
		print(i.cod_mensagem)
	