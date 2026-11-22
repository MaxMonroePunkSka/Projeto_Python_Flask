from servicos.database import get_db

def media(array_notas):
    """Recebe um array e retorna uma média arredondada."""
    if not array_notas:
        return 0
    return round(sum(array_notas) / len(array_notas), 1)

def get_jogos():
    conn = get_db()
    jogos = conn.execute("SELECT * FROM clientes ORDER BY id").fetchall()
    conn.close()
    return jogos