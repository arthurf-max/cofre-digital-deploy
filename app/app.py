from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Lendo a senha do ambiente
    senha_banco = os.getenv('DB_PASSWORD', 'SENHA_NAO_CONFIGURADA')

    if senha_banco == 'SENHA_NAO_CONFIGURADA':
        status_seguranca = "Inseguro - Senha não encontrada no cofre!"
    else:
        status_seguranca = "Seguro - Conectado com sucesso ao banco!"

    return jsonify({
        "mensagem": "Bem-vindo ao Cofre Digital",
        "status": status_seguranca
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
