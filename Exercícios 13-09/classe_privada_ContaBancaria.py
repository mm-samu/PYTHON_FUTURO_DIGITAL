class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def ver_saldo(self):
        return self.__saldo


    def depositar(self, deposito):
        if deposito < 0:
            print("Não permitimos valor negativo")
        else:
            self.__saldo += deposito

    def sacar(self, saque):
        if saque >= self.__saldo or saque < 0:
            print("Coloque o valor do saque corretamente")
        else:
            self.__saldo -= saque

conta1 = ContaBancaria("Samuel", 100)

print(conta1.ver_saldo())
conta1.depositar(100)
print(conta1.ver_saldo())
conta1.sacar(90)
print(conta1.ver_saldo())

