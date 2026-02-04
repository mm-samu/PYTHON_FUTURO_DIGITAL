from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_bonus(self, valor):
        pass

class Gerente(Funcionario):
    def calcular_bonus(self, valor):
        return valor+(valor*0.3)

class Desenvolvedor:
    def calcular_bonus(self,valor):
        return valor+(valor*0.18)

gerente1 = Gerente()
print(gerente1.calcular_bonus(1000))
