from abc import ABC, abstractmethod

class FormaGeometrical(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FormaGeometrical):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

retangulo = Retangulo(10, 10)
print(retangulo.calcular_area())


