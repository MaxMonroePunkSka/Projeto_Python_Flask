from servicos.database import get_db

def aniversario(data_nasc):
    """Recebe uma data em string no formato AAAA-MM-DD e retorna uma string no formato DD/MM."""
    data_array = data_nasc.split('-')
    data_array.pop(0)
    return f"{data_array[1]}/{data_array[0]}"

def get_clientes():
    conn = get_db()
    clientes = conn.execute("SELECT * FROM clientes ORDER BY id").fetchall()
    conn.close()
    return clientes

