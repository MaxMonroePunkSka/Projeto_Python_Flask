from servicos.database import get_db

def get_jogos():
    conn = get_db()
    jogos = conn.execute("SELECT * FROM jogos ORDER BY id").fetchall()
    conn.close()
    return jogos