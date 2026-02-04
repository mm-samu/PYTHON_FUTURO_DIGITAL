from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self,marca,velocidade):
        self.marca = marca
        self.velocidade = velocidade

@abstractmethod
def acelerar(self, velocidade):
    pass
@abstractmethod
def frear(self, velocidade):
    pass

class Carro(Veiculo):
    def acelerar(self):
        self.velocidade = self.velocidade+(self.velocidade*0.40)
        return self.velocidade

    def frear(self):
        self.velocidade = self.velocidade - (self.velocidade * 0.30)
        return self.velocidade

class Moto(Veiculo):
    def acelerar(self):
        self.velocidade = self.velocidade + (self.velocidade * 0.25)
        return self.velocidade

    def frear(self):
        self.velocidade = self.velocidade - (self.velocidade * 0.20)
        return self.velocidade

carro1 = Carro("fiat",30)
moto1 = Moto("yamaha",40)

print(carro1.velocidade)
print(carro1.acelerar())
print(carro1.frear())

print(moto1.velocidade)
print(moto1.acelerar())
print(moto1.frear())
