class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome,salario)
        self.departamento = departamento

gerente = Gerente('samu', 200, "salão")

print(gerente.nome)
print(gerente.salario)
print(gerente.departamento)

