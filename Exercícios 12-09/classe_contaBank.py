class ContaBancaria:

    banco = "Banco Central"

    def __init__(self, titular, saldo):
        # banco = "Banco Central"
        self.titular = titular
        self.saldo = saldo

def apresentar(self):
    print(f"O titular {self.titular} possui saldo de R$ {self.saldo} cujo banco pertence ao {self.banco}")

conta1 = ContaBancaria("Juan", 500)
conta2 = ContaBancaria("Marilene", 300)

apresentar(conta1)
apresentar(conta2)
