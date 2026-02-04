try:
    numero = int(input("Digite um número para verificar se é par ou impar:\n"))
    if numero%2 == 0:
        print("O número é par")
    else:
        print( "O número é impar")
except Exception as e:
    print("O que você inseriu não é um número. Tente novamente!")