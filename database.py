import sqlite3

DATABASE = "loja_jogos.db"

def get_db():
    """Abre uma conexão com o banco e a retorna pronta para uso"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn