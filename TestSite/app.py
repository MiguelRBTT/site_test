from flask import Flask, render_template

app = Flask(__name__)

# route -> algumacoisa.com/contatos -> é o caminho da URL
# função é o que quero exibir naquela página
# templates

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


#criando uma página dinâmica
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)


# colocar o site no ar
if __name__ == "__main__":

    app.run(debug=True)