from flask import Blueprint, render_template, request, redirect, url_for, flash
from servicos.operacoes_clientes import aniversario

clientes_bp = Blueprint("clientes", __name__)

clientes = []

@clientes_bp.route("/clientes")
def listar():
    return render_template("clientes/lista.html", clientes=clientes)

@clientes_bp.route("/clientes/<int:id>")
def detalhes(id):
    cliente = next((c for c in clientes if c["id"] == id), None)
    if not cliente:
        return "Cliente não encontrado", 404
    return render_template("clientes/detalhes.html", cliente=cliente)

@clientes_bp.route("/clientes/novo", methods=["GET", "POST"])
def novo():
    erro = None
    if request.method == "POST":
        nome = request.form.get("nome", "")
        data_aniv = aniversario(request.form.get("data-nasc", ""))
        apelido = request.form.get("apelido", "")
        if not nome or not data_aniv or not apelido:
            erro = "Preencha todos os campos."
        else:
            clientes.append({"id": len(clientes), "nome": nome, "data_aniv": data_aniv, "apelido": apelido})
            flash("Cliente cadastrado com sucesso!")
            return redirect(url_for('clientes.listar'))
    return render_template("clientes/form.html", erro=erro)

