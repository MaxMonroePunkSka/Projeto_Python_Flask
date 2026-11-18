def media(array_notas):
    """Recebe um array e retorna uma média arredondada."""
    if not array_notas:
        return 0
    return round(sum(array_notas) / len(array_notas), 1)

