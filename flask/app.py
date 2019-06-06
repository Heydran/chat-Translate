from flask import Flask, render_template, request, redirect

global_user = ["Default"]

app = Flask(__name__)
app.secret_key = 'senha'
msg = ["ola","hellow"]

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/send")
def send():

	m = request.args.get("msg")
	msg.append(m)
	print(global_user)
	return render_template("chat.html", user = global_user, key = "duh")

@app.route("/entry_room")
def entry_room():
	global_user[0] = request.args.get("user")
	return render_template("chat.html", user = global_user, key = "duh")

@app.route("/msg_box")
def chat():
	return render_template("msg_box.html", msg = msg, user = global_user[0])

if __name__ == "__main__":

	app.run(debug = True)