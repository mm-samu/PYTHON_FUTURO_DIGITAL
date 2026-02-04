from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

@abstractmethod
def emitir_som(self):
    print("Som genérico")

class Cachorro(Animal):

    def emitir_som(self):
        return ("Latido!")

cachorro1 = Cachorro("Alfred")
print(f"O animal chamado {cachorro1.nome} emitiu: " +cachorro1.emitir_som())
