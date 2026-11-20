from servicos.database import get_db

def aniversario(data_nasc):
    """Recebe uma data no formato AAAA-MM-DD e retorna um array com o mẽs e o dia."""
    data_array = data_nasc.split('-')
    data_array.pop(0)
    return data_array

def get_clientes():
    conn = get_db()
    clientes = conn.execute("SELECT * FROM clientes ORDER BY id").fetchall()
    conn.close()
    return clientes

