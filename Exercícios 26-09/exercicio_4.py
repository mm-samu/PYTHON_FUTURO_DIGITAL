from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod

    def rodas(self):
        pass

class Carro(Veiculo):
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.roda = 4

    def rodas(self):
        return f"A quantidade de rodas do carro é {self.roda}"

    def acelerar(self):
        self.velocidade = self.velocidade + 15
        return f"A sua velocidade agora está em {self.velocidade}"

class Moto(Veiculo):
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.roda = 2

    def rodas(self):
        return f"A quantidade de rodas da moto é {self.roda}"

    def acelerar(self):
        self.velocidade = self.velocidade + 9
        return f"A sua velocidade agora está em {self.velocidade}"

carro1 = Carro(20)
print(carro1.acelerar())
print(carro1.rodas())

moto1 = Moto(10)
print(moto1.acelerar())
print(moto1.rodas())




