from flask import Flask, render_template
from rotas.clientes import clientes_bp
from rotas.jogos import jogos_bp
from servicos.operacoes_clientes import get_clientes
from servicos.operacoes_jogos import get_jogos

app = Flask(__name__)
app.secret_key = 'projeto01-secreta'

app.register_blueprint(clientes_bp)
app.register_blueprint(jogos_bp)

@app.route("/")
def index():
    clientes = get_clientes()
    jogos = get_jogos()
    return render_template('index.html', total_clientes=len(clientes), total_jogos=len(jogos))

if __name__ == "__main__":
    app.run(debug=True)