from flask import Blueprint, render_template, request, redirect, url_for, flash
from servicos.operacoes_jogos import media

jogos_bp = Blueprint("jogos", __name__)

jogos = [
    {"id": 0, "titulo": "Minecraft", "nota": 8.9, "categorias": ["sobrevivencia", "aventura"]},
    {"id": 1, "titulo": "Dead Cells", "nota": 9.0, "categorias": ["heck'n'slash", "roguelike"]},
    {"id": 2, "titulo": "Cult of The Lamb", "nota": 8.5, "categorias": ["roguelike", "roguelite"]},
]

@jogos_bp.route("/jogos")
def listar():
    return render_template("jogos/lista.html", jogos=jogos)

@jogos_bp.route("/jogos/<int:id>")
def detalhes(id):
    jogo = next((j for j in jogos if j["id"] == id), None)
    if not jogo:
        return "Jogo não encontrado", 404
    return render_template("jogos/detalhes.html", jogo=jogo)

@jogos_bp.route("/jogos/novo", methods=["GET", "POST"])
def novo():
    erro = None
    if request.method == "POST":

        titulo = request.form.get("titulo", "").strip()
        nota01 = float(request.form.get("nota01", 0) or 0)
        nota02 = float(request.form.get("nota02", 0) or 0)
        nota03 = float(request.form.get("nota03", 0) or 0)
        cat01 = request.form.get("categoria01", "").strip()
        cat02 = request.form.get("categoria02", "").strip()
        notas = [nota01, nota02, nota03]
        categorias = [cat01, cat02]

        if not titulo:
            erro = "O título é obrigatório"
        else:
            jogos.append({
                "id": len(jogos),
                "titulo": titulo,
                "nota": media(notas),
                "categorias": categorias,
            })
            flash("Jogo adicionado!")
            return redirect(url_for('jogos.listar'))

    return render_template("jogos/form.html", erro=erro)

