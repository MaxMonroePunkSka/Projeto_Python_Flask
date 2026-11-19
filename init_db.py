from servicos.database import get_db

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            nota01 REAL DEFAULT 0,
            nota02 REAL DEFAULT 0,
            nota03 REAL DEFAULT 0,
            media REAL DEFAULT 0,
            categorias TEXT DEFAULT ''
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dataAniv DATE,
            apelido TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("Tabelas criadas.")

if __name__ == "__main__":
    init_db()