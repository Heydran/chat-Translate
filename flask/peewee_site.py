from peewee import *

db = SqliteDatabase("Mensagens.db")
db.connect()

class Modelo(Model):
	class Meta:
		database = db

class Usuario(Modelo):
	cod_usuario = AutoField(primary_key = True)
	nom_usuario =  CharField()

class Mensagem(Modelo):
	cod_mensagem = AutoField(primary_key = True)
	mensagem = CharField()
	usuario = ForeignKeyField(Usuario, column_name = "cod_usuario")

def pegar_cod(usuario):
	return Usuario.select().where(Usuario.nom_usuario == usuario)[0].cod_usuario

def pegar_mensagens():
	return Mensagem.select()

if __name__ == '__main__':
	
	db.create_tables([Usuario, Mensagem])

	u1 = Usuario(nom_usuario = "user").save()
	m1 = Mensagem(mensagem = "teste", usuario = 1).save()

	for msg in Mensagem.select():
		print(msg.usuario.nom_usuario)
	