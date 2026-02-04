def calcular_frete(peso,distancia):
    if peso <= 10:
        return distancia*5

    if peso>10:
        return distancia*7

def test_calcular_frete():
    assert calcular_frete(5,10) == 50
    assert calcular_frete(11,10) == 70