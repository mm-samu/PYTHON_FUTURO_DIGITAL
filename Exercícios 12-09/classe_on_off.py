class Lampada:
    def __init__(self, ligada):
        self.ligada = False

def ligar(self):
    self.ligada = True

def desligar(self):
    self.ligada = False

def apresentar(self):
    return self.ligada

lampada_sala = Lampada(True)
print(apresentar(lampada_sala))

ligar(lampada_sala)
print(apresentar(lampada_sala))