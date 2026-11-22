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
            dataNasc TEXT,
            apelido TEXT NOT NULL
        )
    """)

    conn.execute(
        "INSERT INTO jogos (titulo, nota01, nota02, nota03, media, categorias)" \
        "VALUES" \
        "('Minecraft', 8.9, 9.0, 9.2, 9.0, 'sobrevivencia, aventura')," \
        "('Cult of The Lamb', 9.0, 8.0, 8.5, 8.5, 'roguelike, roguelite')," \
        "('Dead Cells', 10.0, 9.0, 8.0, 9.0, 'heck-n-slash, roguelike')"
    )

    conn.commit()
    conn.close()
    print("Tabelas criadas.")

if __name__ == "__main__":
    init_db()