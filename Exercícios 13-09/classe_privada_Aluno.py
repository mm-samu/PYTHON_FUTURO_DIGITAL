class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            print("O intervalo de notas deve ser só entre 0 a 10")
        else:
            self.__nota = nota


aluno1 = Aluno("Juan", 10)

aluno1.nota = 20
print("A nota no aluno é: ",aluno1.nota)
aluno1.nota = 6
print("A nota no aluno é: ",aluno1.nota)
