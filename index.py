import json

from flask import Flask, request
from person import *
import json

app = Flask(__name__)

@app.route("/teste")
def index():
    return "Olá Mundo! "

@app.route("/list/pessoa/<id>")
def listaPessoa(id):
    pessoa = Person("maria", 30)
    dictPessoa = pessoa.__dict__
    jsonPessoa = json.dumps(dictPessoa)
    return jsonPessoa

@app.route("/inhh/pessoa", methods=["POST"])
def criarPessoa():
    id = str(request.form.get("id"))
    nome = str(request.form.get("nome"))
    idade = str(request.form.get("idade"))
    arq = open("pessa.txt", "a")
    arq.write(id + "#" + nome + "#" + idade + "\n")
    arq.close()
    return "dado criados com sucesso!"

@app.route("/")
def home():
    return str(100*3**2-50)

if __name__== "__main__":
    app.run()

# procedimentos para fazer:
# git bash
# curl http:...
# curl -X"POST" -d "id=18 none = maria 8idade = 30"


