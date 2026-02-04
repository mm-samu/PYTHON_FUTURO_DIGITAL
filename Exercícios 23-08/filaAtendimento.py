#Olhar biblioteca collections.deque
class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def get_nome(self):
        return self.nome

    def get_nacionalidade(self):
        return self.nacionalidade

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

autor1 = Autor("Manuel","Brasileiro")
livro1 = Livro("História do Soul João", autor1)

print(livro1.get_titulo())
print(livro1.get_titulo().get_nacionalidade())


