nome = input("Digite um nome")
nome.upper()
comparacao = nome[::-1]
if (nome == comparacao):
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")

