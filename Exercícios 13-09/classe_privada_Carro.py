class Carro:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.__velocidade = velocidade

    def acelerar(self, velocidade):
        self.__velocidade += velocidade

    def frear(self, velocidade):
        if self.__velocidade-velocidade < 0:
            print("A velocidade não pode ficar negativa")
        else:
            self.__velocidade -= velocidade

    def ver_velocidade(self):
        return self.__velocidade

carro1 = Carro("modelo", 5)

carro1.acelerar(10)
print(carro1.ver_velocidade())
carro1.frear(20)
print(carro1.ver_velocidade())
carro1.frear(-100)
