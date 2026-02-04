class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

def verificar_aprovacao(self):
    if self.nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

aluno1 = Aluno("Samuel", 7)
aluno2 = Aluno("Juan", 5)

print(verificar_aprovacao(aluno1))
print(verificar_aprovacao(aluno2))