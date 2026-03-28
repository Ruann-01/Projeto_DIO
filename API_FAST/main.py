# Autor: Ruann Campos
from flask import Flask, jsonify

app = Flask(__name__)

# Rota inicial
@app.route("/")
def home():
    return "API funcionando!"

# Rota que retorna dados
@app.route("/dados")
def dados():
    return jsonify({
        "nome": "Ruann",
        "curso": "Engenharia da Computação",
        "status": "Ativo"
    })

# Rota com parâmetro
@app.route("/saudacao/<nome>")
def saudacao(nome):
    return jsonify({
        "mensagem": f"Olá, {nome}!"
    })

# Executar a API
if __name__ == "__main__":
    app.run(debug=True)