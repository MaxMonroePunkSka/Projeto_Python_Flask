def aniversario(data_nasc):
    """Recebe uma data no formato AAAA-MM-DD e retorna um array com o mẽs e o dia."""
    data_array = data_nasc.split('-')
    data_array.pop(0)
    return data_array

