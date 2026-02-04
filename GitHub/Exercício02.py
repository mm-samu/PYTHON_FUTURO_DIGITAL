def contar_vogais_e_consoantes(palavra):

    vogais = 0
    consoantes = 0

    palavra.lower()
    for i in palavra:
        if i in "aeiou":
            vogais += 1
        if i not in "aeiou" and i != " ":
            consoantes += 1
    print(f"Vogais:{vogais} | consoantes:{consoantes}")


def palindromo(nome):
    if nome == nome[::-1]:
        print(f"A palavra {nome} é um palíndromo")


running = True
while running:
    menu = int(input(("Escolha uma das opções:\n"
                      "\n1-Contar vogais e consoantes"
                      "\n2- Verificar palíndromo"
                      "\n3- Frequência de palavras"
                      "\n4-Verificador de senha forte"
                      "\n5- Gerar acrônico\n")))
    if menu == 1:
        frase = input("Digite uma frase: ")
        contar_vogais_e_consoantes(frase)

    if menu == 2:
        frase = input("Digite uma frase: ")
        lista = frase.split()
        for i in lista:
            palindromo(i)

    if menu ==3:
        frase = input("Digite uma frase: ")
        frase.lower()
        lista = frase.split()
        contador={}







