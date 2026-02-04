running = True

while running:
    menu = int(input(("Escolha uma das opções:\n"
                      "\n1-Exercício 'criando seu primeiro dicionario'"
                      "\n2- Exercício tupla como valor no dicionário"
                      "\n3- Exercício 'tupla como chave no dicionário'"
                      "\n4-Exercício 'notas de alunos'"
                      "\n5- Exercício 'produtos e preço'\n"
                      "\n6- Exercício 'jogo da velha")))
    if menu == 1:

        dicionario ={
            "nome":"ana",
            "idade":"20",
            "cidade":"cajazeiras"
        }
        print(dicionario)

    if menu == 2:

        agenda = {
            "samuel":("83991385674","samuel.medeiros1@hotmail.com"),
            "ana":("83991857641","ana@hotmail.com")
        }
        print(agenda)
    if menu == 3:

        cidades={
            ("-6.88634","-38.5614") : "Cajazeiras",  # (latitude,longitude)
            ("-3.71839"," -25.4284") : "Fortaleza",
            ("49.2733", "-38.5434"): "Curitiba",
        }

        print(cidades)
    if menu == 4:

        alunos={
            "samuel":(10,9,7),
            "ana":(5,5,6),
        }

        for i in alunos:
            print(sum((alunos[i]))/len(alunos[i]))  # o alunos[i] pega o valor da chave(key)

    if menu == 5:

        precos={}
        produto= ""
        tamanho=""
        preco=0

        vezes = int(input("Deseja cadastrar quantos produtos?"))

        for _ in range(vezes):
            produto = input("Digite o produto: ")
            tamanho = input("Digite o tamanho do produto: ")
            preco = int(input("Digite o preço do produto: "))
            precos[produto,tamanho] = preco

        print(precos)

    if menu == 6:

        tabuleiro={
        (0,0): "-", (0,1): "-", (0,2): "-",
        (1,0): "-", (1,1): "-", (1,2): "-",
        (2,0): "-", (2,1): "-", (2,2): "-"
        }

        for i in tabuleiro:
            if tabuleiro[i] == "x" and  







