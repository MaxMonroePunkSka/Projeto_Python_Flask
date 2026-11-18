from flask import Flask, render_template
from rotas.clientes import clientes_bp, clientes
from rotas.jogos import jogos_bp, jogos

app = Flask(__name__)
app.secret_key = 'projeto01-secreta'

app.register_blueprint(clientes_bp)
app.register_blueprint(jogos_bp)

@app.route("/")
def index():
    return render_template('index.html', total_clientes=len(clientes), total_jogos=len(jogos))

if __name__ == "__main__":
    app.run(debug=True)