from flask import Flask, render_template, request, redirect

app = Flask("__name__")
app.secret_key = 'senha'
msg = ["ola","hellow"]
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/send")
def send():
    m = request.args.get("msg")
    msg.append(m)
    return redirect("/")

@app.route("/entry_room")
def entry_room():
    user = request.args.get("user")
    return render_template("chat.html", user = user)

@app.route("/msg_box")
def chat():
    return render_template("msg_box.html", msg = msg, user = request.args.get('user'))


app.run(debug = True)