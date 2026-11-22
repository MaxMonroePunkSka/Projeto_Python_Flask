from flask import Blueprint, render_template, request, redirect, url_for, abort
from servicos.operacoes_jogos import get_jogos, get_db

jogos_bp = Blueprint("jogos", __name__, url_prefix="/jogos")

@jogos_bp.route("/")
def listar():
    jogos = get_jogos()
    return render_template("jogos/lista.html", jogos=jogos)

@jogos_bp.route("/<int:id>")
def detalhes(id):
    conn = get_db()
    jogo = conn.execute("SELECT * FROM jogos WHERE id = ?", (id,)).fetchone()
    conn.close()
    
    if jogo is None:
        abort(404)
    return render_template("jogos/detalhes.html", jogo=jogo)

@jogos_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":

        titulo = request.form["titulo"].strip()
        nota01 = float(request.form["nota01"])
        nota02 = float(request.form["nota02"])
        nota03 = float(request.form["nota03"])
        cat01 = request.form["categoria01"].strip()
        cat02 = request.form["categoria02"].strip()
        media = (nota01 + nota02 + nota03)/3
        categorias = f"{cat01}, {cat02}"

        if not titulo:
            return render_template("jogos/form.html", erro = "O título é obrigatório.")
        else:
            conn = get_db()
            conn.execute(
                "INSERT INTO jogos (titulo, nota01, nota02, nota03, media, categorias)" \
                "VALUES (?, ?, ?, ?, ?, ?)",
                (titulo, nota01, nota02, nota03, media, categorias)
            )
            return redirect(url_for('jogos.listar'))

    return render_template("jogos/form.html", erro=None)

