class Produto:
    def __init__(self, nome, preco=0):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if preco < 0:
            print("O preço não pode ser negativo")
        else:
            self.__preco = preco

produto1 = Produto("biscoito", 5)
produto2 = Produto("cerveja", 20)

produto2.preco = 10
produto2.preco = -20
print(produto2.preco)

