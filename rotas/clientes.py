from flask import Blueprint, render_template, request, redirect, url_for, abort
from servicos.database import get_db

clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")

conn = get_db()
clientes = conn.execute("SELECT * FROM clientes ORDER BY nome").fetchall()
conn.close()

@clientes_bp.route("/")
def listar():
    return render_template("clientes/lista.html", clientes=clientes)

@clientes_bp.route("/<int:id>")
def detalhes(id):
    conn = get_db()
    cliente = conn.execute("SELECT * FROM clientes WHERE id = ?", (id,)).fetchone()
    conn.close()

    if cliente is None:
        abort(404)
    return render_template("clientes/detalhes.html", cliente=cliente)

@clientes_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        nome = request.form["nome"].strip()
        data_nasc = request.form["data-nasc"].strip()
        apelido = request.form["apelido"].strip()

        if not nome or not data_nasc or not apelido:
            return render_template("clientes/form.html", erro = "Preencha todos os campos.")
        else:
            conn = get_db()
            conn.execute(
                "INSERT INTO clientes (nome, dataNasc, apelido) " \
                "VALUES (?, ?, ?)",
                (nome, data_nasc, apelido)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('clientes.listar'))

    return render_template("clientes/form.html", erro=None)

