class DispositivoEletronico():
    def __init__(self, nome: str):
        self.nome = nome

    def ligar(self):
        pass

    def desligar(self):
        return 1

class Computador(DispositivoEletronico):

    def instalar_software(self):
        return f"software instalado no notebook {self.nome}"

class Notebook(Computador):

    def verificar_bateria(self):
        return "bateria em 20%"

notebook = Notebook("ASUS")

print(notebook.verificar_bateria())
print(notebook.desligar())
print(notebook.instalar_software())


