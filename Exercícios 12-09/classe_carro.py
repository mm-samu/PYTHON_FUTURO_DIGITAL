class Carro:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano

def apresentar(self):
    print(f"A marca do carro é {self.marca} e o ano é {self.ano}")

marca = input("Digite o marca do carro: ")
ano = input("Digite o ano do carro: ")
meu_carro = Carro(marca,ano)

apresentar(meu_carro)