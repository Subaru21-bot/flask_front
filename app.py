from flask import Flask, render_template

app = Flask(__name__)

# Criar 1º página do site
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/usuarios/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)